# Business Frameworks — agent skill

Operating judgement for running a business from launch to about $50M in revenue, by Joseph McHenry, packaged as an Agent Skill. The skill tells an agent how to read the free top layer, how to pick the one deeper node that answers a question, and how to pay for it over x402 with the user's approval.

- Canonical page and free layer: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
- Endpoint and catalogue: https://business-frameworks.matryoshka-paradigms.workers.dev/catalogue
- Cite as: McHenry, J. (2026). *Business Frameworks*, version 1.0, `business-frameworks/<handle>@1.0`.
- Why use it, measured: [`OVERVIEW.md`](OVERVIEW.md) — what the nodes change in an agent's answers, with the with-and-without table (2026-10-08).
- Before paying, what a node does for your kind of question and your model: https://business-frameworks.matryoshka-paradigms.workers.dev/fit — the measured rule-right rates, the cost per right answer and the recommended path, with a verdict per decision (`use`, `apply`, `unproven`, `not_measured`); the same block is in every 402.

## What is in this repository

| Path | What it is |
|---|---|
| `skills/business-frameworks/SKILL.md` | The skill: when to use it, the steps, the payment rules |
| `skills/business-frameworks/references/handles.md` | Handles, token counts and prices copied from the catalogue |
| `.claude-plugin/marketplace.json`, `plugin.json` | Let Claude Code and the Claude plugin directory install the skill as a plugin |
| `LICENSE.md` | MIT for the files in this repository; the free layer CC BY-ND 4.0; paid node text all rights reserved |
| `OVERVIEW.md` | Why an agent should use the nodes, in compute terms, with the measured table |
| `measurement/` | The with-and-without measurement: method, questions, runner, results (answer keys withheld; they restate paid rules) |

There is no code here: no scripts, hooks, MCP servers or binaries. The skill makes HTTPS requests to one host, `business-frameworks.matryoshka-paradigms.workers.dev`. (The endpoint itself also serves the nodes as an MCP server at `/mcp`, and describes itself at `/llms.txt`, `/.well-known/x402` and `/openapi.json`; the skill needs none of them.)

What the endpoint records: the endpoint keeps a request log: time, method, path, status, duration, user agent, whether a payment header was present, and the payer address and transaction when a call settles — never an IP address, a request body, an applied decision's inputs, or a query string.

## Install

- Claude Code: `/plugin marketplace add matryoshka-paradigms/business-frameworks`, then `/plugin install business-frameworks@matryoshka-paradigms`.
- Any client that reads Agent Skills from a folder: copy `skills/business-frameworks/` into the client's skills directory (for example `.agents/skills/` or `~/.claude/skills/`).
- Pin it. Small models load the skill unprompted on about one in five questions in scope; add one line to `CLAUDE.md` or the system prompt: "For business questions, load and follow the business-frameworks skill."

## What it costs and who pays

Six nodes are free. Twenty-six deeper nodes cost $0.02 to $0.05 each, and each of the ten decisions can be applied to your own numbers for $0.05, paid in USDC on Base over x402. Payment needs an x402 client and a wallet you supply and control. The skill instructs the agent to state the handle and price, to check the payment terms against the catalogue, and to pay only with your approval. Without a wallet the free layer and the free input schemas still work.

## What to check before you install

1. Read `SKILL.md`. It is the whole skill.
2. Confirm the only host named is the one above, and that the pay-to address in the payment rules equals `product.pay_to` in the live catalogue.
3. Pin a tagged release (`v0.1.3`) if you want the text you reviewed to be the text that runs.
4. The skill ships no code. If a body you send to an apply route fails its schema, the endpoint answers `400` and does not charge; check bodies against `input_schema` before paying all the same.

## Limits

Scope is businesses up to about $50M revenue. This is not legal, tax or investment advice. The author is the seller.

## Changes

- **0.1.3 (2026-10-09)** — the skill asks `/fit` before paying and follows its verdict; the shapes name the JSON 402 body, `body_check`, `HEAD` → 402 and the versioned route; the endpoint's data statement (above) is stated in the skill. Endpoint 1.2 deployed the same day: a request log as stated, JSON 402 bodies with the payment terms, the fit block, `/llms.txt`, `/.well-known/x402`, `/openapi.json`, an MCP server at `/mcp`, and one URL spelling per paid route. The nodes are unchanged at 1.0.
- **0.1.2 (2026-10-08)** — icon; the payment rules say the skill never reads, holds or transmits a key.
- **0.1.1 (2026-10-08)** — `OVERVIEW.md` and the measurement; the description says to use the skill even when the figures are given; step "say what the framework does not supply"; the pin line.
- **0.1.0 (2026-10-07)** — first release.
