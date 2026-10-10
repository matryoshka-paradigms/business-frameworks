---
name: business-frameworks
description: Operating judgement for a business from launch to about 50M US dollars of revenue, as short versioned decision frameworks built on V = CF/(r − g) and, from document version 1.2, on the market read as a chain of nodes. Use when the user runs or advises a small or mid-sized business and has to decide something about value, cash flow, cost of capital, growth or the market it sells into and buys from — reinvest or distribute, owner pay, the cash cycle, runway, a hurdle rate, concentration, growth pace, a price, an adjacency, which node of a supply chain binds, how much pricing power a position has and for how long, what a shock does to a seat. Use it even when the question already supplies the figures — what it adds is the rule, not the arithmetic. The top layer is free. Deeper nodes, bundles of nodes for a broad task, and decisions applied to the user's own numbers cost USD 0.02–0.20 over x402 (USDC on Base) and need the user's approval before any payment. Not for legal, tax or investment advice, and not for businesses above 50M US dollars of revenue.
license: MIT for the files in this repository (this skill, its references, the manifest and the README); free-layer text quoted from the dataset card CC-BY-ND-4.0; paid node text all rights reserved (see LICENSE.md)
compatibility: Needs outbound HTTPS to business-frameworks.matryoshka-paradigms.workers.dev. The free layer needs nothing else. Paid calls need an x402 client and a wallet holding USDC on Base, both supplied and controlled by the user.
metadata:
  author: Joseph McHenry
  skill-version: "0.2.0"
  product-version: "1.2"
  endpoint-build: "2026.10.10"
  homepage: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
---

# Business Frameworks

A layered document of operating judgement by Joseph McHenry. Every node has a handle `business-frameworks/<path>@<version>`, a token count and a price. One objective sits at the top, V = CF/(r − g): value equals cash flow divided by the cost of capital less long-term growth. Five branches descend from it — value, cash-flow, risk, growth and market (the chain of nodes a business sells into and buys from) — each from the why, to the scale band, to the decision; a sixth, decision, says how every rule's parameters are set and adjusted. The current document version is 1.2.

Ask narrow, pay per node; ask broad, get a quoted bundle whose price is the sum of the nodes it takes, stated before you pay.

This skill ships no code. It tells you which URL to call, what the call costs and when to stop.

Base URL: `https://business-frameworks.matryoshka-paradigms.workers.dev`

## What is free and what is paid

| Layer | What | Nodes | Cost |
|---|---|---|---|
| 0–1 | The equation, the five terms, the fifteen-second definition, the four decision-method nodes | 11 | free |
| 2 | Why-nodes (USD 0.02); scale bands, tools (pro forma, forecast, self-financeable growth), the six market method nodes and the six chain patterns (USD 0.03) | 33 | USD 0.02–0.03 each |
| 3 | Decision nodes: inputs, rule, action, check | 15 | USD 0.05 each |
| apply | A decision node's rule run on the user's numbers | 15 routes | USD 0.05 each |
| bundle | The nodes a broad task takes, quoted first, delivered in order on one settlement | 20 | the sum of the nodes, USD 0.05–0.20 |

Every node is served in two variants at the same price: `full` (the default: the lede, its conditions and its reasoning) and `terse` (`?variant=terse`: the lede alone, which is right on its own, only coarser). A bundle delivers its central node full and the rest terse.

The live catalogue is the authority on handles, token counts, prices and bundles: `GET /catalogue` (free JSON). `references/handles.md` is a copy for orientation and may be older.

## Steps

1. **Start free.** `GET /node/equation`, then the term the question turns on: `/node/value`, `/node/cash-flow`, `/node/risk`, `/node/growth`, `/node/market` (and `/node/value/15s`). Each response has `text`, `levels` (lede, conditions, reasoning), `cites`, `children` with the handles one level down and `related` with the handles to read next. Often this is enough to frame the answer; say so and stop. `/node/decision` and its three children say how the rules' default parameters are meant to be used.
2. **Place the business in a scale band** by annual revenue in US dollars: under 1M, 1–5M, 5–25M, 25–50M. If revenue is unknown, ask. Above 50M, say the document is out of scope.
3. **Narrow question: pick the smallest descent** that answers it (table below). One node is the normal purchase. Do not buy a branch.
4. **Broad question: ask for a quote.** `POST /resolve` with `{question, revenue_usd, chain_position, decision, bundle, inputs}` (all optional; `inputs` is the figures in hand by field name — only the names are read) is free and deterministic. A named bundle or decision wins; then the input fields; then the authored patterns of the question. The answer is one quote (`match: single`) with its nodes, their variants and the price, which is the sum of the nodes' catalogue prices; or `candidates` with task lines to choose from; or, with no match, the twenty task lines and the free roots. Show the user the quote; on approval `GET` the quote's `url` and pay once. Do not resolve a question that one node answers.
5. **If the user has numbers and the question is one of the fifteen decisions, use the apply route.** `GET /apply/<decision-path>` returns the input schema and an example input, free. Build the body from the user's figures, check it against the schema yourself, then `POST` it. The five market decisions take facts about a node or a chain, not company names.
6. **Before paying for a decision, ask what the node does for this kind of question.** `GET /fit?decision=<decision-path>&model=<the model you are running>` is free. It returns the measured record for the ten decisions of document version 1.0 — how often the rule was stated with no framework, with the free layer and with the node, the cost per answer and per rule-right answer by model, the recommended path — and one verdict: `use` (buy the node), `apply` (the text does not lift this kind of question; the applied route computes it), `unproven` (no lift shown for your model class at the sample size — say so and let the user decide), `not_measured` (no figure for your model, or a market decision, which the pilot did not cover), `skip`. The figures are a pilot (one run per question, 2026-10-08) and say so.
7. **Before any paid call, follow the payment rules below.**
8. **Answer with the handle.** Cite `business-frameworks/<path>@<version>` beside each point you take from a node, pass on the node's own citations, and say which calls were paid and what was spent. A bundle's nodes each carry their own `cite_as`.
9. **Say what the framework does not supply.** A bond yield, a beta, a premium you chose, a threshold the node does not state, a chain's edge weights you estimated: label it as your own input or assumption and name the kind of source. Never present your own figure as the framework's.

