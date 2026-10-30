# Business Frameworks — agent skill

Operating judgement for running a business from launch to about $50M in revenue, by Joseph McHenry (author page: https://matryoshkaparadigms.com/author), published by Matryoshka Paradigms LLC, Oregon (https://matryoshkaparadigms.com/), packaged as an Agent Skill. The skill tells an agent how to read the free top layer, how to pick the one deeper node that answers a narrow question or the quoted bundle that answers a broad one, and how to pay over x402 with the user's approval.

> Ask narrow, pay per node; ask broad, get a quoted bundle at USD 0.05, stated before you pay.

- Canonical page and free layer: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
- Endpoint and catalogue: https://business-frameworks.matryoshka-paradigms.workers.dev/catalogue
- Cite as: McHenry, J. (2026). *Business Frameworks*, document version 1.4, `business-frameworks/<handle>@1.4`.
- Why use it, measured: [`OVERVIEW.md`](OVERVIEW.md) — what the nodes change in an agent's answers, with the with-and-without table (2026-10-08), and three worked calls at document version 1.3: a narrow question, a broad one, and a decision run on the user's figures.
- Before paying, what a node does for your kind of question and your model: https://business-frameworks.matryoshka-paradigms.workers.dev/fit — the measured rule-right rates, the cost per right answer and the recommended path, with a verdict per decision (`use`, `apply`, `unproven`, `not_measured`); the same block is in every 402.

## What is in this repository

| Path | What it is |
|---|---|
| `skills/business-frameworks/SKILL.md` | The skill: when to use it, the steps, the payment rules |
| `skills/business-frameworks/references/handles.md` | Handles, token counts, prices and the twenty bundles copied from the catalogue |
| `.claude-plugin/marketplace.json`, `plugin.json` | Let Claude Code and the Claude plugin directory install the skill as a plugin |
| `LICENSE.md` | MIT for the files in this repository; the free layer CC BY-ND 4.0; paid node text all rights reserved |
| `OVERVIEW.md` | Why an agent should use the nodes, in compute terms, with the measured table |
| `measurement/` | The with-and-without measurement: method, questions, runner, results (answer keys withheld; they restate paid rules) |
| `evals/` | A suite for `claude plugin eval`: the free layer with the plugin and without, re-runnable by anyone on their own account (see `evals/README.md`) |

There is no code here: no scripts, hooks, MCP servers or binaries. The skill makes HTTPS requests to one host, `business-frameworks.matryoshka-paradigms.workers.dev`. (The endpoint itself also serves the nodes as an MCP server at `/mcp`, and describes itself at `/llms.txt`, `/.well-known/x402` and `/openapi.json`; the skill needs none of them.)

What the endpoint records: the endpoint keeps a request log: time, method, path, status, duration, user agent, whether a payment header was present, and the payer address and transaction when a call settles — never an IP address, a request body, an applied decision's inputs, or a query string.

## Install

- Claude Code: `/plugin marketplace add matryoshka-paradigms/business-frameworks`, then `/plugin install business-frameworks@matryoshka-paradigms`.
- Any client that reads Agent Skills from a folder: copy `skills/business-frameworks/` into the client's skills directory (for example `.agents/skills/` or `~/.claude/skills/`).
- Pin it. Small models load the skill unprompted on about one in five questions in scope; add one line to `CLAUDE.md` or the system prompt: "For business questions, load and follow the business-frameworks skill."

## What it costs and who pays

Thirteen nodes are free. Fifty-four deeper nodes cost $0.02 to $0.05 each, fifteen of the seventeen decisions can be applied to your own numbers for $0.05, and a bundle — the nodes a broad task takes, quoted free first — costs a flat $0.05 with or without its scale band, paid in USDC on Base over x402. Nothing on the endpoint costs more than $0.05 a call. Payment needs an x402 client and a wallet you supply and control. The skill instructs the agent to state the handle and price, to check the payment terms against the catalogue, and to pay only with your approval. Without a wallet the free layer and the free input schemas still work.

## What to check before you install

1. Read `SKILL.md`. It is the whole skill.
2. Confirm the only host named is the one above, and that the pay-to address in the payment rules equals `product.pay_to` in the live catalogue.
3. Pin a tagged release (`v0.3.0`) if you want the text you reviewed to be the text that runs.
4. The skill ships no code. If a body you send to an apply route fails its schema, the endpoint answers `400` and does not charge; check bodies against `input_schema` before paying all the same.

## Limits

Scope is businesses up to about $50M revenue. This is not legal, tax or investment advice. The author is the seller.

**If a request is refused with 403 and error 1010.** Send a `User-Agent` header that names your client. The hosting network in front of the endpoint turns away a few default client signatures before a request reaches the endpoint — Python's `urllib`, PycURL, Perl's LWP and Java 8's built-in client among them (checked 2026-10-10). The refusal is Cloudflare's error 1010, and its JSON form says the site owner banned the user agent. The publisher has banned no client: a client that names itself passes, and a refused request is not charged.

## Changes

- **0.4.0 (2026-10-29)** — document version 1.4 on endpoint build 2026.10.29: the ethics vector — eight nodes under `ethics/` (the root and its feasibility method free; a why node, one node each on risk, cash flow and growth, and two decisions served as nodes only) — and one sentence in the equation's honest limit. The skill reads the ethics floor first when the question is whether something may be done at all; the layer table, the routing table, the handle reference and the counts follow the release; every handle ticks to `@1.4` and 1.3 stays readable at `@1.3`. `server.json` at 2026.10.29 for the MCP Registry.
- **0.3.1 (2026-10-26)** — the author page (https://matryoshkaparadigms.com/author) and the publisher, Matryoshka Paradigms LLC (Oregon), named in this README, `OVERVIEW.md`, `DECISIONS.md`, the skill's metadata and the plugin manifest, so that an agent reading the repository reaches the same author and organization entities as the card, the endpoint and the site. No change to the skill's steps, shapes or payment rules; document version 1.3 and endpoint build 2026.10.22 unchanged.
- **0.3.0 (2026-10-22)** — document version 1.3 on endpoint build 2026.10.22. Three decision rules re-worded where small models misread them (the runway floor as one number with the reserve part of it; reinvestment funded from the whole balance, the reserve-first reading named as excluded; the gross and the net cash cycle both named, the tie-up on the gross) — every handle is `@1.3`, the 1.2 and 1.0 texts stay readable at their own handles. A third variant of every node, `?variant=agent`: the accepted text as fields (scope, inputs, rule, action, check, reasoning, units, a worked example, the applied route, the recheck, and two strings to paste — `recheck_note` and `closing_citation`), the same price; `bf_read_node` takes it too. Every bundle at a flat USD 0.05, band included, and the access sentence re-stated on every surface; the per-payment cap in the skill falls to USD 0.05. The skill's step 8 says how to answer with a node in hand (the decision in one sentence, the first step, the reason, the next check, the offer to write the recheck into the user's notes, the citation last) and sends figures to the applied route rather than computing by hand. The six MCP tools declare output schemas; the payment-required tool result carries the 402's facts; `openapi.json` carries real response examples for the applied routes.
- **0.2.0 (2026-10-10)** — document version 1.2 on endpoint build 2026.10.10: 59 nodes (32 re-cut in one shape — lede, conditions, reasoning — and served full or terse at the same price; 27 new: the `market` branch with its why node, six method nodes, four scale bands, six chain patterns and five applied decisions, and the free `decision` branch on parameters, extension and effort). Twenty quoted bundles behind a free deterministic resolver (`POST /resolve`). The skill routes narrow questions to one node and broad ones to a quote, adds the market and bundle rows to its table, raises the per-payment cap to USD 0.25 for bundles, and states the two variants. Every handle is `@1.2`; the 1.0 text stays readable at `@1.0`. The MCP server has six tools. 0.1.4's skill fix and `evals/` are included.
- **0.1.4 (2026-10-10)** — the skill body no longer writes a dollar sign directly before a digit: Claude Code reads `$0`, `$1` and `$5` in a skill as argument placeholders, so on a load with arguments the prices, the payment cap and the scale bands reached the model rewritten (found by the eval suite). Amounts now read `USD 0.05`. `evals/` added: a suite for `claude plugin eval`, free layer only. The skill and this page now ask clients to send a `User-Agent` header: the host's edge refuses some default client signatures with 403, error 1010, before a request reaches the endpoint.
- **0.1.3 (2026-10-09)** — the skill asks `/fit` before paying and follows its verdict; the shapes name the JSON 402 body, `body_check`, `HEAD` → 402 and the versioned route; the endpoint's data statement (above) is stated in the skill. Endpoint 1.2 deployed the same day: a request log as stated, JSON 402 bodies with the payment terms, the fit block, `/llms.txt`, `/.well-known/x402`, `/openapi.json`, an MCP server at `/mcp`, and one URL spelling per paid route. The nodes are unchanged at 1.0.
- **0.1.2 (2026-10-08)** — icon; the payment rules say the skill never reads, holds or transmits a key.
- **0.1.1 (2026-10-08)** — `OVERVIEW.md` and the measurement; the description says to use the skill even when the figures are given; step "say what the framework does not supply"; the pin line.
- **0.1.0 (2026-10-07)** — first release.
