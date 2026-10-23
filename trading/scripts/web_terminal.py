#!/usr/bin/env python3
"""
Convenience launcher for Bloomberg Agent Hive Web Terminal.
Starts the local server and optionally opens the browser.
"""
import os, sys, subprocess, webbrowser

def main():
    web_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "web")
    server_script = os.path.join(web_dir, "server.py")
    
    print("Launching Bloomberg Agent Hive v6.0 Institutional Web Terminal...")
    print(f"Server script: {server_script}")
    
    # Try opening browser after 1 second
    try:
        webbrowser.open("http://localhost:8888")
    except Exception:
        pass
        
    cmd = [sys.executable, server_script]
    subprocess.call(cmd)

if __name__ == "__main__":
    main()
