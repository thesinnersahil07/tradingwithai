# Playbook B: Forex & Commodities (Major/Minor Pairs, Gold XAU/USD, Silver & Crude)

## When to Activate

Activate this playbook whenever the target asset is a global currency pair (`EUR/USD`, `GBP/USD`, `USD/JPY`, `GBP/JPY`, `AUD/USD`, `USD/CAD`, `USD/CHF`, `USD/INR`) or spot/futures commodity (`XAU/USD` Gold, `XAG/USD` Silver, `WTI / Brent Crude`).

## 1. Asian Session Range Sweep & ICT Killzone Protocol

Global FX and Gold operate on a 24-hour interbank liquidity cycle driven by Tokyo, London, and New York session handovers:

- **Step 1 - Map the Asian Session Box:** Mark the high and low formed during the Tokyo/Asian consolidation window (`5:30 AM to 11:30 AM IST` / `00:00 to 06:00 UTC`). Retail traders place breakout orders and stop-losses directly above the Asian High and below the Asian Low.
- **Step 2 - Spot the "Judas Swing" (False Breakout / Liquidity Sweep):**
  - At the **London Open** or **New York Open**, algorithms frequently spike price 10-25 pips above the Asian High (or below the Asian Low) to sweep retail stop-losses and tap a higher-timeframe 1H/4H Order Block or Fair Value Gap.
  - **Never chase the initial breakout of the Asian range.** Wait for a sweep of the Asian High/Low, a 5m/15m **Market Structure Shift (MSS / CHoCH)** back inside the range with displacement, and enter on the retracement into the newly formed **Fair Value Gap (FVG)**.
- **Official Session Killzones (IST / UTC / EST):**
  - **London Open Killzone:** `12:30 PM to 3:30 PM IST` (`11:30 AM to 2:30 PM IST` during UK Summer BST) | `07:00 to 10:00 UTC` | `02:00 to 05:00 EST`.
  - **New York Open Killzone:** `5:30 PM to 8:30 PM IST` (US Summer EDT) / `6:30 PM to 9:30 PM IST` (US Winter EST) | `12:00 to 15:00 UTC` | `08:00 to 11:00 EST`.
  - **London Fix / Close Window:** `8:30 PM to 10:00 PM IST` (`15:00 to 16:30 UTC`) - Watch for intraday profit-taking reversals; avoid initiating fresh trend-continuation scalps right into the London Fix.

## 2. Central Bank Rate Differential & Sovereign Yield Spread Matrix

In Forex, you are always trading two currencies simultaneously. Pair the **fundamentally strongest currency** against the **fundamentally weakest**:

- **Central Bank Policy Divergence:** Compare current policy stances and CME FedWatch / OIS rate-cut or rate-hike probabilities across the **Federal Reserve (FOMC)**, **European Central Bank (ECB)**, **Bank of England (BoE)**, **Bank of Japan (BoJ)**, and **Reserve Bank of Australia (RBA)**.
- **2-Year & 10-Year Sovereign Bond Yield Spreads:**
  - `EUR/USD` tracks the **German 2Y/10Y Bund Yield minus US 2Y/10Y Treasury Yield** spread.
  - `USD/JPY` tracks the **US 10Y Treasury Yield minus Japan 10Y JGB Yield** spread (high sensitivity to US yield spikes and BoJ intervention warnings above key psychological levels).

## 3. Gold (`XAU/USD`) Real-Yield & Safe-Haven Matrix

Gold does not pay a coupon, so its primary institutional macro driver is the **US 10-Year Real Yield (10Y TIPS)** alongside the **US Dollar Index (`DXY`)**:

- **Bearish Headwind for Gold:** Rising `DXY` + Rising US 10Y Real Yields (`TIPS`).
- **High-Conviction Bullish Tailwind for Gold:** Falling `DXY` + Falling US 10Y Real Yields (`TIPS`).
- **Geopolitical / Central Bank Accumulation Regime (DXY + Gold Rising Together):** When Gold rises even while `DXY` and nominal yields rise, flag a **Sovereign / Geopolitical Safe-Haven Accumulation Regime**—never blindly short Gold strictly on DXY strength without a confirmed 1H/4H structural breakdown.

## 4. CFTC COT Whale Check & Prop-Firm Risk Rules

- Always check the latest Friday **CFTC Commitments of Traders (COT)** report for Non-Commercial net positioning extremes.
- Output position sizing in **Standard (`1.00`), Mini (`0.10`), and Micro (`0.01`) lots**, verifying that spread widens during session rollover (`2:30 AM - 3:30 AM IST` / `17:00 EST`) will not prematurely stop out the trade.
