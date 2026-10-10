# Handles — Business Frameworks, document version 1.2

Copied from `GET /catalogue` of endpoint build 2026.10.10 on 2026-10-10. The live catalogue is the authority on handles, token counts, prices and bundles; if this file and the catalogue differ, the catalogue is right. All handles are prefixed `business-frameworks/` and carry `@1.2`; the 32 marked 1.0 also answer at `@1.0` with their 1.0 text. Tokens are the full variant, with the terse variant in parentheses.

| Path | Title | Layer | Tokens (terse) | Price | Apply route | Versions |
|---|---|---|---|---|---|---|
| `equation` | The equation V = CF/(r − g) | 0 | 275 (44) | free |  | 1.2, 1.0 |
| `value` | Value (V) | 1 | 241 (72) | free |  | 1.2, 1.0 |
| `cash-flow` | Cash flow (CF) | 1 | 251 (51) | free |  | 1.2, 1.0 |
| `risk` | Risk (r) | 1 | 275 (91) | free |  | 1.2, 1.0 |
| `growth` | Growth (g) | 1 | 229 (94) | free |  | 1.2, 1.0 |
| `value/15s` | Long-term shareholder value in fifteen seconds | 1 | 83 (83) | free |  | 1.2, 1.0 |
| `value/why` | Why value is the objective, and what moves it | 2 | 290 (89) | USD 0.02 |  | 1.2, 1.0 |
| `value/band/sub-1m` | Value below $1M: the owner is the business | 2 | 292 (106) | USD 0.03 |  | 1.2, 1.0 |
| `value/band/5-25m` | Value $5–25M: the business becomes an asset | 2 | 197 (114) | USD 0.03 |  | 1.2, 1.0 |
| `value/band/25-50m` | Value $25–50M: value is position | 2 | 243 (44) | USD 0.03 |  | 1.2, 1.0 |
| `cash-flow/why` | Why profit is not cash, and where the cash goes | 2 | 318 (65) | USD 0.02 |  | 1.2, 1.0 |
| `cash-flow/band/sub-1m` | Cash flow below $1M: pay the owner first | 2 | 202 (63) | USD 0.03 |  | 1.2, 1.0 |
| `cash-flow/band/1-5m` | Cash flow $1–5M: the cash cycle rules | 2 | 272 (143) | USD 0.03 |  | 1.2, 1.0 |
| `cash-flow/band/5-25m` | Cash flow $5–25M: capital allocation | 2 | 194 (71) | USD 0.03 |  | 1.2, 1.0 |
| `cash-flow/pro-forma` | How the forward view is built | 2 | 278 (201) | USD 0.03 |  | 1.2, 1.0 |
| `risk/why` | Why r is a price, and how it is set | 2 | 494 (106) | USD 0.02 |  | 1.2, 1.0 |
| `risk/band/sub-5m` | Risk below $5M: the chance of survival | 2 | 290 (101) | USD 0.03 |  | 1.2, 1.0 |
| `risk/band/5-50m` | Risk from $5M up: market-referenced r | 2 | 193 (78) | USD 0.03 |  | 1.2, 1.0 |
| `growth/why` | Why growth is conditional, and where its ceiling is | 2 | 298 (89) | USD 0.02 |  | 1.2, 1.0 |
| `growth/forecast` | From a revenue forecast to a g you can defend | 2 | 232 (168) | USD 0.03 |  | 1.2, 1.0 |
| `growth/self-financeable` | The growth the business can pay for itself | 2 | 358 (131) | USD 0.03 |  | 1.2, 1.0 |
| `growth/band/25-50m` | Growth $25–50M: a scope decision | 2 | 285 (81) | USD 0.03 |  | 1.2, 1.0 |
| `value/decide/reinvest-or-distribute` | Reinvest or distribute | 3 | 258 (200) | USD 0.05 | `POST /apply/value/decide/reinvest-or-distribute` USD 0.05 | 1.2, 1.0 |
| `value/decide/build-or-run-for-cash` | Build for transfer or run for cash | 3 | 165 (165) | USD 0.05 | `POST /apply/value/decide/build-or-run-for-cash` USD 0.05 | 1.2, 1.0 |
| `cash-flow/decide/cash-cycle` | Manage the cash cycle | 3 | 160 (160) | USD 0.05 | `POST /apply/cash-flow/decide/cash-cycle` USD 0.05 | 1.2, 1.0 |
| `cash-flow/decide/runway` | Keep the runway | 3 | 317 (195) | USD 0.05 | `POST /apply/cash-flow/decide/runway` USD 0.05 | 1.2, 1.0 |
| `cash-flow/decide/owner-pay` | Pay the owner first | 3 | 98 (98) | USD 0.05 | `POST /apply/cash-flow/decide/owner-pay` USD 0.05 | 1.2, 1.0 |
| `risk/decide/hurdle` | Set the hurdle rate | 3 | 170 (170) | USD 0.05 | `POST /apply/risk/decide/hurdle` USD 0.05 | 1.2, 1.0 |
| `risk/decide/concentration` | Limit concentration | 3 | 137 (137) | USD 0.05 | `POST /apply/risk/decide/concentration` USD 0.05 | 1.2, 1.0 |
| `growth/decide/pace` | Set the pace of growth | 3 | 146 (146) | USD 0.05 | `POST /apply/growth/decide/pace` USD 0.05 | 1.2, 1.0 |
| `growth/decide/price` | Set the price | 3 | 196 (196) | USD 0.05 | `POST /apply/growth/decide/price` USD 0.05 | 1.2, 1.0 |
| `growth/decide/adjacency` | Approve or refuse an adjacency | 3 | 257 (257) | USD 0.05 | `POST /apply/growth/decide/adjacency` USD 0.05 | 1.2, 1.0 |
| `decision` | Decision rules: wrong as rarely as possible for the effort | 1 | 210 (91) | free |  | 1.2 |
| `decision/parameters` | Parameters: the defaults, and the ladder for adjusting them | 2 | 265 (103) | free |  | 1.2 |
| `decision/extension` | Extension: outside the bands the rules were written for | 2 | 233 (87) | free |  | 1.2 |
| `decision/effort` | Effort: match the analysis to the stakes | 2 | 255 (101) | free |  | 1.2 |
| `market` | Market (the chain): rent accrues at the node that binds | 1 | 195 (83) | free |  | 1.2 |
| `market/why` | Why the constraint is read before the price | 2 | 372 (147) | USD 0.02 |  | 1.2 |
| `market/map` | Map the chain as markets, not companies | 2 | 426 (122) | USD 0.03 |  | 1.2 |
| `market/edges` | Draw the edges: weights, lags, pull and constraint | 2 | 357 (132) | USD 0.03 |  | 1.2 |
| `market/structure` | Score the structure and read the sellers' propensity | 2 | 344 (135) | USD 0.03 |  | 1.2 |
| `market/balance` | Balance supply against demand and find the crossing | 2 | 348 (128) | USD 0.03 |  | 1.2 |
| `market/buyers` | Sort the buyers into four tiers | 2 | 320 (140) | USD 0.03 |  | 1.2 |
| `market/shocks` | Test the node against four shocks | 2 | 333 (124) | USD 0.03 |  | 1.2 |
| `market/band/sub-1m` | Market below $1M: a buyer at the end of a chain | 2 | 303 (125) | USD 0.03 |  | 1.2 |
| `market/band/1-5m` | Market $1–5M: the customer node's verdict is the ceiling | 2 | 298 (127) | USD 0.03 |  | 1.2 |
| `market/band/5-25m` | Market $5–25M: the node's four quantities are yours | 2 | 310 (133) | USD 0.03 |  | 1.2 |
| `market/band/25-50m` | Market $25–50M: possibly the binding node of a regional chain | 2 | 310 (104) | USD 0.03 |  | 1.2 |
| `market/pattern/layered-input` | Pattern: an input at many layers is not a branch | 2 | 272 (115) | USD 0.03 |  | 1.2 |
| `market/pattern/shared-name` | Pattern: two bases under one name are two chains | 2 | 239 (84) | USD 0.03 |  | 1.2 |
| `market/pattern/relieved-capacity` | Pattern: relieved capacity is the small firm's window | 2 | 273 (110) | USD 0.03 |  | 1.2 |
| `market/pattern/shared-upstream` | Pattern: a shared upstream node enters once | 2 | 253 (104) | USD 0.03 |  | 1.2 |
| `market/pattern/split-test` | Pattern: the buyer decides a split | 2 | 279 (106) | USD 0.03 |  | 1.2 |
| `market/pattern/binding-shift` | Pattern: a change moves the binding node | 2 | 303 (98) | USD 0.03 |  | 1.2 |
| `market/decide/verdict` | Read a node's verdict | 3 | 234 (167) | USD 0.05 | `POST /apply/market/decide/verdict` USD 0.05 | 1.2 |
| `market/decide/pricing-power` | Score pricing power | 3 | 291 (228) | USD 0.05 | `POST /apply/market/decide/pricing-power` USD 0.05 | 1.2 |
| `market/decide/binding-node` | Find the binding node | 3 | 256 (199) | USD 0.05 | `POST /apply/market/decide/binding-node` USD 0.05 | 1.2 |
| `market/decide/rent` | Price the rent over the horizon | 3 | 186 (122) | USD 0.05 | `POST /apply/market/decide/rent` USD 0.05 | 1.2 |
| `market/decide/shock` | Transfer a shock to your seat | 3 | 298 (228) | USD 0.05 | `POST /apply/market/decide/shock` USD 0.05 | 1.2 |