| The user asks | Go to | Kind |
|---|---|---|
| What should we do with spare cash; fund this project or pay it out | `value/decide/reinvest-or-distribute` | decision + apply |
| Build the business to hand over or sell, or run it for income | `value/decide/build-or-run-for-cash` | decision + apply |
| Profitable but short of cash; where does the cash go | `cash-flow/why`, then `cash-flow/decide/cash-cycle` | why, decision + apply |
| Will we run out; how much reserve; which bills wait | `cash-flow/decide/runway` | decision + apply |
| Is the owner really making money after a fair wage | `cash-flow/decide/owner-pay` | decision + apply |
| What discount rate, hurdle rate or cost of capital to use | `risk/why`, then `risk/decide/hurdle` | why, decision + apply |
| Are we too dependent on one customer, supplier or person | `risk/decide/concentration` | decision + apply |
| How fast can we grow on our own cash; is outside money worth it | `growth/self-financeable`, then `growth/decide/pace` | tool, decision + apply |
| What price can this product carry | `growth/decide/price` | decision + apply |
| Should we enter a new line or market, or buy a company | `growth/decide/adjacency` | decision + apply |
| Which stage of our supply chain binds, and by what lag it reaches us | `market/why`, then `market/decide/binding-node` | why, decision + apply |
| Is this input shortage real, temporary, or just a price | `market/decide/verdict` | decision + apply |
| How much pricing power does our position have, and for how long | `market/decide/pricing-power`, then `market/decide/rent` | decision + apply |
| What does a demand collapse, an overbuild, a credit squeeze or a policy change do to us | `market/shocks`, then `market/decide/shock` | tool, decision + apply |
| Draw the chain we sit in; which stages are nodes | `market/map`, `market/edges`; the six `market/pattern/*` nodes for the hard cases | tool, chain pattern |
| Turn a forecast into a value, or build the forward view | `growth/forecast`, `cash-flow/pro-forma` | tool |
| How does the answer change at our size | `<term>/band/<band>` from the catalogue | scale band |
| A whole decision with its context; a chain read; a shock traced to our seat | `POST /resolve`, then the quoted bundle | bundle |
| A default in a rule does not fit us; the business is outside the bands | `decision/parameters`, `decision/extension`, `decision/effort` | free |

## Payment rules

Paid routes answer `402` with a `PAYMENT-REQUIRED` header (base64 JSON). The request is repeated with a `PAYMENT-SIGNATURE` header produced by the user's x402 client. No account, no API key.

This skill never reads, holds or transmits a key. The signature is made inside the user's own payment tool — a wallet the user installed and controls, such as an x402 wallet MCP server — which asks the user before each payment; the skill only repeats the request with the header that tool returns.

- **Approval first.** Pay only if the user has approved this call, or has set a standing limit that covers it. State the handle and the price before paying; for a bundle, state the quote (the nodes and the sum).
- **Check the terms in the 402 before signing.** All four must hold; if any fails, do not pay and tell the user what differed:
  - network `eip155:8453` (Base mainnet);
  - asset USDC, contract `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`;
  - pay-to `0xbBaCd5111E0Ca3a52DdAA39D4723Cf75C1A75D91`, the same address as `product.pay_to` in the catalogue;
  - amount equal to the catalogue price for that handle — for a bundle, the quoted sum — and never above USD 0.25 (250000 base units).
