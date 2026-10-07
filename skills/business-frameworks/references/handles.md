# Handles — Business Frameworks 1.0

Copied from `GET /catalogue` on 2026-10-07. The live catalogue is the authority on handles, token counts and prices; if this file and the catalogue differ, the catalogue is right. All handles are prefixed `business-frameworks/` and carry `@1.0`.

| Path | Title | Layer | Tokens | Price | Apply route |
|---|---|---|---|---|---|
| `equation` | The equation V = CF/(r − g) | 0 | 240 | free |  |
| `value` | Value (V) | 1 | 210 | free |  |
| `cash-flow` | Cash flow (CF) | 1 | 210 | free |  |
| `risk` | Risk (r) | 1 | 210 | free |  |
| `growth` | Growth (g) | 1 | 210 | free |  |
| `value/15s` | Long-term shareholder value in fifteen seconds | 1 | 100 | free |  |
| `value/why` | Why value is the objective, and what moves it | 2 | 350 | $0.02 |  |
| `value/band/sub-1m` | Value below $1M: the owner is the business | 2 | 300 | $0.03 |  |
| `value/band/5-25m` | Value $5–25M: the business becomes an asset | 2 | 250 | $0.03 |  |
| `value/band/25-50m` | Value $25–50M: value is position | 2 | 250 | $0.03 |  |
| `cash-flow/why` | Why profit is not cash, and where the cash goes | 2 | 400 | $0.02 |  |
| `cash-flow/band/sub-1m` | Cash flow below $1M: pay the owner first | 2 | 250 | $0.03 |  |
| `cash-flow/band/1-5m` | Cash flow $1–5M: the cash cycle rules | 2 | 350 | $0.03 |  |
| `cash-flow/band/5-25m` | Cash flow $5–25M: capital allocation | 2 | 250 | $0.03 |  |
| `cash-flow/pro-forma` | How the forward view is built | 2 | 350 | $0.03 |  |
| `risk/why` | Why r is a price, and how it is set | 2 | 500 | $0.02 |  |
| `risk/band/sub-5m` | Risk below $5M: the chance of survival | 2 | 350 | $0.03 |  |
| `risk/band/5-50m` | Risk from $5M up: market-referenced r | 2 | 250 | $0.03 |  |
| `growth/why` | Why growth is conditional, and where its ceiling is | 2 | 400 | $0.02 |  |
| `growth/forecast` | From a revenue forecast to a g you can defend | 2 | 350 | $0.03 |  |
| `growth/self-financeable` | The growth the business can pay for itself | 2 | 350 | $0.03 |  |
| `growth/band/25-50m` | Growth $25–50M: a scope decision | 2 | 300 | $0.03 |  |
| `value/decide/reinvest-or-distribute` | Reinvest or distribute | 3 | 220 | $0.05 | `POST /apply/value/decide/reinvest-or-distribute` $0.05 |
| `value/decide/build-or-run-for-cash` | Build for transfer or run for cash | 3 | 220 | $0.05 | `POST /apply/value/decide/build-or-run-for-cash` $0.05 |
| `cash-flow/decide/cash-cycle` | Manage the cash cycle | 3 | 220 | $0.05 | `POST /apply/cash-flow/decide/cash-cycle` $0.05 |
| `cash-flow/decide/runway` | Keep the runway | 3 | 220 | $0.05 | `POST /apply/cash-flow/decide/runway` $0.05 |
| `cash-flow/decide/owner-pay` | Pay the owner first | 3 | 150 | $0.05 | `POST /apply/cash-flow/decide/owner-pay` $0.05 |
| `risk/decide/hurdle` | Set the hurdle rate | 3 | 220 | $0.05 | `POST /apply/risk/decide/hurdle` $0.05 |
| `risk/decide/concentration` | Limit concentration | 3 | 220 | $0.05 | `POST /apply/risk/decide/concentration` $0.05 |
| `growth/decide/pace` | Set the pace of growth | 3 | 220 | $0.05 | `POST /apply/growth/decide/pace` $0.05 |
| `growth/decide/price` | Set the price | 3 | 220 | $0.05 | `POST /apply/growth/decide/price` $0.05 |
| `growth/decide/adjacency` | Approve or refuse an adjacency | 3 | 220 | $0.05 | `POST /apply/growth/decide/adjacency` $0.05 |

Node text: `GET /node/<path>`. Apply schema and example input (free): `GET /apply/<path>`.