## Bundles

A bundle is quoted free at `POST /resolve` and bought at `GET /bundle/<id>` (or `/bundle/<id>/band/<slug>` with the scale band for the business's revenue, USD 0.03 more). The price is the sum of the nodes' catalogue prices; the central node is delivered full, the rest terse.

| Bundle | Kind | Task | Nodes | Price |
|---|---|---|---|---|
| `decide/adjacency` | decision | Approve or refuse a move outside the core business | `growth/decide/adjacency` (full), `growth/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/build-or-run-for-cash` | decision | Decide whether to build the business to be sold or run it for income | `value/decide/build-or-run-for-cash` (full), `value/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/cash-cycle` | decision | Shorten the time cash is tied up between paying and being paid | `cash-flow/decide/cash-cycle` (full), `cash-flow/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/concentration` | decision | Decide which dependencies on one customer, one supplier or the owner are risks to act on | `risk/decide/concentration` (full), `risk/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/hurdle` | decision | Set the rate of return an investment in this business has to beat | `risk/decide/hurdle` (full), `risk/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/owner-pay` | decision | Test whether the business makes money after the owner is paid a market wage | `cash-flow/decide/owner-pay` (full), `cash-flow/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/pace` | decision | Test whether planned growth pays for itself and whether outside money is worth taking | `growth/decide/pace` (full), `growth/why` (terse) | USD 0.07 |
| `decide/price` | decision | Set the price by segment between what the customer will pay and what one more unit costs | `growth/decide/price` (full), `growth/why` (terse) | USD 0.07 |
| `decide/reinvest-or-distribute` | decision | Decide what to fund from the cash in hand and what to pay out | `value/decide/reinvest-or-distribute` (full), `value/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `decide/runway` | decision | Find where the cash forecast breaks and what to cut or defer first | `cash-flow/decide/runway` (full), `cash-flow/why` (terse) | USD 0.07 (USD 0.10 with a band) |
| `market/position` | market | Place your business on the chain it sells into and buys from, and read what its seat means | `market/map` (full), `market/why` (terse) | USD 0.05 (USD 0.08 with a band) |
| `market/binding` | market | Find the node that binds your chain and the lag by which its constraint reaches you | `market/decide/binding-node` (full), `market/edges` (terse) | USD 0.08 (USD 0.11 with a band) |
| `market/pricing-power-horizon` | market | Price what your pricing power is worth over the horizon: the rent for the durability years | `market/decide/rent` (full), `market/decide/pricing-power` (terse), `market/balance` (terse) | USD 0.13 (USD 0.16 with a band) |
| `market/shocks-reaching-me` | market | Find which shocks reach your business, by what path and with what lag | `market/decide/shock` (full), `market/shocks` (terse), `market/edges` (terse) | USD 0.11 (USD 0.14 with a band) |
| `market/buyer-tier` | market | Sort your customers and your binding node's buyers into the four tiers and learn what transfers under stress | `market/buyers` (full), `market/decide/shock` (terse) | USD 0.08 (USD 0.11 with a band) |
| `market/verdict` | market | Read a node's verdict — binding, transient, pass-through or open — from its constraint, never from its price | `market/decide/verdict` (full), `market/balance` (terse), `market/structure` (terse), `market/why` (terse) | USD 0.13 |
| `cross/value-given-chain-position` | cross | Value the business given where it sits in its chain: a price-taker's margin, or rent for the durability years | `value/why` (full), `market/decide/rent` (terse), `market/why` (terse) | USD 0.09 (USD 0.12 with a band) |
| `cross/growth-given-binding-node` | cross | Set the pace of growth given the node that binds your chain: the self-financeable rate against the allocation you can get | `growth/decide/pace` (full), `market/decide/binding-node` (terse), `growth/self-financeable` (terse) | USD 0.13 (USD 0.16 with a band) |
| `cross/price-given-pricing-power` | cross | Set your price given your node's pricing power: the customer's willingness to pay, bounded by what the node lets you hold | `growth/decide/price` (full), `market/decide/pricing-power` (terse) | USD 0.10 (USD 0.13 with a band) |
| `cross/runway-given-shocks` | cross | Find where the cash forecast breaks when the shocks that reach your chain are written into the bad case | `cash-flow/decide/runway` (full), `market/decide/shock` (terse) | USD 0.10 (USD 0.13 with a band) |
