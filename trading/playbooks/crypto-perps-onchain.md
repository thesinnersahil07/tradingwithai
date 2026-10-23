# Playbook C: Crypto, Bitcoin, Altcoins & Perpetual Futures

## When to Activate

Activate this playbook whenever the target asset is Bitcoin (`BTC`), Ethereum (`ETH`), Solana (`SOL`), any Layer-1/Layer-2/DeFi/Meme altcoin, or a crypto spot/perpetual futures contract.

## 1. US Spot ETF Institutional Flow Tracker

Institutional spot demand is anchored by US Spot Bitcoin and Ethereum ETFs:

- **Daily Net Inflow / Outflow Check:** Check the latest daily net flow figures across **BlackRock (`IBIT` / `ETHA`)**, **Fidelity (`FBTC` / `FETH`)**, **Ark (`ARKB`)**, **Bitwise (`BITB`)**, and **Grayscale (`GBTC` / `ETHE`)**.
- **Spot vs. Perp Alignment:**
  - *Spot ETF Net Inflows + Negative/Neutral Perp Funding:* High-conviction institutional spot accumulation. Favor Long setups on pullbacks to VWAP or 1H/4H Order Blocks.
  - *Multi-Day Spot ETF Net Outflows + High Positive Perp Funding:* Retail is buying leveraged tops while institutions redeem spot shares. High risk of a sharp liquidation cascade; block aggressive long breakouts.
- **US Equity Open Volatility Window (`7:00 PM to 9:30 PM IST` / `09:30 to 12:00 EST`):** Crypto experiences its highest daily volume and institutional ETF hedging/creation flows during the first 2.5 hours of the New York stock market open. Expect two-way stop hunts in the first 30 minutes of the NY equities bell before the real directional trend establishes.

## 2. Capital Rotation & Dominance Matrix (`BTC.D`, `USDT.D`, `ETH/BTC`)

Never trade an altcoin in isolation. Classify the crypto capital rotation regime first:

| BTC Price Action | BTC Dominance (`BTC.D`) | USDT Dominance (`USDT.D`) | Regime Verdict & Execution Rule |
| :--- | :--- | :--- | :--- |
| **Rising** | **Rising** | Falling | **Bitcoin Season:** Institutional capital is concentrating in BTC. Focus longs strictly on BTC; altcoins will underperform on a risk-adjusted basis. |
| **Rising or Stable** | **Falling** | Falling | **Altcoin Season / Beta Rotation:** Profits are rotating from BTC into high-beta Layer-1s and sector leaders (`ETH/BTC` rising). Approve high-conviction Altcoin longs. |
| **Falling** | **Rising** | **Rising** | **Altcoin Capitulation / Risk-Off:** Liquidity is fleeing altcoins back into BTC and stablecoins. Strictly block Altcoin longs; favor cash or short setups. |
| **Falling** | Falling | **Breaking Out Upward** | **Market-Wide Liquidation Flush:** Broad risk-off move across all crypto. Enforce flat protocol or short bias until `USDT.D` hits resistance. |

## 3. Liquidation Heatmap & Funding Rate Squeeze Filter

Crypto markets trade 24/7 with up to 50x-100x retail leverage, making **Liquidation Pools** the primary fuel for intraday price moves:

- **Annualized / 8h Funding Rate Thresholds:**
  - *Neutral / Healthy Baseline:* `+0.005% to +0.010%` per 8 hours.
  - *Overcrowded Retail Longs (`> +0.030%` per 8h):* Retail is paying extreme premium to stay long. Market makers have a strong incentive to drive price down into the nearest **Long Liquidation Cluster** before any sustained move higher.
  - *Crowded Shorts (`< 0.000%` negative funding):* Perp traders are heavily shorting below spot price. If spot CVD and ETF flows remain constructive, look for a **Short Squeeze displacement rally**.
- **Wick-Proof Stop Placement:** Always place hard Stop-Losses outside the 7-day high-leverage liquidation cluster (using **Isolated Margin** or spot execution) so a sudden 3-5% liquidation wick does not liquidate the account before price reverses.

## 4. On-Chain Whale Netflows & 7-Day Cliff Token Unlock Radar

- **Exchange Netflows:** Large whale inflows of `BTC/ETH/Altcoins` onto centralized exchanges signal imminent spot selling pressure; large outflows to cold custody together with stablecoin (`USDT/USDC`) inflows to exchanges signal buying power.
- **Mandatory 7-Day Cliff Token Unlock Check (For All Altcoins):**
  - Before approving any Swing Long on an altcoin, search `"<TOKEN> token unlock schedule next 7 days" Tokenomist Dropstab`.
  - If a cliff unlock exceeding **2% to 5% of circulating supply** (allocated to VCs, team, or early investors) occurs within the next 7 days, **VETO Swing Longs** and warn of pre-unlock front-running sell pressure.
