# Handles — Business Frameworks, document version 1.6.1

Copied from `GET /catalogue` of endpoint build 2026.11.18 on 2026-11-17 (handles, tokens, prices and versions unchanged at endpoint build 2026.11.19). The live catalogue is the authority on handles, token counts, prices and bundles; if this file and the catalogue differ, the catalogue is right. All handles are prefixed `business-frameworks/` and carry `@1.6.1`; the 154 nodes of 1.6 also answer at `@1.6`, the 84 of 1.5 at `@1.5`, the 67 of 1.4 at `@1.4`, the 59 of 1.3 at `@1.3` and `@1.2`, each with that version's text, and the 32 marked 1.0 at `@1.0` as well. Fifteen of the 62 decisions have an apply route; the other 47, and the 14 methods written in the decision shape, are served as nodes only.

| Path | Title | Layer | Tokens (terse) | Price | Apply route | Versions |
|---|---|---|---|---|---|---|
| `equation` | The equation V = CF/(r − g) | 0 | 325 (71) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value` | Value (V) | 1 | 241 (72) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow` | Cash flow (CF) | 1 | 254 (51) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk` | Risk (r) | 1 | 275 (91) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth` | Growth (g) | 1 | 229 (94) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/15s` | Long-term shareholder value in fifteen seconds | 1 | 83 (83) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/why` | Why value is the objective, and what moves it | 2 | 290 (89) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/band/sub-1m` | Value below $1M: the owner is the business | 2 | 292 (106) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/band/5-25m` | Value $5–25M: the business becomes an asset | 2 | 405 (114) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/band/25-50m` | Value $25–50M: value is position | 2 | 243 (44) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/why` | Why profit is not cash, and where the cash goes | 2 | 353 (65) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/band/sub-1m` | Cash flow below $1M: pay the owner first | 2 | 202 (63) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/band/1-5m` | Cash flow $1–5M: the cash cycle rules | 2 | 272 (143) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/band/5-25m` | Cash flow $5–25M: capital allocation | 2 | 194 (71) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/pro-forma` | How the forward view is built | 2 | 553 (242) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk/why` | Why r is a price, and how it is set | 2 | 554 (106) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk/band/sub-5m` | Risk below $5M: the chance of survival | 2 | 423 (101) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk/band/5-50m` | Risk from $5M up: market-referenced r | 2 | 247 (78) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/why` | Why growth is conditional, and where its ceiling is | 2 | 338 (89) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/forecast` | From a revenue forecast to a g you can defend | 2 | 678 (231) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/self-financeable` | The growth the business can pay for itself | 2 | 358 (131) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/band/25-50m` | Growth $25–50M: a scope decision | 2 | 329 (81) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/decide/reinvest-or-distribute` | Reinvest or distribute | 3 | 619 (561) | USD 0.05 | `POST /apply/value/decide/reinvest-or-distribute` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `value/decide/build-or-run-for-cash` | Build for transfer or run for cash | 3 | 645 (645) | USD 0.05 | `POST /apply/value/decide/build-or-run-for-cash` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/decide/cash-cycle` | Manage the cash cycle | 3 | 463 (463) | USD 0.05 | `POST /apply/cash-flow/decide/cash-cycle` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/decide/runway` | Keep the runway | 3 | 382 (260) | USD 0.05 | `POST /apply/cash-flow/decide/runway` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `cash-flow/decide/owner-pay` | Pay the owner first | 3 | 98 (98) | USD 0.05 | `POST /apply/cash-flow/decide/owner-pay` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk/decide/hurdle` | Set the hurdle rate | 3 | 224 (224) | USD 0.05 | `POST /apply/risk/decide/hurdle` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `risk/decide/concentration` | Limit concentration | 3 | 517 (517) | USD 0.05 | `POST /apply/risk/decide/concentration` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/decide/pace` | Set the pace of growth | 3 | 448 (448) | USD 0.05 | `POST /apply/growth/decide/pace` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/decide/price` | Set the price | 3 | 705 (705) | USD 0.05 | `POST /apply/growth/decide/price` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `growth/decide/adjacency` | Approve or refuse an adjacency | 3 | 563 (563) | USD 0.05 | `POST /apply/growth/decide/adjacency` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2, 1.0 |
| `decision` | Decision rules: wrong as rarely as possible for the effort | 1 | 541 (119) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `decision/parameters` | Parameters: the defaults, and the ladder for adjusting them | 2 | 523 (103) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `decision/extension` | Extension: outside the bands the rules were written for | 2 | 233 (87) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `decision/effort` | Effort: match the analysis to the stakes | 2 | 520 (101) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market` | Market (the chain): rent accrues at the node that binds | 1 | 195 (83) | free |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/why` | Why the constraint is read before the price | 2 | 372 (147) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/map` | Map the chain as markets, not companies | 2 | 458 (122) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/edges` | Draw the edges: weights, lags, pull and constraint | 2 | 390 (132) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/structure` | Score the structure and read the sellers' propensity | 2 | 392 (183) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/balance` | Balance supply against demand and find the crossing | 2 | 348 (128) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/buyers` | Sort the buyers into four tiers | 2 | 346 (140) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/shocks` | Test the node against four shocks | 2 | 333 (124) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/band/sub-1m` | Market below $1M: a buyer at the end of a chain | 2 | 385 (125) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/band/1-5m` | Market $1–5M: the customer node's verdict is the ceiling | 2 | 341 (127) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/band/5-25m` | Market $5–25M: the node's four quantities are yours | 2 | 418 (154) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/band/25-50m` | Market $25–50M: possibly the binding node of a regional chain | 2 | 310 (104) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/layered-input` | Pattern: an input at many layers is not a branch | 2 | 272 (115) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/shared-name` | Pattern: two bases under one name are two chains | 2 | 239 (84) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/relieved-capacity` | Pattern: relieved capacity is the small firm's window | 2 | 273 (110) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/shared-upstream` | Pattern: a shared upstream node enters once | 2 | 253 (104) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/split-test` | Pattern: the buyer decides a split | 2 | 293 (106) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/pattern/binding-shift` | Pattern: a change moves the binding node | 2 | 350 (98) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/decide/verdict` | Read a node's verdict | 3 | 234 (167) | USD 0.05 | `POST /apply/market/decide/verdict` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/decide/pricing-power` | Score pricing power | 3 | 352 (243) | USD 0.05 | `POST /apply/market/decide/pricing-power` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/decide/binding-node` | Find the binding node | 3 | 256 (199) | USD 0.05 | `POST /apply/market/decide/binding-node` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/decide/rent` | Price the rent over the horizon | 3 | 186 (122) | USD 0.05 | `POST /apply/market/decide/rent` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `market/decide/shock` | Transfer a shock to your seat | 3 | 325 (228) | USD 0.05 | `POST /apply/market/decide/shock` USD 0.05 | 1.6.1, 1.6, 1.5, 1.4, 1.3, 1.2 |
| `ethics` | Ethics inside the equation: a floor first, then the three terms | 1 | 276 (128) | free |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/feasible` | Feasible first: strike, draw the line, seek the middle way, then rank | 2 | 985 (188) | free |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/why` | Why conduct belongs inside the equation, and what the link is not | 2 | 273 (88) | USD 0.02 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/risk` | Conduct and r: acceptable risk, consent and the tail | 2 | 408 (87) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/cash-flow` | Conduct and CF: trust, disclosure and conflicts of interest | 2 | 265 (147) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/growth` | Conduct and g: stewardship, the frame in use and harm outside it | 2 | 245 (91) | USD 0.03 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/decide/safety-concern` | Decide: a safety objection against cost or schedule | 3 | 230 (230) | USD 0.05 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `ethics/decide/disclose` | Decide: telling the people who rely on a fact | 3 | 418 (418) | USD 0.05 |  | 1.6.1, 1.6, 1.5, 1.4 |
| `worker` | The worker inside the equation: pride and stake through the three terms | 1 | 341 (91) | free |  | 1.6.1, 1.6, 1.5 |
| `worker/read-the-job` | Read the job: three moves before deciding anything about a role | 2 | 794 (94) | free |  | 1.6.1, 1.6, 1.5 |
| `worker/why` | Why the worker is inside the equation, and what the link is not | 2 | 544 (94) | USD 0.02 |  | 1.6.1, 1.6, 1.5 |
| `worker/cash-flow` | The worker and CF: the effort decision — what is counted, who sees, and the ratchet | 2 | 437 (89) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `worker/risk` | The worker and r: the membership decision — fear, the promise ledger, and what ends turnover | 2 | 581 (90) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `worker/growth` | The worker and g: the pipeline, hidden improvements, and automation as applied | 2 | 460 (95) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `worker/decide/design-the-job` | Decide: redraw a role so that its holder can see what they finish | 3 | 491 (491) | USD 0.05 |  | 1.6.1, 1.6, 1.5 |
| `worker/decide/measure` | Decide: what to count, who sees the count, and how a standard moves | 3 | 614 (614) | USD 0.05 |  | 1.6.1, 1.6, 1.5 |
| `worker/decide/share-the-gain` | Decide: a stake that works — share, say and sight, sized to the headcount | 3 | 492 (492) | USD 0.05 |  | 1.6.1, 1.6, 1.5 |
| `quality` | Quality inside the equation: the customer satisfied, produced where someone cares | 1 | 294 (91) | free |  | 1.6.1, 1.6, 1.5 |
| `quality/see-the-work` | See the work: five observations and the traps that drain care | 2 | 608 (95) | free |  | 1.6.1, 1.6, 1.5 |
| `quality/why` | Why quality is inside the equation, and what the link is not | 2 | 379 (93) | USD 0.02 |  | 1.6.1, 1.6, 1.5 |
| `quality/cash-flow` | Quality and CF: the customer who returns, the rework that does not show, the count that replaces the result | 2 | 412 (91) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `quality/risk` | Quality and r: the defect tail, the standard held by the responsible person, and the leading signals | 2 | 372 (89) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `quality/growth` | Quality and g: a standard that rises when beaten, and the stuck point where new quality enters | 2 | 303 (95) | USD 0.03 |  | 1.6.1, 1.6, 1.5 |
| `quality/decide/stop-or-ship` | Decide: a known defect meets a date | 3 | 299 (299) | USD 0.05 |  | 1.6.1, 1.6, 1.5 |
| `quality/decide/standard` | Decide: who sets the standard, who judges against it, and how it moves | 3 | 318 (318) | USD 0.05 |  | 1.6.1, 1.6, 1.5 |
| `communicate` | Communicate: what a message carries, and what it loses | 1 | 132 (48) | free |  | 1.6.1, 1.6 |
| `communicate/advise` | Advise: an answer as sure as its analysis | 3 | 337 (337) | USD 0.05 |  | 1.6.1, 1.6 |
| `communicate/decide/tell-a-group` | Decide: telling a group about a change | 3 | 279 (279) | USD 0.05 |  | 1.6.1, 1.6 |
| `communicate/decide/the-ask` | Decide: asking a decider for something | 3 | 307 (307) | USD 0.05 |  | 1.6.1, 1.6 |
| `customer` | The customer inside the equation: chosen, won, priced and kept | 1 | 172 (96) | free |  | 1.6.1, 1.6 |
| `customer/cash-flow` | The customer and CF: the customer who comes back | 2 | 174 (51) | USD 0.03 |  | 1.6.1, 1.6 |
| `customer/decide/acquire` | Decide: where the next customers come from | 3 | 257 (257) | USD 0.05 |  | 1.6.1, 1.6 |
| `customer/decide/retain` | Decide: whom to keep, and how | 3 | 249 (249) | USD 0.05 |  | 1.6.1, 1.6 |
| `customer/decide/select` | Decide: which customers to serve | 3 | 254 (254) | USD 0.05 |  | 1.6.1, 1.6 |
| `customer/growth` | The customer and g: what a capable customer tells a supplier | 2 | 130 (48) | USD 0.03 |  | 1.6.1, 1.6 |
| `customer/risk` | The customer and r: the customer who stops buying | 2 | 147 (38) | USD 0.03 |  | 1.6.1, 1.6 |
| `customer/why` | Why the customer is inside the equation: the need the business serves | 2 | 154 (46) | USD 0.02 |  | 1.6.1, 1.6 |
| `decision/ask` | Decide: the question before the analysis | 3 | 234 (234) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/change` | Decide: how to carry a change | 3 | 335 (335) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/change/no-cash` | A change made without new money | 3 | 307 (307) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/change/score` | Scoring a change before it starts | 3 | 322 (322) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/continue-or-stop` | Decide: continue or stop | 3 | 249 (249) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/effort/initiatives` | How many changes to carry at once | 3 | 240 (240) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/effort/test` | A test that can be believed | 3 | 284 (284) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/negotiate` | Decide: a negotiation | 3 | 312 (312) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/predict` | Decide: acting on a prediction | 3 | 449 (449) | USD 0.05 |  | 1.6.1, 1.6 |
| `decision/who-decides` | Decide: who decides | 3 | 264 (264) | USD 0.05 |  | 1.6.1, 1.6 |
| `ethics/feasible/pricing-law-reference` | Reference: United States pricing law, initial guidance | 2 | 585 (92) | USD 0.03 |  | 1.6.1, 1.6 |
| `growth/decide/adjacency/trade-off` | An adjacent move and the trade-offs it meets | 3 | 221 (221) | USD 0.05 |  | 1.6.1, 1.6 |
| `growth/decide/pace/hosted-venture` | A venture hosted inside an existing business | 3 | 349 (349) | USD 0.05 |  | 1.6.1, 1.6 |
| `growth/decide/pace/innovation-hurdle` | How a new venture is judged and funded | 3 | 286 (286) | USD 0.05 |  | 1.6.1, 1.6 |
| `growth/decide/price/critical-mass` | Pricing where each user makes the product worth more | 3 | 409 (409) | USD 0.05 |  | 1.6.1, 1.6 |
| `growth/decide/price/measure-wtp` | Measuring what buyers will pay | 3 | 252 (252) | USD 0.05 |  | 1.6.1, 1.6 |
| `growth/decide/price/structure` | The unit and structure of a price | 3 | 305 (305) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate` | Operate: the business run on a system | 1 | 286 (95) | free |  | 1.6.1, 1.6 |
| `operate/daily` | The daily loop at the work | 2 | 414 (110) | USD 0.03 |  | 1.6.1, 1.6 |
| `operate/decide/first-90-days` | Decide: the first months after a change of owner | 3 | 277 (277) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/decide/improvement-staffing` | Decide: who does the improving | 3 | 338 (338) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/decide/team-or-group` | Decide: a team or a working group | 3 | 269 (269) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/metrics` | The few measures the business is run by | 3 | 268 (268) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/office` | Where people sit, and who talks to whom | 3 | 303 (303) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/project` | How a project is organized | 3 | 288 (288) | USD 0.05 |  | 1.6.1, 1.6 |
| `operate/why` | Why a business runs an operating system | 2 | 539 (122) | USD 0.02 |  | 1.6.1, 1.6 |
| `owner` | The owner inside the equation: the part every other part reads | 1 | 145 (53) | free |  | 1.6.1, 1.6 |
| `owner/decide/delegate` | Decide: what the owner hands over | 3 | 329 (329) | USD 0.05 |  | 1.6.1, 1.6 |
| `owner/decide/under-pressure` | Decide: the owner under pressure | 3 | 314 (314) | USD 0.05 |  | 1.6.1, 1.6 |
| `owner/see-your-week` | See your week: one week of the owner's hours | 2 | 271 (50) | USD 0.03 |  | 1.6.1, 1.6 |
| `owner/why` | Why the owner is inside the equation | 2 | 269 (108) | USD 0.02 |  | 1.6.1, 1.6 |
| `risk/decide/concentration/counterparty` | The terms that limit what one counterparty can cost | 3 | 298 (298) | USD 0.05 |  | 1.6.1, 1.6 |
| `risk/decide/concentration/key-person` | Dependence on one person | 3 | 342 (342) | USD 0.05 |  | 1.6.1, 1.6 |
| `risk/decide/premortem` | Decide: a commitment that cannot be undone | 3 | 380 (380) | USD 0.05 |  | 1.6.1, 1.6 |
| `risk/decide/substitute` | Decide: the substitute that could replace the business | 3 | 437 (437) | USD 0.05 |  | 1.6.1, 1.6 |
| `risk/decide/supply` | Decide: dependence on a supplier | 3 | 332 (332) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy` | Strategy: where the firm competes, how it differs, what it refuses | 1 | 192 (53) | free |  | 1.6.1, 1.6 |
| `strategy/decide/business-model` | Decide: whether a move needs a new business model | 3 | 312 (312) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/buy-a-rival` | Decide: buying a competitor | 3 | 300 (300) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/industry` | Decide: the field to compete in | 3 | 310 (310) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/integrate-or-contract` | Decide: make a stage or contract for it | 3 | 238 (238) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/new-market` | Decide: an offer for those who do not buy today | 3 | 302 (302) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/position` | Decide: the position | 3 | 354 (354) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/decide/position/principle` | The core of the strategy in one phrase | 3 | 309 (309) | USD 0.05 |  | 1.6.1, 1.6 |
| `strategy/vision` | Vision: the value that cannot be measured in cash flow | 2 | 269 (74) | USD 0.03 |  | 1.6.1, 1.6 |
| `strategy/why` | Why a difference lasts | 2 | 327 (66) | USD 0.02 |  | 1.6.1, 1.6 |
| `value/decide/buy-a-firm` | Decide: buying a going concern | 3 | 558 (558) | USD 0.05 |  | 1.6.1, 1.6 |
| `value/decide/buy-a-firm/diligence` | Diligence before a purchase | 3 | 449 (449) | USD 0.05 |  | 1.6.1, 1.6 |
| `value/decide/run-the-sale` | Decide: selling the firm | 3 | 427 (427) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/arrive` | Decide: a newcomer's first months | 3 | 250 (250) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/design-the-job/group` | A result that belongs to a group | 3 | 233 (233) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/hard-talk` | Decide: a hard conversation | 3 | 321 (321) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/learn` | Decide: how a skill is learned | 3 | 217 (217) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/measure/first-miss` | The written expectation and the first miss | 3 | 234 (234) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/select` | Decide: whom to hire | 3 | 232 (232) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/share-the-gain/key-person-stake` | A stake for one key person | 3 | 360 (360) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/share-the-gain/managers` | How managers are paid | 3 | 201 (201) | USD 0.05 |  | 1.6.1, 1.6 |
| `worker/decide/share-the-gain/seller-pay` | How sellers are paid | 3 | 242 (242) | USD 0.05 |  | 1.6.1, 1.6 |

