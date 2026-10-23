#!/usr/bin/env python3
"""
Bloomberg Agent Hive v6.0 - Web Terminal Local Backend Server
Uses pure Python standard library (http.server) with zero external dependencies.
Serves the institutional HTML5/CSS3/JS Web Terminal and provides REST APIs
for live multi-agent analysis, autopsy logging, and autonomous evolution.
"""
import http.server
import json
import os
import socketserver
import subprocess
import sys
import urllib.parse

PORT = 5050
WEB_DIR = os.path.dirname(os.path.abspath(__file__))
SCRIPTS_DIR = os.path.join(os.path.dirname(WEB_DIR), "scripts")
QUANT_ENGINE = os.path.join(SCRIPTS_DIR, "quant_engine.py")

class TerminalRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=WEB_DIR, **kwargs)

    def do_GET(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/status":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            memory_file = os.path.join(SCRIPTS_DIR, "trade_autopsy_memory.json")
            if os.path.exists(memory_file):
                with open(memory_file, "r", encoding="utf-8") as f:
                    data = f.read()
                self.wfile.write(data.encode("utf-8"))
            else:
                self.wfile.write(json.dumps({"status": "READY", "epoch": 1}).encode("utf-8"))
            return

        elif parsed.path == "/api/analyze":
            qs = urllib.parse.parse_qs(parsed.query)
            symbol = qs.get("symbol", ["NIFTY"])[0]
            capital = qs.get("capital", ["100000"])[0]
            risk = qs.get("risk", ["1.0"])[0]
            
            # Execute quant_engine.py in analyze mode
            cmd = [sys.executable, QUANT_ENGINE, "--symbol", symbol, "--capital", capital, "--risk", risk]
            try:
                out = subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=15).decode("utf-8")
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(out.encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        elif parsed.path == "/api/latest-signals":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            signals_file = os.path.join(WEB_DIR, "live_signals.json")
            if os.path.exists(signals_file):
                with open(signals_file, "r", encoding="utf-8") as f:
                    data = f.read()
                self.wfile.write(data.encode("utf-8"))
            else:
                self.wfile.write(json.dumps({"status": "WAITING_FOR_GEMINI_SIGNALS"}).encode("utf-8"))
            return

        super().do_GET()

    def do_POST(self):
        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/api/autopsy":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                payload = json.loads(body)
                outcome = payload.get("outcome", "loss")
                failure = payload.get("failure_type", "liquidity_trap")
                notes = payload.get("notes", "Web Terminal Logging")
                
                # Execute autopsy update
                cmd = [sys.executable, QUANT_ENGINE, "--mode", "autopsy", "--outcome", outcome,
                       "--failure-type", failure, "--notes", notes]
                subprocess.check_output(cmd, stderr=subprocess.STDOUT, timeout=10)

                # Execute autonomous evolution
                cmd_evolve = [sys.executable, QUANT_ENGINE, "--mode", "evolve"]
                evolve_out = subprocess.check_output(cmd_evolve, stderr=subprocess.STDOUT, timeout=10).decode("utf-8")

                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(evolve_out.encode("utf-8"))
            except Exception as e:
                self.send_response(500)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        elif parsed.path == "/api/push-signals":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length).decode("utf-8")
            try:
                payload = json.loads(body)
                signals_file = os.path.join(WEB_DIR, "live_signals.json")
                with open(signals_file, "w", encoding="utf-8") as f:
                    json.dump(payload, f, indent=2)
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.send_header("Access-Control-Allow-Origin", "*")
                self.end_headers()
                self.wfile.write(json.dumps({"status": "SUCCESS", "message": "Signals updated by Gemini"}).encode("utf-8"))
            except Exception as e:
                self.send_response(400)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps({"error": str(e)}).encode("utf-8"))
            return

        self.send_response(404)
        self.end_headers()

def run_server():
    socketserver.TCPServer.allow_reuse_address = True
    port = PORT
    for attempt in range(5):
        try:
            with socketserver.TCPServer(("", port), TerminalRequestHandler) as httpd:
                print(f"\n==================================================================")
                print(f"  BLOOMBERG AGENT HIVE v6.0 WEB TERMINAL SERVER ACTIVE")
                print(f"  Local URL: http://localhost:{port}")
                print(f"  Network URL: http://127.0.0.1:{port}")
                print(f"==================================================================\n")
                sys.stdout.flush()
                httpd.serve_forever()
        except OSError:
            port += 1

if __name__ == "__main__":
    run_server()
