# The decisions — what each takes, what it returns

*Document version 1.6.1 (endpoint build 2026.11.19). Sixty-two decision nodes, each in the shape inputs / rule / action / check; fifteen of them are applied to the caller's own figures at `POST /apply/<path>` for the node's price (USD 0.05), and the other forty-seven are served as nodes only. From document version 1.6.1 each applied route computes the rule its node states: the six that 1.6 left on the 1.5 rule — `value/decide/reinvest-or-distribute`, `value/decide/build-or-run-for-cash`, `risk/decide/concentration`, `growth/decide/pace`, `growth/decide/price` and `growth/decide/adjacency` — were rebuilt in endpoint build 2026.11.18 and take the inputs listed below. The schema, an example and the names of the figures the rule returns are free at `GET /apply/<path>`; an unpaid POST answers 402 with `body_check`, so a body is found wrong before anything is paid. The rule is applied exactly as the node states it — no model sits between the inputs and the answer. Prices and handles are in the live catalogue; this page is for orientation.*

Ask narrow, pay per node; ask broad, get a quoted bundle at USD 0.05, stated before you pay. When the question gives figures for a decision, the applied route computes them; the answer reports its result and does not recompute it.

## The ten decisions of value, cash flow, risk and growth

*Units.* Fields ending _pct take a number of percent (13 means 13%, not 0.13). Fields ending _per_sales_dollar are fractions of a sales dollar (0.65 means 65 cents), and probabilities run from 0 to 1. Money is a plain number in one currency for the whole call; revenue_usd alone is in US dollars, because the scale bands are set in US dollars.

| Decision | Node | Takes (required; optional) | Returns |
|---|---|---|---|
| `risk/decide/hurdle` | Set the hurdle rate (224 tokens, terse 224) | `long_bond_yield_pct`, `asset_betas`; `market_premium_pct`, `personal_premium_pct`, `revenue_usd`, `plan_probability` | r for this business — its cost of capital, the discount rate — with the sub-$5M probability rule and the concentrated owner's stated premium applied. |
| `cash-flow/decide/cash-cycle` | Manage the cash cycle (463 tokens, terse 463) | `days_receivable`, `days_inventory`, `days_supplier_credit`, `cost_of_sales_per_sales_dollar`, `operating_expense_per_sales_dollar` | the cycle, the cents tied up per sales dollar, and the lever to pull first. |
| `cash-flow/decide/runway` | Keep the runway (382 tokens, terse 260) | `opening_cash`, `periods`; `operating_cash_month`, `bad_month_collections`, `revenue_usd` | the first breach of the floor — the next period's must-pay outflows plus the reserve — and the action order with amounts. |
| `growth/decide/pace` | Set the pace of growth (448 tokens, terse 448) | `planned_growth_pct`, `r_pct`; `self_financeable_ceiling_pct`, `cash_margin_per_sales_dollar`, `days_receivable`, `days_inventory`, `days_supplier_credit`, `cost_of_sales_per_sales_dollar`, `operating_expense_per_sales_dollar`, `outside_capital` | whether the plan funds itself and whether outside money is worth taking. |
| `growth/decide/price` | Set the price (705 tokens, terse 705) | `reference_price`, `incremental_cost`, `segments`; `entry_price`, `segments_can_be_kept_apart`, `below_floor`, `price_move` | the ceiling and floor per segment and the room between them; with the optional inputs, the price at which entry pays, a below-floor case judged on lifetime value, and a price move against its break-even volume change. |
| `risk/decide/concentration` | Limit concentration (517 tokens, terse 517) | `largest_customer_share_pct`, `largest_supplier_share_pct`; `owner_only_functions`, `threshold_pct`, `largest_three_customers_share_pct`, `channel_share_pct`, `channel_owner_can_change_terms_alone`, `largest_customer_contract_makes_whole`, `largest_customer_exposure` | which dependencies are priced risks and what to do first. |
| `value/decide/reinvest-or-distribute` | Reinvest or distribute (619 tokens, terse 561) | `r_pct`, `cash_available`, `candidates`; `screen_pct`, `cash_floor`, `runway_target`, `revenue_usd` | them ranked, the ones to fund from the balance above the cash floor, where to stop, and what to distribute. |
| `cash-flow/decide/owner-pay` | Pay the owner first (98 tokens, terse 98) | `owner_hours_per_year`, `market_wage_per_hour`, `reported_cash_flow`; `distributions_taken` | the cash flow after a market wage — and whether the business is a job that loses money. |
| `value/decide/build-or-run-for-cash` | Build for transfer or run for cash (645 tokens, terse 645) | `durable_position`, `founder_free_revenue_share_pct`, `repeating_revenue_share_pct`; `previous_quarter`, `new_technology`, `window_exit`, `option_plan`, `proof_of_cash` | build-for-transfer or run-for-cash, the matching actions, and the quarterly check; with the optional inputs, the window's exit in cash flow with a priced option to stay, and a buyer's proof of cash. |
| `growth/decide/adjacency` | Approve or refuse an adjacency (563 tokens, terse 563) | `core_not_at_risk`, `only_move_under_way`, `reuses_core`; `move`, `creates_value_for_segment`, `can_be_top_three`, `stop_condition_written`, `failure_patterns`, `core_dimensions_changed`, `capturable_value`, `cost_of_move` | approve or refuse, with the failing screens named. |

