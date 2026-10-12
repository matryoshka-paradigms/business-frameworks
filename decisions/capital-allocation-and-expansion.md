# Capital allocation and expansion

*Business Frameworks · a decision family · document version 1.2 · Joseph McHenry*

> "We can add a second shift, a finishing line or a service contract business. Which of them clears the screens, how fast can we grow on our own cash, and do we distribute this year?"

Between $5M and $25M the dominant question stops being survival and becomes allocation: there is cash, there are more uses for it than there is cash, and the owner's job is to rank them against the cost of the money and against each other. This family holds the three decisions that do the ranking — what to fund and what to pay out, how fast the business can grow without outside money, and whether a move outside the core should be approved at all — plus the cross-cut that reads the pace of growth against the stage of the chain that limits supply. The free layer that frames them (the value term, the growth term, the fifth of the six checks and the four decision-method nodes) is on the canonical page at no cost.

## The decisions

**Reinvest or distribute** — `business-frameworks/value/decide/reinvest-or-distribute@1.2`
*You send:* r, the business's hurdle rate; the screen above it (a default of 30%, a rule of thumb, adjustable one rung at a time by the free `decision/parameters` node); all the cash on hand as one balance; the runway you want to keep; annual revenue; and the candidate uses, each with the cash it needs, its expected return and, below $5M, its probability of working. *You get back:* the candidates ranked, the ones to fund in order, where to stop, and what is left to distribute. *Price:* $0.05 to read the node; $0.05 to apply it. *Bundle:* `decide/reinvest-or-distribute` — the decision in full with the value why node in its short form — $0.07; $0.10 with the $5–25M scale band.

**Set the pace of growth** — `business-frameworks/growth/decide/pace@1.2`
*You send:* the planned growth rate; r; either the self-financeable ceiling if you already know it or the figures that produce it (cash margin per sales dollar, the three day-counts, the two cost shares); and the terms of any outside money on offer — what it would earn and what it costs. *You get back:* whether the plan funds itself, the ceiling if you did not send one, and whether the outside capital is worth taking. *Price:* $0.05 to read; $0.05 to apply. *Bundles:* `decide/pace` — the decision in full with the growth why node in its short form — $0.07; `cross/growth-given-binding-node` — the pace decision in full with the binding-node decision and the self-financeable method in short form, so the plan is tested against the allocation the chain will give you as well as against your own cash — $0.13; $0.16 with a band.

**Approve or refuse an adjacency** — `business-frameworks/growth/decide/adjacency@1.2`
*You send:* your answers to the screens — the core is not put at risk; the offer creates value for a defined customer segment against that segment's best alternative; this is the only move under way; the move reuses core customers, channels or capabilities; a stop condition is written down — and which of seven failure patterns you judge to apply. *You get back:* approve or refuse, with the failing screens and the matching failure pattern named. The endpoint works on the judgments you send and does not check them. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `decide/adjacency` — the decision in full with the growth why node in its short form — $0.07; $0.10 with the $25–50M band.

Every figure and every screen is the caller's own; the endpoint looks nothing up. The rule runs exactly as the node states it and the node's text comes back with the result. A bundle that lists a price "with a band" carries one for the sizes the catalogue names. Payment is per call, USDC on Base over x402, no account.

## A worked example, from the free layer alone

A $12M precision machining business with $900,000 in the bank wants to keep $350,000 of runway and has four uses for the rest: a second-shift crew ($90,000, an expected 55%), a five-axis mill ($280,000, 35%), a scheduling-system replacement ($150,000, 18%) and a finishing line ($400,000, 24%); r is 12%, and the plan is to grow 20%.

The free layer settles the shape of the answer before any node is read. The value term says value is created only where the capital inside the business earns more than r — so all four uses clear the cost of money, the scheduling system and the finishing line by a few points, the crew and the mill by a lot. The fifth of the six checks names the method for the cash ceiling (Churchill and Mullins, 2001): with 7 cents of cash generated per sales dollar, cost of sales at 60 cents and operating expense at 30, receivables at 55 days and inventory at 35 against 30 days of supplier credit, the business can fund growth of roughly 50% a year from its own cash — so a 20% plan does not need outside money, and the question is purely which uses to fund. The free layer stops there: it neither ranks the four nor says what to hold. The canonical page does say that this decision's rule screens candidates at a default of 30% before the r test, which only the crew and the mill pass; what that leaves to hold against the $350,000 target and what to distribute is the node's answer on your balance, and the ladder in `decision/parameters` is how the screen is moved — one rung, on evidence, for every candidate alike — when the 18% and 24% uses deserve another look. The adjacency decision is for the day the finishing line becomes a service business for other people's parts.

## Before you pay

- The free `decision` branch on the canonical page — `decision`, `decision/parameters`, `decision/extension`, `decision/effort` — says how the defaults in these rules are set, how to move them one rung at a time, what to do outside the bands and how much analysis a decision of this size deserves.
- The fifth of the six checks — compute the self-financeable growth rate and name where any cash above it comes from — gives the method in a sentence; the node `growth/self-financeable` ($0.03) works it through, and the pace decision computes it from your figures.
- The input schema for each decision, with an example body, is free at `GET https://business-frameworks.matryoshka-paradigms.workers.dev/apply/<decision>`; a bundle quote is free at `POST …/resolve` with the question and your revenue — or name the decision, since a question that asks for the pace, the allocation and the adjacency together is three; the measured record for each decision, by model, is free at `GET …/fit?decision=<decision>&model=<model>` (a pilot of one run per question, labelled as such).

## Not for

Market data, tax or law, industry playbooks, businesses above about $50M in revenue, or long multi-step tasks. An acquisition, a plant or a change of ownership earns the full method — the forecast and the pro forma — not a rule with defaults; the free `decision/effort` node says where that line falls.

## Sources this family draws on

Churchill, N. and Mullins, J., "How Fast Can Your Company Afford to Grow?", *Harvard Business Review*, May 2001 · Bruner, R., *Applied Mergers and Acquisitions*, Wiley, 2004, ch. 3 · Zook, C. and Allen, J., "Growth Outside the Core", *Harvard Business Review*, December 2003 · Zook, C. and Allen, J., *Profit from the Core*, Harvard Business Press, 2010, ch. 2 and 3 · Porter, M., "From Competitive Advantage to Corporate Strategy", *Harvard Business Review*, May 1987 · Gordon, M. and Shapiro, E., "Capital Equipment Analysis: The Required Rate of Profit", *Management Science*, 3(1), 1956.

## Cite

McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks

*If this page helped, a like on the dataset's page on Hugging Face is how the next reader finds it.*
