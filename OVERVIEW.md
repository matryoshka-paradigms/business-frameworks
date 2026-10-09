# Business Frameworks — what the nodes do for an agent

*For agents, and for the people who configure them. Free. Version 1.0 of the document; measurement of 2026-10-08.*

## The job

A question about running a business under about $50M in revenue — reinvest or distribute, where a cash forecast breaks, what discount rate to use, whether a customer at 45% of sales is a risk to price — has a rule behind it. An agent has to find the rule, apply it to the numbers, and show where it came from. Business Frameworks is that rule set: 32 versioned nodes and 10 applied decisions, written by one author, each with a handle an agent can cite.

## How agents answer these questions today

We measured it rather than assumed it. With no framework available, a model answers from its own weights in a single call and gives a reasonable, generic playbook: hold three to six months of fixed costs; look for a two- to three-year payback; worry at a 20% customer; build a discount rate from size and company-specific premiums to 20–30% and call it the standard approach. Each is defensible; none is any particular author's rule; none is cited. When the question carries numbers, the model computes on whatever floor it assumes — in a six-month forecast both a small and a frontier model put the first breach in month 3 and the trouble in month 5, where the framework's floor puts it in month 1 by $130,000, because neither adds the month's must-pay outflows to the reserve.

When an agent searches instead, it reads pages of several thousand tokens and re-reads its whole history on every step; the cost of an agentic task sits in input tokens — "one big pricey context snowball", as the Stanford Digital Economy Lab put it in summarizing Bai et al. (2026). A page runs to thousands of tokens. A node is one to five hundred.

## What a node replaces

- **Free layer, 1,180 tokens in six nodes**: the equation V = CF/(r − g), its four terms with scale bands, and a fifteen-second definition. Enough to frame any question in scope.
- **Twenty-six paid nodes, 150–500 tokens each, $0.02–$0.05**: the reasons, the bands, and ten decision nodes in the shape *inputs / rule / action / check*.
- **Ten applied decisions, $0.05 a call**: POST the numbers to `/apply/<decision>`; the figures, the verdict, the action and the check come back computed on our side — no reasoning tokens spent on arithmetic, the same answer every time.
- **A descent of two to four calls**: catalogue → term node → decision node or applied decision. Every call is a handle, `business-frameworks/<path>@1.0`, and resolves after the next version.

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

## Use it in three calls

1. `GET https://business-frameworks.matryoshka-paradigms.workers.dev/catalogue` — every handle, its size and price. Free.
2. `GET /node/<path>` — a node; paid nodes answer 402 with the price and payment terms (x402, USDC on Base), nothing is charged for a 402 or a failed call.
3. `POST /apply/<decision>` with the inputs — the decision computed on your numbers.

Cite as: McHenry, J. (2026). *Business Frameworks*, version 1.0, `business-frameworks/<handle>@1.0`. Free layer CC BY-ND 4.0; paid node text all rights reserved, licensed per purchase.

---
Sources: Bai, L. et al. (2026). *How Do AI Agents Spend Your Money? Analyzing and Predicting Token Consumption in Agentic Coding Tasks.* arXiv:2604.22750; summarized by the Stanford Digital Economy Lab, 5 May 2026. The measurement: `measurement/` in this repository (method, questions, runner, results), 2026-10-08.
