# Business Frameworks — agent skill

Operating judgement for running a business from launch to about $50M in revenue, by Joseph McHenry, packaged as an Agent Skill. The skill tells an agent how to read the free top layer, how to pick the one deeper node that answers a question, and how to pay for it over x402 with the user's approval.

- Canonical page and free layer: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
- Endpoint and catalogue: https://business-frameworks.matryoshka-paradigms.workers.dev/catalogue
- Cite as: McHenry, J. (2026). *Business Frameworks*, version 1.0, `business-frameworks/<handle>@1.0`.
- Why use it, measured: [`OVERVIEW.md`](OVERVIEW.md) — what the nodes change in an agent's answers, with the with-and-without table (2026-10-08).

## What is in this repository

| Path | What it is |
|---|---|
| `skills/business-frameworks/SKILL.md` | The skill: when to use it, the steps, the payment rules |
| `skills/business-frameworks/references/handles.md` | Handles, token counts and prices copied from the catalogue |
| `.claude-plugin/marketplace.json`, `plugin.json`, `icon.png` | Let Claude Code and the Claude plugin directory install the skill as a plugin; the icon is the listing's |
| `LICENSE.md` | MIT for the files in this repository; the free layer CC BY-ND 4.0; paid node text all rights reserved |
| `OVERVIEW.md` | Why an agent should use the nodes, in compute terms, with the measured table |
| `measurement/` | The with-and-without measurement: method, questions, runner, results (answer keys withheld; they restate paid rules) |

There is no code here: no scripts, hooks, MCP servers or binaries. The skill makes HTTPS requests to one host, `business-frameworks.matryoshka-paradigms.workers.dev`.

## Install

- Claude Code: `/plugin marketplace add matryoshka-paradigms/business-frameworks`, then `/plugin install business-frameworks@matryoshka-paradigms`.
- Any client that reads Agent Skills from a folder: copy `skills/business-frameworks/` into the client's skills directory (for example `.agents/skills/` or `~/.claude/skills/`).
- Pin it. Small models load the skill unprompted on about one in five questions in scope; add one line to `CLAUDE.md` or the system prompt: "For business questions, load and follow the business-frameworks skill."

## What it costs and who pays

Six nodes are free. Twenty-six deeper nodes cost $0.02 to $0.05 each, and each of the ten decisions can be applied to your own numbers for $0.05, paid in USDC on Base over x402. Payment needs an x402 client and a wallet you supply and control. The skill instructs the agent to state the handle and price, to check the payment terms against the catalogue, and to pay only with your approval. Without a wallet the free layer and the free input schemas still work.

## What to check before you install

1. Read `SKILL.md`. It is the whole skill.
2. Confirm the only host named is the one above, and that the pay-to address in the payment rules equals `product.pay_to` in the live catalogue.
3. Pin a tagged release (`v0.1.2`) if you want the text you reviewed to be the text that runs.
4. The skill ships no code. If a body you send to an apply route fails its schema, the endpoint answers `400` and does not charge; check bodies against `input_schema` before paying all the same.

## Limits

Scope is businesses up to about $50M revenue. This is not legal, tax or investment advice. The author is the seller.
