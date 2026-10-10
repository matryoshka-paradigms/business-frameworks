# The decisions — what each takes, what it returns

*Document version 1.2 (endpoint build 2026.10.10). Fifteen decision nodes, each in the shape inputs / rule / action / check, each applied to the caller's own figures at `POST /apply/<path>` for the node's price (USD 0.05). The schema and an example are free at `GET /apply/<path>`; an unpaid POST answers 402 with `body_check`, so a body is found wrong before anything is paid. The rule is applied exactly as the node states it — no model sits between the inputs and the answer. Prices and handles are in the live catalogue; this page is for orientation.*

Ask narrow, pay per node; ask broad, get a quoted bundle whose price is the sum of the nodes it takes, stated before you pay.

## The ten decisions of value, cash flow, risk and growth

*Units.* Fields ending _pct take a number of percent (13 means 13%, not 0.13). Fields ending _per_sales_dollar are fractions of a sales dollar (0.65 means 65 cents), and probabilities run from 0 to 1. Money is a plain number in one currency for the whole call; revenue_usd alone is in US dollars, because the scale bands are set in US dollars.

| Decision | Node | Takes (required; optional) | Returns |
|---|---|---|---|
| `risk/decide/hurdle` | Set the hurdle rate (170 tokens, terse 170) | `long_bond_yield_pct`, `asset_betas`; `market_premium_pct`, `personal_premium_pct`, `revenue_usd`, `plan_probability` | r for this business — its cost of capital, the discount rate — with the sub-$5M probability rule and the concentrated owner's stated premium applied. |
| `cash-flow/decide/cash-cycle` | Manage the cash cycle (160 tokens, terse 160) | `days_receivable`, `days_inventory`, `days_supplier_credit`, `cost_of_sales_per_sales_dollar`, `operating_expense_per_sales_dollar` | the cycle, the cents tied up per sales dollar, and the lever to pull first. |
| `cash-flow/decide/runway` | Keep the runway (317 tokens, terse 195) | `opening_cash`, `periods`; `operating_cash_month`, `bad_month_collections`, `revenue_usd` | the first breach of the floor — the next period's must-pay outflows plus the reserve — and the action order with amounts. |
| `growth/decide/pace` | Set the pace of growth (146 tokens, terse 146) | `planned_growth_pct`, `r_pct`; `self_financeable_ceiling_pct`, `cash_margin_per_sales_dollar`, `days_receivable`, `days_inventory`, `days_supplier_credit`, `cost_of_sales_per_sales_dollar`, `operating_expense_per_sales_dollar`, `outside_capital` | whether the plan funds itself and whether outside money is worth taking. |
| `growth/decide/price` | Set the price (196 tokens, terse 196) | `reference_price`, `incremental_cost`, `segments` | the ceiling and floor per segment and the room between them. |
| `risk/decide/concentration` | Limit concentration (137 tokens, terse 137) | `largest_customer_share_pct`, `largest_supplier_share_pct`; `owner_only_functions`, `threshold_pct` | which dependencies are priced risks and what to do first. |
| `value/decide/reinvest-or-distribute` | Reinvest or distribute (258 tokens, terse 200) | `r_pct`, `cash_available`, `runway_target`, `candidates`; `screen_pct`, `revenue_usd` | them ranked, the ones to fund, where to stop, and what to distribute. |
| `cash-flow/decide/owner-pay` | Pay the owner first (98 tokens, terse 98) | `owner_hours_per_year`, `market_wage_per_hour`, `reported_cash_flow`; `distributions_taken` | the cash flow after a market wage — and whether the business is a job that loses money. |
| `value/decide/build-or-run-for-cash` | Build for transfer or run for cash (165 tokens, terse 165) | `durable_position`, `founder_free_revenue_share_pct`, `repeating_revenue_share_pct`; `previous_quarter` | build-for-transfer or run-for-cash, the matching actions, and the quarterly check. |
| `growth/decide/adjacency` | Approve or refuse an adjacency (257 tokens, terse 257) | `core_not_at_risk`, `only_move_under_way`, `reuses_core`; `move`, `creates_value_for_segment`, `can_be_top_three`, `stop_condition_written`, `failure_patterns` | approve or refuse, with the failing screens named. |

## The five market decisions

*Units.* Shares and weights are fractions from 0 to 1 (0.65 means 65%). Scores run 0 to 10. Force scores are whole numbers 1 to 5, scored as pressure on the seller's margins (1 weak, 5 strong). Months are whole numbers. Years are calendar years for crossing and base, and a count for the horizon.

| Decision | Node | Takes (required; optional) | Returns |
|---|---|---|---|
| `market/decide/verdict` | Read a node's verdict (234 tokens, terse 167) | `short_inside_horizon`, `lead_time_months`, `horizon_months`, `suppliers_building`, `relief_documented_inside_horizon`, `price_set_by_wider_cycle`, `supply_elastic` | its verdict — binding, transient, pass-through or open — with the fact that decided it. |
| `market/decide/pricing-power` | Score pricing power (291 tokens, terse 228) | `committed_years`, `lead_time_months`, `lead_time_pre2020_months`, `forces`, `max_downstream_weight`, `tier34_share_marginal`, `propensity_read`, `price_series_rising`; `deposit_reservation_years`, `other_reservation_years`, `allocation_state`, `balance`, `defeat_term`, `transmitted_constraint` | tightness, structure and pricing power 0–10, with the evidence cut applied. |
| `market/decide/binding-node` | Find the binding node (256 tokens, terse 199) | `chain`, `edges` | effective tightness along the path, the binding node and the lag by which its constraint reaches each seat. |
| `market/decide/rent` | Price the rent over the horizon (186 tokens, terse 122) | `base_year`; `pricing_power`, `crossing_year`, `base_month`, `horizon_years`, `nodes` | durability — the years before new supply crosses demand — and rent over the horizon. |
| `market/decide/shock` | Transfer a shock to your seat (298 tokens, terse 228) | `shock_type`, `tier_mix_marginal`, `propensity_read`, `driver_share`, `lead_time_months`, `horizon_months`; `analog`, `dispersion_flag` | the verdict steps and the lag that reach you, with the transfer test applied. |

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

## Three rule changes at document version 1.2

- `value/decide/reinvest-or-distribute`: an IRR screen (`screen_pct`, default 30, never below r) above the r test; a candidate is funded where its return clears the screen and exceeds r, in return order, stopping at the first that fails either.
- `cash-flow/decide/runway`: the floor for each period is the next period's must-pay outflows plus a reserve of one month of operating cash (`operating_cash_month`; `bad_month_collections` accepted under its 1.0 name through this release); the last period is measured against its own must-pay; every later breach is listed in the action.
- `growth/decide/adjacency`: the second screen is that the offer creates value for a defined segment (`creates_value_for_segment`; `can_be_top_three` accepted through this release); a move that fails a screen is refused as it stands and may be re-submitted once the screen is fixed or dropped.

The twenty-first scenario set that confirms every rule on invented businesses is the evidence pack (`measurement/` for the with-and-without measurement of 2026-10-08; the pack itself is published with the card).
