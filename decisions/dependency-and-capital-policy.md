# Dependency and capital policy

*Business Frameworks · a decision family · document version 1.2 · Joseph McHenry*

> "One OEM is 45% of our sales and our biggest supplier is single-sourced. What is the concentration rule, and what hurdle should the new five-axis cell clear?"

Two numbers an owner of a $1–25M business carries in the head without ever writing a rule for them: how much of the business depends on one customer, one supplier or the owner alone, and what return a new machine or a new cell has to earn before it is worth the cash. This family holds both rules and the chain reading that sits behind the supplier question — which stage of the chain you buy from is the one that actually binds, and how long its constraint takes to reach you. The free layer that frames them (the risk term, its sub-$5M condition on survival before beta, and the market term) is on the canonical page at no cost.

## The decisions

**Limit concentration** — `business-frameworks/risk/decide/concentration@1.2`
*You send:* the largest customer's share of revenue; the largest supplier's share of purchased inputs; the functions only the owner can perform today, as a short list; and, if you want to move it, the share above which a dependency counts (the default is about a third, a rule of thumb). *You get back:* which of the three dependencies are priced risks for a concentrated owner, and what to do about each first. *Price:* $0.05 to read the node; $0.05 to apply it. *Bundle:* `decide/concentration` — the decision in full with the risk why node in its short form — $0.07; $0.10 with the under-$5M or the $5M-and-up band.

**Set the hurdle rate** — `business-frameworks/risk/decide/hurdle@1.2`
*You send:* the current yield on a long government bond (your figure, with its source and date); the asset betas of two or three comparable public companies, each with its debt stripped out; the market premium you use (a rule of thumb of roughly six points stands in if you send none); any extra return an owner concentrated in this one business states on top; and, below $5M of revenue, the probability the plan works. *You get back:* r for this business — the cost of capital that every reinvestment and growth decision in the document is tested against — with the sub-$5M probability rule and the concentrated owner's stated premium applied, each step shown. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `decide/hurdle` — the decision in full with the risk why node in its short form — $0.07; $0.10 with the under-$5M or the $5M-and-up band.

**Find the binding node** — `business-frameworks/market/decide/binding-node@1.2`
*You send:* the chain you buy through as an ordered list from end demand to the upstream limit, each stage with its tightness, and the edges between them with a weight for how irreplaceable each stage's output is and the lag in months. *You get back:* the effective tightness along the path, the stage that binds, and the lag by which its constraint reaches your seat. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `market/binding` — the decision in full with the edge method in its short form — $0.08; $0.11 with a band.

Every figure is the caller's own and comes with its source; the endpoint looks nothing up. The rule runs exactly as the node states it and the node's text comes back with the result. A bundle that lists a price "with a band" carries one for the sizes the catalogue names. Payment is per call, USDC on Base over x402, no account.

## A worked example, from the free layer alone

A $6M contract manufacturer: one OEM is 45% of sales, one supplier provides 58% of purchased inputs, and only the owner quotes. The risk term on the canonical page carries the rule of thumb in the open — one customer or supplier above about a third of revenue or supply is a priced risk for a concentrated owner — so both the customer and the supplier are over the line before any node is bought; the owner-only quoting is the third dependency, and the decision node ranks the three and says what to do first. For the five-axis cell: the same term says r is the price of the money, a long-bond yield plus a premium scaled by how the business moves with the economy, and that for an owner whose wealth is in this one business that market figure is a floor, not the answer. With a 4.6% bond, comparable asset betas near 1.1 and a six-point premium, the market-referenced rate is about 11% — and the owner's stated premium for being undiversified goes on top. Nothing above $5M needs a survival probability; a business below it does, and the free sub-$5M condition says to keep that probability out of the rate and put it into the cash flows. The applied route produces the exact r and the ranked dependencies; the binding-node decision says which stage behind the single-sourced supplier is the one that actually sets the lead time.

## Before you pay

- The fourth of the six checks on the canonical page — if a rate above 30% is being used to discount a sub-$5M business, write down the survival probability it hides and the ordinary rate that remains — is free and settles most "venture rate" arguments.
- The sixth check — name the stage in your chain whose output is committed furthest ahead and the months between it going on allocation and your input going short — is the free version of the binding-node reading.
- The input schema for each decision, with an example body, is free at `GET https://business-frameworks.matryoshka-paradigms.workers.dev/apply/<decision>`; a bundle quote is free at `POST …/resolve` with the question and your revenue — or name the decision, since a question that asks for the concentration rule and the hurdle together is two decisions; the measured record for each decision, by model, is free at `GET …/fit?decision=<decision>&model=<model>` (a pilot of one run per question, labelled as such).

## Not for

Market data, tax or law, industry playbooks, businesses above about $50M in revenue, or long multi-step tasks. The hurdle decision asks for the bond yield and the betas as your inputs with their source; it does not supply market data, and a figure you have not sourced is not the framework's figure.

## Sources this family draws on

Ruback, R., "Capital Cash Flows: A Simple Approach to Valuing Risky Cash Flows", *Financial Management*, Summer 2002 · Porter, M., "How Competitive Forces Shape Strategy", *Harvard Business Review*, March–April 1979 · Porter, M., "The Five Competitive Forces That Shape Strategy", *Harvard Business Review*, January 2008 · Goldratt, E. and Cox, J., *The Goal*, North River Press, 1984 · Graham, B., *The Intelligent Investor*, Harper, 1949, ch. 20.

## Cite

McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks

*If this page helped, a like on the dataset's page on Hugging Face is how the next reader finds it.*
