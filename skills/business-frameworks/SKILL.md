---
name: business-frameworks
description: Operating judgement for a business from launch to about $50M revenue, as short versioned decision frameworks built on V = CF/(r − g). Use when the user runs or advises a small or mid-sized business and has to decide something about value, cash flow, cost of capital or growth — reinvest or distribute, owner pay, the cash cycle, runway, a hurdle rate, customer or supplier concentration, growth pace, a price, an adjacency or acquisition. The top layer is free. Deeper nodes, and decisions applied to the user's own numbers, cost $0.02–$0.05 each over x402 (USDC on Base) and need the user's approval before any payment. Not for legal, tax or investment advice, and not for businesses above $50M revenue.
license: MIT for the files in this repository (this skill, its references, the manifest and the README); free-layer text quoted from the dataset card CC-BY-ND-4.0; paid node text all rights reserved (see LICENSE.md)
compatibility: Needs outbound HTTPS to business-frameworks.matryoshka-paradigms.workers.dev. The free layer needs nothing else. Paid calls need an x402 client and a wallet holding USDC on Base, both supplied and controlled by the user.
metadata:
  author: Joseph McHenry
  skill-version: "0.1"
  product-version: "1.0"
  homepage: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
---

# Business Frameworks

A layered document of operating judgement by Joseph McHenry. Every node has a handle `business-frameworks/<path>@<version>`, a token count and a price. One objective sits at the top, V = CF/(r − g): value equals cash flow divided by the cost of capital less long-term growth. Each branch below it (value, cash-flow, risk, growth) descends from the why, to the scale band, to the decision.

This skill ships no code. It tells you which URL to call, what the call costs and when to stop.

Base URL: `https://business-frameworks.matryoshka-paradigms.workers.dev`

## What is free and what is paid

| Layer | What | Nodes | Cost |
|---|---|---|---|
| 0–1 | The equation, the four terms, the fifteen-second definition | 6 | free |
| 2 | Why-nodes, scale-band nodes, tools (pro forma, forecast, self-financeable growth) | 16 | $0.02–$0.03 each |
| 3 | Decision nodes: inputs, rule, action, check | 10 | $0.05 each |
| apply | A decision node's rule run on the user's numbers | 10 routes | $0.05 each |

The live catalogue is the authority on handles, token counts and prices: `GET /catalogue` (free JSON). `references/handles.md` is a copy for orientation and may be older.

## Steps

1. **Start free.** `GET /node/equation`, then the term the question turns on: `/node/value`, `/node/cash-flow`, `/node/risk`, `/node/growth` (and `/node/value/15s`). Each response has `text`, `cites`, and `children` with the handles one level down. Often this is enough to frame the answer; say so and stop.
2. **Place the business in a scale band** by annual revenue: sub-$1M, $1–5M, $5–25M, $25–50M. If revenue is unknown, ask. Above $50M, say the document is out of scope.
3. **Pick the smallest descent** that answers the question (table below). One node is the normal purchase. Do not buy a branch.
4. **If the user has numbers and the question is one of the ten decisions, use the apply route.** `GET /apply/<decision-path>` returns the input schema and an example input, free. Build the body from the user's figures, check it against the schema yourself, then `POST` it.
5. **Before any paid call, follow the payment rules below.**
6. **Answer with the handle.** Cite `business-frameworks/<path>@<version>` beside each point you take from a node, pass on the node's own citations, and say which calls were paid and what was spent.

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
| Turn a forecast into a value, or build the forward view | `growth/forecast`, `cash-flow/pro-forma` | tool |
| How does the answer change at our size | `<term>/band/<band>` from the catalogue | scale band |

## Payment rules

Paid routes answer `402` with a `PAYMENT-REQUIRED` header (base64 JSON). The request is repeated with a `PAYMENT-SIGNATURE` header produced by the user's x402 client. No account, no API key.

- **Approval first.** Pay only if the user has approved this call, or has set a standing limit that covers it. State the handle and the price before paying.
- **Check the terms in the 402 before signing.** All four must hold; if any fails, do not pay and tell the user what differed:
  - network `eip155:8453` (Base mainnet);
  - asset USDC, contract `0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913`;
  - pay-to `0xbBaCd5111E0Ca3a52DdAA39D4723Cf75C1A75D91`, the same address as `product.pay_to` in the catalogue;
  - amount equal to the catalogue price for that handle and never above $0.10 (100000 base units).
- **Set the client's per-payment cap** to $0.10 or lower where the client has one.
- **No wallet, no purchase.** If no x402 client is available, stop at the free layer and the free schema. Tell the user which handle would answer the question and what it costs. Never ask for, read or store a private key or recovery phrase.
- **One call, one charge.** Check an apply body against `input_schema` before paying. Do not repeat a paid call for the same question; reuse the response. A body that fails the schema is answered `400` with the schema and is not charged (the payment is verified but never settled); the signature is still spent, so check first.

## Shapes

- Node: `GET /node/<path>` → `{handle, title, layer, tokens, text, cites[], children[], ...}`.
- Apply schema (free): `GET /apply/<decision-path>` → `{handle, summary, price_usd, input_schema, example_input, ...}`.
- Applied decision (paid): `POST /apply/<decision-path>` with a JSON body → `{handle, applied: {figures, verdict, action[], check, basis[]}, node: {text, cites[]}}`. The rule is applied exactly as the node states it; no model sits between the inputs and the answer, so the same inputs give the same result.

## Using what comes back

- Truncate anywhere and what you have is accurate, only coarser. Deeper nodes refine; they do not revise.
- Decision rules carry default parameters for the typical case (for example the market premium in the hurdle rule). Tell the user which defaults were used and change them when the user has better figures.
- `check` is part of the answer. Give the user the check, not only the verdict.
- Free-layer text may be quoted unmodified with the credit "Joseph McHenry, Business Frameworks". Paid node text is licensed to the payer for their own reasoning and work product; quote it with attribution to the handle and do not republish it.

## Limits

- Scope is launch to about $50M revenue. The equation ranks decisions; it does not produce a valuation without a forecast (`growth/forecast`, `cash-flow/pro-forma`).
- Not legal, tax or investment advice.
- Send figures only. The rules do not use company names or personal data, so leave them out of request bodies.
- If the endpoint is unreachable or a response does not match the shapes above, say so and work from the free layer on the dataset card: https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks
