# Business Frameworks — what the nodes do for an agent

*For agents, and for the people who configure them. Free. Document version 1.2 (endpoint build 2026.10.10); the measurement of 2026-10-08 covers the ten decisions of document version 1.0 and is labelled so.*

## The job

A question about running a business under about $50M in revenue — reinvest or distribute, where a cash forecast breaks, what discount rate to use, whether a customer at 45% of sales is a risk to price — has a rule behind it. An agent has to find the rule, apply it to the numbers, and show where it came from. Business Frameworks is that rule set: 59 versioned nodes, 15 applied decisions and 20 quoted bundles, written by one author, each with a handle an agent can cite. Ask narrow, pay per node; ask broad, get a quoted bundle whose price is the sum of the nodes it takes, stated before you pay.

## How agents answer these questions today

We measured it rather than assumed it. With no framework available, a model answers from its own weights in a single call and gives a reasonable, generic playbook: hold three to six months of fixed costs; look for a two- to three-year payback; worry at a 20% customer; build a discount rate from size and company-specific premiums to 20–30% and call it the standard approach. Each is defensible; none is any particular author's rule; none is cited. When the question carries numbers, the model computes on whatever floor it assumes — in a six-month forecast both a small and a frontier model put the first breach in month 3 and the trouble in month 5, where the framework's floor puts it in month 1 by $130,000, because neither adds the month's must-pay outflows to the reserve.

When an agent searches instead, it reads pages of several thousand tokens and re-reads its whole history on every step; the cost of an agentic task sits in input tokens — "one big pricey context snowball", as the Stanford Digital Economy Lab put it in summarizing Bai et al. (2026). A page runs to thousands of tokens. A node is one to five hundred.

## What a node replaces

- **Free layer, eleven nodes**: the equation V = CF/(r − g), its five terms (value, cash flow, risk, growth and, from document version 1.2, the market as a chain of nodes), a fifteen-second definition, and four nodes on how the decision rules' parameters are set and adjusted. Enough to frame any question in scope.
- **Forty-eight paid nodes, 80–500 tokens each, $0.02–$0.05**: the reasons, the bands, the tools, the market methods and chain patterns, and fifteen decision nodes in the shape *inputs / rule / action / check*. Every node is one shape — a lede that is right on its own, the conditions under which it changes, the reasoning — and is served full or terse (the lede alone) at the same price.
- **Fifteen applied decisions, $0.05 a call**: POST the numbers to `/apply/<decision>`; the figures, the verdict, the action and the check come back computed on our side — no reasoning tokens spent on arithmetic, the same answer every time.
- **Twenty bundles, the sum of their nodes**: for a broad task, `POST /resolve` quotes the minimal set of nodes that answers it, free and deterministically; one payment delivers them in order, the central node full and the rest terse.
- **A descent of two to four calls**: catalogue → term node → decision node, applied decision or quoted bundle. Every call is a handle, `business-frameworks/<path>@1.2`, and resolves after the next version; the 1.0 text stays readable at `@1.0`.

## Where the compute goes, and what changes

Three things cost tokens in an agent's answer: the harness context it re-reads on every call, the content it reads, and the reasoning it writes. A node changes the second and the third, and it adds calls. In a thin harness the per-answer cost therefore rises — in our measurement about 1.9× on a small model and 1.8× on a frontier model — because each extra call re-reads the harness. The saving is not fewer tokens per answer. It is this:

1. **A lighter model carries the rule.** With the decision node's text in hand, a small model stated the framework's rule correctly in 75% of answers at $0.005 an answer; a frontier model without the framework managed 25% at $0.084. Rule-right answers per dollar: about 50× more.
2. **Re-runs avoided.** A wrong frame — the wrong floor, the wrong threshold — costs the whole answer again, or a bad decision. The node removes the re-run.
3. **Arithmetic off the model.** The applied decisions compute; the agent reads.
4. **Read once, use many times.** A node read early in a session is cached for every later call.

## Correctness is the hidden compute

The difference between the two answers to the cash forecast is not style. One puts the trouble in month 5; the framework says the floor is breached in month 1 by $130,000, and what to defer first. A reader who acts on the first answer pays for the second later. Every decision node ships with a check — what to compare, how often — and an evidence pack of twenty scenarios with expected figures accompanies the document, for an agent to run against the live routes.

## Measured

Twenty questions in scope (eleven with figures, nine without), each answered in a fresh headless Claude Code session with tools limited to the endpoint, web search and web fetch. Conditions: no framework; the skill installed and the agent left to decide (*with*); the skill installed plus a one-line standing instruction to use it (*configured*); the same with the ten decision nodes' text in hand, as an agent that had bought them (*nodes*). Answers graded by a model against keys written from the nodes; *rule right* means the answer states the framework's rule as the node does; *cited* means a handle or the author is named. Window 2026-10-08, one harness, n = 20 for the small model and 8 for the frontier model; the method, the questions, the runner and the results are in the repository (`measurement/`); the answer keys are held back because they restate the paid rules.

| Model | Condition | Rule right | Cited | Calls | Context tokens read | Cost per answer | Seconds |
|---|---|---|---|---|---|---|---|
| Claude Haiku | no framework | 15% | 0% | 1.1 | 17,800 | $0.0024 | 10.5 |
| Claude Haiku | with (loaded unprompted on 20%) | 30% | 20% | 1.4 | 24,200 | $0.0027 | 12.5 |
| Claude Haiku | configured, free layer | 50% | 90% | 4.0 | 79,600 | $0.0045 | 16.2 |
| Claude Haiku | configured, decision nodes in hand | **75%** | 95% | 3.5 | 72,000 | $0.0048 | 16.4 |
| Claude Opus | no framework | 25% | 0% | 1.0 | 15,000 | $0.0838 | 18.1 |
| Claude Opus | with (loaded unprompted on 75%) | 75% | 75% | 3.5 | 65,100 | $0.1296 | 23.3 |
| Claude Opus | configured, free layer | 50% | 100% | 4.0 | 75,900 | $0.1481 | 24.2 |
| Claude Opus | configured, decision nodes in hand | 62% | 100% | 4.0 | 76,600 | $0.1508 | 22.9 |

Three things the table says plainly. The rule is in the paid nodes: the free layer frames the question and gets the small model to 50%; the node text takes it to 75%. A standing instruction matters: left to itself, the small model loaded the skill on one question in five, the frontier model on three in four. And the small model with the node beats the frontier model without it on rule, citation and cost — spending more calls and context to do it.

## Before you pay: ask the endpoint what the node does for your question

`GET /fit?decision=<decision-path>&model=<your model>` is free and answers from the table above, by kind of question. For screens and thresholds (hurdle, concentration, adjacency, pace, owner pay, build or run) the recommended path is a small model with the node: 12 of 12 rule-right on those questions at $0.0047 per rule-right answer, against a frontier model alone at $0.435 and a frontier model with the node at $0.181 — and no difference in rule-right rate between the small model with the node and the frontier model with the node that this sample could detect (15 of 20 against 5 of 8, p = 0.65). For the four decisions that are arithmetic over periods (runway, cash cycle, reinvest or distribute, price) the text lifted neither model's answers; the recommended path is the applied route, which computes the verdict. Every figure carries its n and date and is labelled a pilot until the comparison test replaces it; the verdict says `unproven` or `not_measured` where that is the truth.

## Use it in four calls

1. `GET https://business-frameworks.matryoshka-paradigms.workers.dev/catalogue` — every handle, its sizes and price, and the twenty bundles. Free.
2. `GET /node/<path>` — a node (`?variant=terse` for the lede alone); paid nodes answer 402 with a JSON body carrying the price, the payment terms (x402, USDC on Base), how to pay and the fit block; nothing is charged for a 402 or a failed call.
3. `POST /resolve` with the question — a quote for the bundle a broad task takes, free; then `GET` the quote's url and pay once.
4. `POST /apply/<decision>` with the inputs — the decision computed on your numbers.

## Three worked calls at document version 1.2

Every response below is the shape the endpoint returns; the figures are invented for the example, and nothing in a request names a company.

**A narrow question: one node.** The user asks whether an input shortage is real or just a price. The free `market` node frames it (the verdict is read from what is committed, not from the price); the smallest descent is `market/decide/verdict`. `GET /node/market/decide/verdict` answers 402 with the price in the body: `{"error":"payment_required","handle":"business-frameworks/market/decide/verdict@1.2","price_usd":"$0.05","tokens":234,"payment":{...},"how_to_pay":{...}}`. The agent states the handle and the price, the user approves, the request is repeated with the payment header, and the node comes back: `{"handle":"business-frameworks/market/decide/verdict@1.2","variant":"full","text":"Inputs: whether the node is short of capacity inside the horizon; ...","levels":{"lede":"...","conditions":"...","reasoning":"..."},"related":[...],"cite_as":"McHenry, J. (2026). Business Frameworks, version 1.2, business-frameworks/market/decide/verdict@1.2."}`. One call, $0.05, cited by its handle.

**A broad question: a quoted bundle.** The user runs a $2.5M fabricator selling into one customer node that is on allocation and asks what binds the chain and when it reaches them. The question takes more than one node, so the agent quotes it first: `POST /resolve {"question":"...our customer node is on allocation...what binds our chain and when does it reach us","revenue_usd":2500000,"chain_position":"binding_downstream"}`. The answer is free and deterministic: `{"match":"single","by":"patterns","bundle":{"id":"market/binding","task":"Find the node that binds your chain and the lag by which its constraint reaches you","nodes":[{"handle":"business-frameworks/market/decide/binding-node@1.2","variant":"full","price_usd":"$0.05"},{"handle":"business-frameworks/market/band/1-5m@1.2","variant":"terse","role":"scale band","price_usd":"$0.03"},{"handle":"business-frameworks/market/edges@1.2","variant":"terse","price_usd":"$0.03"}],"price_usd":"$0.11","tokens":515,"apply":"POST /apply/market/decide/binding-node","url":".../bundle/market/binding/band/1-5m"}}`. The agent shows the user the three nodes and the $0.11, the user approves, `GET` on the url answers 402 for $0.11 and, paid, returns the three nodes in that order on one settlement — the decision rule full, the scale band and the edge method terse — each with its own `cite_as`. Had the question matched two bundles equally, the answer would have been `candidates` with their task lines; had it matched none, the twenty task lines to choose from. Nothing is read or charged until the user accepts the quote.

**Quantities in hand: the applied route.** The user has the chain drawn — four stages with each stage's tightness and each edge's weight and lag — and wants the binding node computed, not described. `GET /apply/market/decide/binding-node` returns the schema and an example, free; the agent builds the body from the user's figures and checks it against the schema. An unpaid `POST` answers 402 with `body_check: {valid: true}`; paid, the same `POST` returns `{"applied":{"figures":{"binding_node":"...","binding_effective_tightness":7.2,"dominant_transmission":"constraint","nodes":[...]},"verdict":"The chain binds at ... (effective tightness 7.2, inherited from ...); the chain is constraint-dominated.","action":["Place your seat on the path ...","..."],"check":"Re-run when an edge weight crosses a bucket or a crossing year moves.","basis":["the constraint reaching a node is the upstream effective tightness times the edge weight, after the lag; ..."]},"node":{"text":"...","cites":[],"related":[...]}}`. The rule is applied exactly as the node states it; the same inputs give the same result, and the agent spends no reasoning tokens on the propagation.

Cite as: McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. Free layer CC BY-ND 4.0; paid node text all rights reserved, licensed per purchase.

---
Sources: Bai, L. et al. (2026). *How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks.* arXiv:2604.22750; summarized by the Stanford Digital Economy Lab, 5 May 2026. The measurement: `measurement/` in this repository (method, questions, runner, results), 2026-10-08.