## The five market decisions

*Units.* Shares and weights are fractions from 0 to 1 (0.65 means 65%). Scores run 0 to 10. Force scores are whole numbers 1 to 5, scored as pressure on the seller's margins (1 weak, 5 strong). Months are whole numbers. Years are calendar years for crossing and base, and a count for the horizon.

| Decision | Node | Takes (required; optional) | Returns |
|---|---|---|---|
| `market/decide/verdict` | Read a node's verdict (234 tokens, terse 167) | `short_inside_horizon`, `lead_time_months`, `horizon_months`, `suppliers_building`, `relief_documented_inside_horizon`, `price_set_by_wider_cycle`, `supply_elastic` | its verdict — binding, transient, pass-through or open — with the fact that decided it. |
| `market/decide/pricing-power` | Score pricing power (352 tokens, terse 243) | `committed_years`, `lead_time_months`, `lead_time_pre2020_months`, `forces`, `max_downstream_weight`, `tier34_share_marginal`, `propensity_read`, `price_series_rising`; `deposit_reservation_years`, `other_reservation_years`, `allocation_state`, `balance`, `defeat_term`, `transmitted_constraint` | tightness, structure and pricing power 0–10, with the evidence cut applied. |
| `market/decide/binding-node` | Find the binding node (256 tokens, terse 199) | `chain`, `edges` | effective tightness along the path, the binding node and the lag by which its constraint reaches each seat. |
| `market/decide/rent` | Price the rent over the horizon (186 tokens, terse 122) | `base_year`; `pricing_power`, `crossing_year`, `base_month`, `horizon_years`, `nodes` | durability — the years before new supply crosses demand — and rent over the horizon. |
| `market/decide/shock` | Transfer a shock to your seat (325 tokens, terse 228) | `shock_type`, `tier_mix_marginal`, `propensity_read`, `driver_share`, `lead_time_months`, `horizon_months`; `analog`, `dispersion_flag` | the verdict steps and the lag that reach you, with the transfer test applied. |

## What a response looks like

```json
{
  "handle": "business-frameworks/<path>@1.2",
  "applied": {
    "inputs": "<the body as sent>",
    "figures": "<the computed figures>",
    "verdict": "<the decision, worked for these inputs>",
    "action": [
      "<what to do first>",
      "…"
    ],
    "check": "<when to re-run>",
    "basis": [
      "<where the node ends and the arithmetic begins>"
    ]
  },
  "node": {
    "text": "<the node text>",
    "cites": [
      "…"
    ],
    "related": [
      "business-frameworks/<path>@1.2",
      "…"
    ],
    "url": "…/node/<path>"
  },
  "cite_as": "McHenry, J. (2026). Business Frameworks, version 1.2, business-frameworks/<path>@1.2."
}
```

## Two ethics decisions at document version 1.4 — nodes only

Served as nodes at USD 0.05 each, in the same shape; no apply route yet (`/apply` and `/fit` answer `unknown_decision` for them). Read `ethics/feasible` (free) first: it says which options are struck before anything is ranked.

| Decision | Handle | Tokens | Price |
|---|---|---|---|
| A safety objection against cost or schedule | `ethics/decide/safety-concern` | 230 | USD 0.05 |
| Telling the people who rely on a fact | `ethics/decide/disclose` | 418 | USD 0.05 |

## Five worker and quality decisions at document version 1.5 — nodes only