- **Set the client's per-payment cap** to USD 0.25 or lower where the client has one; USD 0.10 is enough when no bundle is in play.
- **No wallet, no purchase.** If no x402 client is available, stop at the free layer, the free schema and the free quote. Tell the user which handle or bundle would answer the question and what it costs. Never ask for, read or store a private key or recovery phrase.
- **One call, one charge.** Check an apply body against `input_schema` before paying. Do not repeat a paid call for the same question; reuse the response, or the `download_url` it carries for a short while. A body that fails the schema is answered `400` with the schema and is not charged (the payment is verified but never settled); the signature is still spent, so check first.

## Shapes

- Node: `GET /node/<path>[?variant=terse|full]` → `{handle, title, layer, tokens, tokens_terse, variant, text, levels{lede, conditions, reasoning} (full only), cites[], children[], related[], versions[], ...}`. A paid node's `402` carries a JSON body: `handle`, `price_usd`, `payment` (the terms), `how_to_pay`, `fit`, `access`; `HEAD` on a paid route also answers `402`. The versioned spelling `/node/<path>@1.2` is a paid route of its own, and `/node/<path>@1.0` returns the 1.0 text of a node that existed then, marked `superseded_by`.
- Resolver (free): `GET /resolve` → how it works, the twenty task lines, the chain positions; `POST /resolve` → `{match, by, bundle{id, task, nodes[], price_usd, url, band, apply, free_first, extensions[]}}` or `{match: "candidates", candidates[]}` or `{match: "none", tasks[], free[]}`.
- Bundle (paid): `GET /bundle/<id>[/band/<slug>]` → `402` with the summed price and the nodes listed; on payment `{handle, id, task, price_usd, nodes[{handle, variant, role, text, cites[], cite_as}], apply, next[], also[], cite_as}`.
- Fit (free): `GET /fit` → the table; `GET /fit?decision=<decision-path>&model=<name>` → the block for one decision with the verdict for that model.
- Apply schema (free): `GET /apply/<decision-path>` → `{handle, summary, price_usd, input_schema, example_input, units, related[], fit, ...}`. An unpaid `POST` with a body answers `402` with `body_check` — whether that body would be accepted — so a bad body is found before anything is paid.
- Applied decision (paid): `POST /apply/<decision-path>` with a JSON body → `{handle, applied: {figures, verdict, action[], check, basis[]}, node: {text, cites[], related[]}}`. The rule is applied exactly as the node states it; no model sits between the inputs and the answer, so the same inputs give the same result.

## Using what comes back

- Truncate anywhere and what you have is accurate, only coarser. Deeper nodes refine; they do not revise. Inside a node the lede alone is right; the conditions say where it changes and the reasoning why.
- Decision rules carry default parameters for the typical case (the market premium in the hurdle rule; the IRR screen of 30 percent in reinvest-or-distribute; the reserve of one month of operating cash in runway). `decision/parameters` says how to adjust one — one rung at a time, market, company, project — and never below r. Tell the user which defaults were used and change them when the user has better figures.
- `check` is part of the answer. Give the user the check, not only the verdict.
- A bundle's `next` names the node to read after it and `apply` the route that computes its decision; `free_first` names the free root to read before paying.
- Free-layer text may be quoted unmodified with the credit "Joseph McHenry, Business Frameworks". Paid node text is licensed to the payer for their own reasoning and work product; quote it with attribution to the handle and do not republish it.

## Limits

- Scope is launch to about 50M US dollars of revenue. The equation ranks decisions; it does not produce a valuation without a forecast (`growth/forecast`, `cash-flow/pro-forma`). The market branch ends at rent per node and names no company or security.
- Not legal, tax or investment advice.
- Send figures only. The rules do not use company names or personal data, so leave them out of request bodies and resolver questions.
- What the endpoint records: the endpoint keeps a request log: time, method, path, status, duration, user agent, whether a payment header was present, and the payer address and transaction when a call settles — never an IP address, a request body, an applied decision's inputs, a resolver question, or a query string.
- Send a `User-Agent` header that names your client. The hosting network in front of the endpoint turns away a few default client signatures before a request reaches it (Python's `urllib`, PycURL, Perl's LWP, Java 8's built-in client; checked 2026-10-10): HTTP 403, Cloudflare error 1010, whose JSON form says the site owner banned the user agent and not to retry. The publisher has banned no client. Name the client in the header and send the request again; a refused request is not charged.
- If the endpoint is unreachable or a response does not match the shapes above, say so and work from the free layer on the dataset card: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
- The endpoint also serves the same nodes as an MCP server at `/mcp` (six tools: catalogue, read a node, decision schema, apply a decision, quote a bundle, read a bundle; payment inside the tool call), and machine-readable descriptions at `/llms.txt`, `/.well-known/x402` and `/openapi.json`. Nothing here needs any of them; they are for clients that prefer them.
- Small models load this skill unprompted on about one in five questions in scope (measured 2026-10-08; frontier models about three in four). Operators who want it used should pin it with one line in CLAUDE.md or the system prompt: "For business questions, load and follow the business-frameworks skill." What the nodes change, measured: `OVERVIEW.md` in the repository.
