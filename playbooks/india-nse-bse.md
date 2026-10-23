# Playbook A: Indian Markets (NSE / BSE, Nifty 50, BankNifty, Sensex & F&O)

## When to Activate

Activate this playbook whenever the target asset is an Indian index (`NIFTY 50`, `BANKNIFTY`, `FINNIFTY`, `MIDCPNIFTY`, `SENSEX`) or any equity/derivative listed on the **National Stock Exchange (NSE)** or **Bombay Stock Exchange (BSE)**.

## 1. Pre-Market & Global Handover Protocol (Before & At 9:15 AM IST)

Check the global-to-domestic liquidity handover before approving any morning trade:

- **GIFT Nifty (`GIFT NIFTY`):** Check the premium or discount relative to the previous NSE Nifty 50 close to gauge the 9:15 AM IST gap-up or gap-down magnitude.
- **Macro & Currency Cues:** Check overnight US closes (S&P 500, Nasdaq 100), Asian session trajectory (Nikkei, Hang Seng), **USD/INR** (`> 84.50` rising rapidly pressures FII flows), and **Brent Crude Oil** (sharp crude spikes pressure Indian inflation and paint/aviation/oil-marketing stocks).
- **Indian ADR Cues:** Check overnight NYSE closes for **HDFC Bank ADR (`HDB`)**, **ICICI Bank ADR (`IBN`)**, and **Infosys ADR (`INFY`)**.

## 2. Index Heavyweight Alignment Engine

Nifty 50 and BankNifty cannot sustain a structural breakout if their top weighted constituents are diverging:

- **For Nifty 50 Setups:** Verify live intraday alignment across the Top 5 heavyweights (~40% combined index weight):
  1. **HDFC Bank (`HDFCBANK`)**
  2. **Reliance Industries (`RELIANCE`)**
  3. **ICICI Bank (`ICICIBANK`)**
  4. **Infosys (`INFY`)**
  5. **TCS (`TCS`) / Larsen & Toubro (`LT`)**
- **For BankNifty Setups:** Verify alignment across **HDFC Bank, ICICI Bank, State Bank of India (`SBIN`), Kotak Mahindra Bank (`KOTAKBANK`), and Axis Bank (`AXISBANK`)**.
- **Trap Filter:** If Nifty breaks above resistance while HDFC Bank and Reliance are trading below their intraday VWAP with negative delta, flag a **Heavyweight Divergence Bull Trap** and block the long entry.

## 3. 2026 NSE F&O Lot Specifications, Ban List & Option Greeks Protocol

- **Standardized 2026 NSE Lot Sizes:**
  - `NIFTY`: **65 units**
  - `BANKNIFTY`: **30 units**
  - `FINNIFTY`: **60 units**
  - `MIDCPNIFTY`: **120 units**
  - `NIFTYNXT50`: **25 units**
  - `SENSEX` (BSE): **20 units**
- **NSE F&O Ban List Check:** For any individual stock F&O trade, search `"NSE F&O ban list today"` to ensure the stock has not crossed 95% of the Market-Wide Position Limit (MWPL). Taking new F&O positions in banned stocks incurs heavy exchange penalties.
- **India VIX & Theta Decay Filter:**
  - When **India VIX is below 12-13 or dropping intraday**, option premiums suffer rapid Theta (time) decay. Warn against buying naked Out-of-The-Money (OTM) options; favor **Futures, Cash Equities, In-The-Money (ITM) options (`Delta >= 0.65`), or Credit Spreads**.
- **NSE Session Killzones (IST):**
  - **Killzone 1 - Morning Opening Discovery:** `9:15 AM to 10:30 AM IST` (Wait for the first 5m or 15m candle close to settle opening gap retail emotion before entering Opening Range Breakouts or VWAP pullbacks).
  - **Midday Chop Danger Zone:** `11:15 AM to 1:15 PM IST` (Low institutional volume and high Theta decay; block breakout option buying).
  - **Killzone 2 - European Overlap & Institutional Closing Wave:** `1:30 PM to 3:15 PM IST` (Institutional VWAP execution and closing trend wave).

## 4. Weekly / Monthly Expiry Day (Gamma & Max Pain) Protocol

On NSE Nifty or BSE Sensex expiry days:

- **Morning to Midday (`9:15 AM - 1:30 PM IST`):** Expect price pinning between the highest Call OI wall and highest Put OI wall around the **Max Pain** strike as institutional option sellers harvest Theta decay.
- **Post-1:45 PM IST Gamma Window (`1:45 PM - 3:05 PM IST`):** Watch for a high-volume breach of the day's highest Call OI or Put OI strike accompanied by unwinding (negative change in OI by trapped writers). Only approve "Zero-to-Hero" or Gamma breakout trades if volume exceeds 2x average and top index heavyweights confirm the break.