Served as nodes at USD 0.05 each, in the same shape; no apply route yet (`/apply` and `/fit` answer `unknown_decision` for them). Read `worker/read-the-job` (free) before a worker decision: it places the role in one of seven situations, and every worker rule takes the situation as its first input. Read `quality/see-the-work` (free) before a quality decision: it says who judges the result, how soon, against what, and whether the maker can stop the work.

| Decision | Handle | Tokens | Price |
|---|---|---|---|
| Redraw a role so that its holder can see what they finish | `worker/decide/design-the-job` | 491 | USD 0.05 |
| What to count, who sees the count, and how a standard moves | `worker/decide/measure` | 614 | USD 0.05 |
| A stake that works — share, say and sight, sized to the headcount | `worker/decide/share-the-gain` | 492 | USD 0.05 |
| A known defect meets a date | `quality/decide/stop-or-ship` | 299 | USD 0.05 |
| Who sets the standard, who judges against it, and how it moves | `quality/decide/standard` | 318 | USD 0.05 |

## Forty decisions and fourteen methods added at document version 1.6 — nodes only

Served as nodes at USD 0.05 each, in the same shape; none has an apply route (`/apply` answers `unknown_decision` for them, and `/fit` lists them as not measured). Each sits under the branch its path names, and each branch opens with a free root: read the root first, then the one node the question turns on. The fourteen methods — ten under `decision/`, three under `operate/` and `communicate/advise` — are written as inputs / rule / action / check without being a single yes-or-no decision.

| Decision or method | Handle | Tokens | Price |
|---|---|---|---|
| Telling a group about a change | `communicate/decide/tell-a-group` | 279 | USD 0.05 |
| Asking a decider for something | `communicate/decide/the-ask` | 307 | USD 0.05 |
| Where the next customers come from | `customer/decide/acquire` | 257 | USD 0.05 |
| Whom to keep, and how | `customer/decide/retain` | 249 | USD 0.05 |
| Which customers to serve | `customer/decide/select` | 254 | USD 0.05 |
| An adjacent move and the trade-offs it meets | `growth/decide/adjacency/trade-off` | 221 | USD 0.05 |
| A venture hosted inside an existing business | `growth/decide/pace/hosted-venture` | 349 | USD 0.05 |
| How a new venture is judged and funded | `growth/decide/pace/innovation-hurdle` | 286 | USD 0.05 |
| Pricing where each user makes the product worth more | `growth/decide/price/critical-mass` | 409 | USD 0.05 |
| Measuring what buyers will pay | `growth/decide/price/measure-wtp` | 252 | USD 0.05 |
| The unit and structure of a price | `growth/decide/price/structure` | 305 | USD 0.05 |
| The first months after a change of owner | `operate/decide/first-90-days` | 277 | USD 0.05 |
| Who does the improving | `operate/decide/improvement-staffing` | 338 | USD 0.05 |
| A team or a working group | `operate/decide/team-or-group` | 269 | USD 0.05 |
| What the owner hands over | `owner/decide/delegate` | 329 | USD 0.05 |
| The owner under pressure | `owner/decide/under-pressure` | 314 | USD 0.05 |
| The terms that limit what one counterparty can cost | `risk/decide/concentration/counterparty` | 298 | USD 0.05 |
| Dependence on one person | `risk/decide/concentration/key-person` | 342 | USD 0.05 |
| A commitment that cannot be undone | `risk/decide/premortem` | 380 | USD 0.05 |
| The substitute that could replace the business | `risk/decide/substitute` | 437 | USD 0.05 |
| Dependence on a supplier | `risk/decide/supply` | 332 | USD 0.05 |
| Whether a move needs a new business model | `strategy/decide/business-model` | 312 | USD 0.05 |
| Buying a competitor | `strategy/decide/buy-a-rival` | 300 | USD 0.05 |
| The field to compete in | `strategy/decide/industry` | 310 | USD 0.05 |
| Make a stage or contract for it | `strategy/decide/integrate-or-contract` | 238 | USD 0.05 |
| An offer for those who do not buy today | `strategy/decide/new-market` | 302 | USD 0.05 |
| The position | `strategy/decide/position` | 354 | USD 0.05 |
| The core of the strategy in one phrase | `strategy/decide/position/principle` | 309 | USD 0.05 |
| Buying a going concern | `value/decide/buy-a-firm` | 558 | USD 0.05 |
| Diligence before a purchase | `value/decide/buy-a-firm/diligence` | 449 | USD 0.05 |
| Selling the firm | `value/decide/run-the-sale` | 427 | USD 0.05 |
| A newcomer's first months | `worker/decide/arrive` | 250 | USD 0.05 |
| A result that belongs to a group | `worker/decide/design-the-job/group` | 233 | USD 0.05 |
| A hard conversation | `worker/decide/hard-talk` | 321 | USD 0.05 |
| How a skill is learned | `worker/decide/learn` | 217 | USD 0.05 |
| The written expectation and the first miss | `worker/decide/measure/first-miss` | 234 | USD 0.05 |
| Whom to hire | `worker/decide/select` | 232 | USD 0.05 |
| A stake for one key person | `worker/decide/share-the-gain/key-person-stake` | 360 | USD 0.05 |
| How managers are paid | `worker/decide/share-the-gain/managers` | 201 | USD 0.05 |
| How sellers are paid | `worker/decide/share-the-gain/seller-pay` | 242 | USD 0.05 |
| Advise: an answer as sure as its analysis | `communicate/advise` | 337 | USD 0.05 |
| The question before the analysis | `decision/ask` | 234 | USD 0.05 |
| How to carry a change | `decision/change` | 335 | USD 0.05 |
| A change made without new money | `decision/change/no-cash` | 307 | USD 0.05 |
| Scoring a change before it starts | `decision/change/score` | 322 | USD 0.05 |
| Continue or stop | `decision/continue-or-stop` | 249 | USD 0.05 |
| How many changes to carry at once | `decision/effort/initiatives` | 240 | USD 0.05 |
| A test that can be believed | `decision/effort/test` | 284 | USD 0.05 |
| A negotiation | `decision/negotiate` | 312 | USD 0.05 |
| Acting on a prediction | `decision/predict` | 449 | USD 0.05 |
| Who decides | `decision/who-decides` | 264 | USD 0.05 |
| The few measures the business is run by | `operate/metrics` | 268 | USD 0.05 |
| Where people sit, and who talks to whom | `operate/office` | 303 | USD 0.05 |
| How a project is organized | `operate/project` | 288 | USD 0.05 |

