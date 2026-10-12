# Pricing bounds

*Business Frameworks · a decision family · document version 1.2 · Joseph McHenry*

> "Our reference competitor quotes at a known price; our part saves the customer rework. What is the floor, the ceiling and the room between them for each segment we quote?"

A price has two bounds. The ceiling is what the customer's alternative costs plus what your product is worth to that customer over it; the floor is what one more unit costs you to make and ship. Between them is the room you have, and it differs by segment — the plant that cannot afford a rework has more room than the buyer who resells the part as a commodity. Above the segment arithmetic sits a second question the market term answers: whether your seat in the chain lets you hold a price at all, and for how long. This family holds the segment decision and the three chain decisions that bound it. The free layer that frames them (the growth term, the market term and its check) is on the canonical page at no cost.

## The decisions

**Set the price** — `business-frameworks/growth/decide/price@1.2`
*You send:* the reference price — what the customer would otherwise pay, per unit; the incremental, avoidable cost of serving one more customer on the same unit basis; and the segments, each with the value your product carries for that segment over the reference, positive or negative. *You get back:* the ceiling and the floor for each segment and the room between them, and which segments have no room at all. *Price:* $0.05 to read the node; $0.05 to apply it. *Bundles:* `decide/price` — the decision in full with the growth why node in its short form — $0.07; `cross/price-given-pricing-power` — the price decision in full with the pricing-power decision in short form, so the ceiling is bounded by what your seat lets you hold — $0.10; $0.13 with a band.

**Read a node's verdict** — `business-frameworks/market/decide/verdict@1.2`
*You send:* what is known about the stage you sell from or buy from — whether its capacity falls short inside your horizon on documented forecasts; the horizon itself, in months; its lead time to add capacity, from suppliers' own statements; whether its suppliers are building now; whether relief is documented with a date inside the horizon; whether its price is set by a wider cycle; whether supply is elastic. *You get back:* the stage's verdict — binding, transient, pass-through or open — and the one fact that decided it. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `market/verdict` — the decision in full with the balance method, the structure method and the market why node in short form — $0.13.

**Score pricing power** — `business-frameworks/market/decide/pricing-power@1.2`
*You send:* years of output already sold and under reservation; the lead time now against the stage's normal lead time before 2020; how the stage clears today (on allocation, tight, balanced, glut) or its balance; the five forces, each scored as pressure on the seller (named after Porter's five forces and scored here on that single scale); how irreplaceable the stage's output is downstream; the share of marginal demand from leveraged and speculative buyers; what the suppliers' restraint reads as; and whether an observed price series for the output is rising. *You get back:* tightness, structure and pricing power on a 0–10 scale, with the evidence cut applied — a high score is believed only with a rising observed price behind it. *Price:* $0.05 to read; $0.05 to apply. *Bundles:* this decision is sold singly in full; in the two bundles that carry it — `cross/price-given-pricing-power` above and `market/pricing-power-horizon` below — it comes in its short form beside the decision that is central there.

**Price the rent over the horizon** — `business-frameworks/market/decide/rent@1.2`
*You send:* the pricing-power score; the first year in which the stage's supply meets its demand on documented forecasts, or none inside the horizon; the year and month you are asking in; the horizon in years (three by default); or several stages to rank at once. *You get back:* durability — the years before new supply crosses demand — and the rent over the horizon, which is pricing power held for the durability years. *Price:* $0.05 to read; $0.05 to apply. *Bundles:* `market/pricing-power-horizon` — the rent decision in full with the pricing-power decision and the balance method in short form — $0.13, $0.16 with a band; `cross/value-given-chain-position` — the value why node in full with the rent decision and the market why node in short form, so the business is valued as a price-taker's margin or as rent for the durability years — $0.09, $0.12 with a band.

Every figure is the caller's own, with its source named; the endpoint looks nothing up. The rule runs exactly as the node states it and the node's text comes back with the result. A bundle that lists a price "with a band" carries one for the sizes the catalogue names. Payment is per call, USDC on Base over x402, no account.

## A worked example, from the free layer alone

A machined component sells against a competitor's part at $480; the incremental cost of one more unit is $310. Three segments value the part differently: food-grade plants, where the part's finish saves a rework step worth about $140 over the reference; general manufacturing, where it is worth about $20 more; and commodity resale, where the buyer would pay $190 less than the reference for any part that fits. The bounds follow from the economic-value method the schema's own field names describe: the ceiling for each segment is the reference plus the segment's value over it — $620, $500 and $290 — and the floor for every segment is the incremental cost, $310. The food-grade segment has $310 of room, general manufacturing $190, and commodity resale is below the floor: there is no price at which that segment pays for its own unit. That much is arithmetic the free layer licenses. The applied route adds the rule's reading of where in the room to set each price and which segments to decline; the market decisions then say whether the room is yours to keep — a finishing capacity that is committed two years ahead with no documented relief holds a price; a stage whose price is set by a global commodity cycle does not, whatever its own tightness.

## Before you pay

- The sixth of the six checks on the canonical page — name the stage in your chain whose output is committed furthest ahead and write down the months between it going on allocation and your input going short — is the free version of the verdict reading.
- The market term's own condition is the free evidence cut: pricing power above the middle of the scale is believed only with a rising observed price behind it.
- The input schema for each decision, with an example body, is free at `GET https://business-frameworks.matryoshka-paradigms.workers.dev/apply/<decision>`; a bundle quote is free at `POST …/resolve` with the question and your revenue — or name the decision; the measured record for each decision, by model, is free at `GET …/fit?decision=<decision>&model=<model>` (a pilot of one run per question; the five market decisions were added at document version 1.2 and are not yet measured, and the record says so).

## Not for

Market data, tax or law, industry playbooks, businesses above about $50M in revenue, or long multi-step tasks. The chain decisions end at rent per stage and name no company or security; every input about a stage is yours, from your suppliers, your customers or a named source.

## Sources this family draws on

Churchill, N. and Mullins, J., "How Fast Can Your Company Afford to Grow?", *Harvard Business Review*, May 2001 · Porter, M., "How Competitive Forces Shape Strategy", *Harvard Business Review*, March–April 1979 · Porter, M., "The Five Competitive Forces That Shape Strategy", *Harvard Business Review*, January 2008 · Goldratt, E. and Cox, J., *The Goal*, North River Press, 1984 · Lee, H., Padmanabhan, V. and Whang, S., "The Bullwhip Effect in Supply Chains", *Sloan Management Review*, Spring 1997 · Gordon, M. and Shapiro, E., "Capital Equipment Analysis: The Required Rate of Profit", *Management Science*, 3(1), 1956.

## Cite

McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks

*If this page helped, a like on the dataset's page on Hugging Face is how the next reader finds it.*
