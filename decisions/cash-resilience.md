# Cash resilience

*Business Frameworks · a decision family · document version 1.2 · Joseph McHenry*

> "Our quotes are up, our receivables are at 75 days and the shop is holding more WIP than it ever has: when does the cash run out, and what do we defer first?"

A business can book a profit every month and still miss a payroll, because the cash that profit describes is sitting in receivables and inventory. This family holds the three decisions that turn a forecast into dates and amounts: where the cash breaks, what the cycle is costing, and which outside shock reaches the bank account and when. Each is a fixed rule that can be read as text or run on your own numbers; the free layer above them — the equation, the cash-flow term and the six checks — is on the canonical page and costs nothing.

## The decisions

**Keep the runway** — `business-frameworks/cash-flow/decide/runway@1.2`
*You send:* the opening cash balance; the forecast as a list of periods, each with its inflows, the outflows that must be paid and the outflows that could be deferred; the reserve (a month of operating cash) and, if you have it, annual revenue. *You get back:* the period in which the balance first breaks the floor, the amounts by which it breaks, and an ordered list of what to defer or cut first, with the figures; the rule says how often to re-run the forecast at your size. *Price:* $0.05 to read the node; $0.05 to apply it to your forecast. *Bundle:* `decide/runway` — the decision in full with the cash-flow why node in its short form — $0.07; $0.10 with the $1–5M scale band.

**Manage the cash cycle** — `business-frameworks/cash-flow/decide/cash-cycle@1.2`
*You send:* receivable days, inventory days and supplier-credit days from your own books; cost of sales and operating expense per sales dollar. *You get back:* the cycle in days, how many cents of each sales dollar are tied up for that long, and which of the three day-counts to work on first. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `decide/cash-cycle`, $0.07; $0.10 with the $1–5M band.

**Transfer a shock to your seat** — `business-frameworks/market/decide/shock@1.2`
*You send:* which of four shocks you are testing (end demand falls; suppliers overbuild; credit to leveraged buyers tightens; a policy or export control); how the demand at the node you buy from splits across four buyer tiers; what its suppliers' restraint reads as; the share of its demand that comes from the chain's own driver; its lead time and your planning horizon; and a past episode to carry forward if its buyers resembled today's. *You get back:* what the node's verdict becomes under that shock, step by step, and the lag before it reaches your business. *Price:* $0.05 to read; $0.05 to apply. *Bundles:* `market/shocks-reaching-me` — the shock decision in full with the shock catalogue and the edge method in short form — $0.11, $0.14 with a band; `cross/runway-given-shocks` — the runway decision in full with the shock decision in short form, so the forecast's bad case is written from the chain rather than from a flat haircut — $0.10, $0.13 with a band.

Every input is the caller's own figure; the endpoint looks nothing up, computes by the rule stated in the node, and returns the node's text with the result. A bundle that lists a price "with a band" carries one for the sizes the catalogue names. Payment is per call, USDC on Base over x402, no account.

## A worked example, from the free layer alone

A job shop with $4M of revenue: receivables 75 days, inventory (mostly work in progress) 70 days, suppliers paid in 30. The cash-flow term on the canonical page defines the operating cycle as inventory days plus receivable days, with supplier credit shortening what has to be financed, not the cycle — so 145 days from stock to cash, 30 of them carried by suppliers, 115 financed by the business. What a rise in sales asks of the bank account follows from the balance sheet alone: a quote book up 25% on $4M is $1M of added sales, which at these day-counts adds about $205,000 of receivables and about $119,000 of inventory at cost, less about $51,000 of added supplier credit — roughly $270,000 the new sales have not yet returned, before a single machine is bought. (Cost of sales at 62 cents of each sales dollar; operating expense at 28.) The applied route adds what the free layer cannot: for the cash-cycle decision, the cents each sales dollar ties up over the cycle and which day-count to attack first; for the runway decision, the week the forecast breaks and the order of deferrals with amounts.

## Before you pay

- The third of the six checks on the canonical page — reconcile the year: operating profit after tax, plus non-cash charges, less capital spending, less the change in working capital, should equal the change in the bank balance before financing — is free and catches most "profit but no cash" cases without a node.
- The input schema for each decision is free at `GET https://business-frameworks.matryoshka-paradigms.workers.dev/apply/<decision>`; an example body is included.
- A quote for the bundle a question needs is free and deterministic: `POST …/resolve` with the question and your revenue — or name the decision.
- The measured record for each decision — how often a model stated the rule with no framework, with the free layer and with the node, by model — is free at `GET …/fit?decision=<decision>&model=<model>`. It is a pilot of one run per question and says so on every figure; the shock decision was added at version 1.2 and is not yet measured, and the record says so.

## Not for

Market data, tax or law, industry playbooks, businesses above about $50M in revenue, or long multi-step tasks. The rules carry default parameters for the typical business in scope; the free `decision/parameters` node says how to adjust them.

## Sources this family draws on

Stancill, J., "How Much Money Does Your New Venture Need?", *Harvard Business Review*, May–June 1986 · Churchill, N. and Mullins, J., "How Fast Can Your Company Afford to Grow?", *Harvard Business Review*, May 2001 · Buffett, W., Berkshire Hathaway letter to shareholders, 2009 · Graham, B., *The Intelligent Investor*, Harper, 1949, ch. 20 · Lee, H., Padmanabhan, V. and Whang, S., "The Bullwhip Effect in Supply Chains", *Sloan Management Review*, Spring 1997.

## Cite

McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks

*If this page helped, a like on the dataset's page on Hugging Face is how the next reader finds it.*