## Three rule sentences re-worded at document version 1.3

The rules did not change; their Rule sentences were re-worded where small models misread them in the 2026-10-21 measurement, and the 1.2 text stays readable at `@1.2`.

- `cash-flow/decide/runway`: the floor in every period is one number — the next period's must-pay outflows plus the reserve — and the test is closing cash against that floor; the reserve is part of the floor, not a target, so closing below the floor is a breach while cash is still positive.
- `value/decide/reinvest-or-distribute`: candidates are funded from the whole cash balance; the runway target is held from what remains after them and the rest is distributed; a reserve set aside first and funded from the remainder is the reading the rule excludes.
- `cash-flow/decide/cash-cycle`: two cycles are read, the gross (receivable days plus inventory days) and the net (the gross less supplier-credit days); the cash each dollar of growth costs uses the gross cycle, with supplier credit counted inside the tie-up rather than subtracted from the days.

## Three rule changes at document version 1.2

- `value/decide/reinvest-or-distribute`: an IRR screen (`screen_pct`, default 30, never below r) above the r test; a candidate is funded where its return clears the screen and exceeds r, in return order, stopping at the first that fails either.
- `cash-flow/decide/runway`: the floor for each period is the next period's must-pay outflows plus a reserve of one month of operating cash (`operating_cash_month`; `bad_month_collections` accepted under its 1.0 name through this release); the last period is measured against its own must-pay; every later breach is listed in the action.
- `growth/decide/adjacency`: the second screen is that the offer creates value for a defined segment (`creates_value_for_segment`; `can_be_top_three` accepted through this release); a move that fails a screen is refused as it stands and may be re-submitted once the screen is fixed or dropped.

The twenty-first scenario set that confirms every rule on invented businesses is the evidence pack (`measurement/` for the with-and-without measurement of 2026-10-08; the pack itself is published with the card).

Author page: https://matryoshkaparadigms.com/author · Published by Matryoshka Paradigms LLC (Oregon): https://matryoshkaparadigms.com/ · Cite as: McHenry, J. (2026). *Business Frameworks*, document version 1.6.1, `business-frameworks/<path>@1.6.1`.