## Bundles

A bundle is quoted free at `POST /resolve` and bought at `GET /bundle/<id>` (or `/bundle/<id>/band/<slug>` with the scale band for the business's revenue). Every bundle costs a flat USD 0.05, with or without its scale band (Card 50 ruling 3, 2026-10-20, amending R19); the central node is delivered full and the rest terse, on one settlement.

| Bundle | Kind | Task | Nodes | Price |
|---|---|---|---|---|
| `decide/adjacency` | decision | Approve or refuse a move outside the core business | `growth/decide/adjacency` (full), `growth/why` (terse) | USD 0.05 (the same with a band) |
| `decide/build-or-run-for-cash` | decision | Decide whether to build the business to be sold or run it for income | `value/decide/build-or-run-for-cash` (full), `value/why` (terse) | USD 0.05 (the same with a band) |
| `decide/cash-cycle` | decision | Shorten the time cash is tied up between paying and being paid | `cash-flow/decide/cash-cycle` (full), `cash-flow/why` (terse) | USD 0.05 (the same with a band) |
| `decide/concentration` | decision | Decide which dependencies on one customer, one supplier or the owner are risks to act on | `risk/decide/concentration` (full), `risk/why` (terse) | USD 0.05 (the same with a band) |
| `decide/hurdle` | decision | Set the rate of return an investment in this business has to beat | `risk/decide/hurdle` (full), `risk/why` (terse) | USD 0.05 (the same with a band) |
| `decide/owner-pay` | decision | Test whether the business makes money after the owner is paid a market wage | `cash-flow/decide/owner-pay` (full), `cash-flow/why` (terse) | USD 0.05 (the same with a band) |
| `decide/pace` | decision | Test whether planned growth pays for itself and whether outside money is worth taking | `growth/decide/pace` (full), `growth/why` (terse) | USD 0.05 (the same with a band) |
| `decide/price` | decision | Set the price by segment between what the customer will pay and what one more unit costs | `growth/decide/price` (full), `growth/why` (terse) | USD 0.05 (the same with a band) |
| `decide/reinvest-or-distribute` | decision | Decide what to fund from the cash in hand and what to pay out | `value/decide/reinvest-or-distribute` (full), `value/why` (terse) | USD 0.05 (the same with a band) |
| `decide/runway` | decision | Find where the cash forecast breaks and what to cut or defer first | `cash-flow/decide/runway` (full), `cash-flow/why` (terse) | USD 0.05 (the same with a band) |
| `market/position` | market | Place your business on the chain it sells into and buys from, and read what its seat means | `market/map` (full), `market/why` (terse) | USD 0.05 (the same with a band) |
| `market/binding` | market | Find the node that binds your chain and the lag by which its constraint reaches you | `market/decide/binding-node` (full), `market/edges` (terse) | USD 0.05 (the same with a band) |
| `market/pricing-power-horizon` | market | Price what your pricing power is worth over the horizon: the rent for the durability years | `market/decide/rent` (full), `market/decide/pricing-power` (terse), `market/balance` (terse) | USD 0.05 (the same with a band) |
| `market/shocks-reaching-me` | market | Find which shocks reach your business, by what path and with what lag | `market/decide/shock` (full), `market/shocks` (terse), `market/edges` (terse) | USD 0.05 (the same with a band) |
| `market/buyer-tier` | market | Sort your customers and your binding node's buyers into the four tiers and learn what transfers under stress | `market/buyers` (full), `market/decide/shock` (terse) | USD 0.05 (the same with a band) |
| `market/verdict` | market | Read a node's verdict — binding, transient, pass-through or open — from its constraint, never from its price | `market/decide/verdict` (full), `market/balance` (terse), `market/structure` (terse), `market/why` (terse) | USD 0.05 (the same with a band) |
| `cross/value-given-chain-position` | cross | Value the business given where it sits in its chain: a price-taker's margin, or rent for the durability years | `value/why` (full), `market/decide/rent` (terse), `market/why` (terse) | USD 0.05 (the same with a band) |
| `cross/growth-given-binding-node` | cross | Set the pace of growth given the node that binds your chain: the self-financeable rate against the allocation you can get | `growth/decide/pace` (full), `market/decide/binding-node` (terse), `growth/self-financeable` (terse) | USD 0.05 (the same with a band) |
| `cross/price-given-pricing-power` | cross | Set your price given your node's pricing power: the customer's willingness to pay, bounded by what the node lets you hold | `growth/decide/price` (full), `market/decide/pricing-power` (terse) | USD 0.05 (the same with a band) |
| `cross/runway-given-shocks` | cross | Find where the cash forecast breaks when the shocks that reach your chain are written into the bad case | `cash-flow/decide/runway` (full), `market/decide/shock` (terse) | USD 0.05 (the same with a band) |
