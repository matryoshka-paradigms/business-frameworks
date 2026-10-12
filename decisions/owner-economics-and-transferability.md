# Owner economics and transferability

*Business Frameworks · a decision family · document version 1.2 · Joseph McHenry*

> "I draw what is left at the end of the month. After a replacement wage for my own hours, is there a business here — and should I be building it to sell or running it for cash?"

Below about $1M of revenue the owner and the business are not yet separate things: the tax return's profit includes the owner's unpaid labour, and a buyer will pay only for the part that runs without the owner in the building. This family holds the two decisions that make the separation explicit — whether the business earns anything once the owner is paid a market wage, and whether its cash should be spent building something transferable or taken out as income. The free layer that frames them (the value term, the cash-flow term and the sub-$1M reading of each) is on the canonical page at no cost.

## The decisions

**Pay the owner first** — `business-frameworks/cash-flow/decide/owner-pay@1.2`
*You send:* the hours the owner works in a year; the hourly wage the business would have to pay someone else to do that work (your figure, from your labour market); the year's cash flow before any owner wage; and, if you like, the distributions the owner took. *You get back:* the cash flow after a market wage, whether the business is a job that pays less than the job market would, and what the distributions did to the balance sheet. *Price:* $0.05 to read the node; $0.05 to apply it. *Bundle:* `decide/owner-pay` — the decision in full with the cash-flow why node in its short form — $0.07; $0.10 with the under-$1M scale band.

**Build for transfer or run for cash** — `business-frameworks/value/decide/build-or-run-for-cash@1.2`
*You send:* your own judgment of whether the position is durable (a competitor could not copy it within a year or two) or a window that will close; the share of revenue earned without the founder doing the work; the share of revenue that repeats without being sold again; and the same two shares a quarter earlier if you track them. *You get back:* build-for-transfer or run-for-cash, the actions that go with the verdict, and a quarterly check on the two shares. The endpoint applies the rule to the judgment you send; it does not assess the position for you. *Price:* $0.05 to read; $0.05 to apply. *Bundle:* `decide/build-or-run-for-cash` — the decision in full with the value why node in its short form — $0.07; $0.10 with the under-$1M or the $5–25M band.

Every figure is the caller's own; nothing is looked up. The rule runs exactly as the node states it and the node's text comes back with the result. A bundle that lists a price "with a band" carries one for the sizes the catalogue names. Payment is per call, USDC on Base over x402, no account.

## A worked example, from the free layer alone

An owner of a machine shop works 2,600 hours a year — fifty hours a week — and the return shows $95,000 of profit, of which $80,000 was taken as distributions. The sub-$1M condition under the cash-flow term on the canonical page says the number that matters is what remains after the owner is paid a market wage for the work the owner does. A shop foreman who could run those hours costs about $45 an hour locally: 2,600 × $45 = $117,000. Cash flow after a market wage is $95,000 − $117,000 = −$22,000. The business is not making money; it is a job that pays $22,000 a year less than the same hours would earn elsewhere, and the $80,000 of distributions came out of a business that earned nothing after the wage. That arithmetic is free. What the applied decision adds is the verdict stated in the rule's terms, what the distributions did to the balance, and the action order; the transferability decision then says whether the next year's cash should buy founder-free revenue — a second estimator, a documented quoting process — or be taken as income while the window lasts.

## Before you pay

- The second check on the canonical page — divide the year's cash flow by the capital employed and compare it with r — is free, and the sub-$1M condition under the value term says what a buyer pays for at this size.
- The input schema for each decision, with an example body, is free at `GET https://business-frameworks.matryoshka-paradigms.workers.dev/apply/<decision>`.
- A quote for the bundle a question needs is free and deterministic: `POST …/resolve` with the question and your revenue — or name the decision; a question that carries both of this family's decisions is best asked as two.
- The measured record for each decision — how often a model stated the rule with no framework, with the free layer and with the node, by model — is free at `GET …/fit?decision=<decision>&model=<model>`; a pilot of one run per question, labelled as such.

## Not for

Market data, tax or law, industry playbooks, businesses above about $50M in revenue, or long multi-step tasks. Whether the owner should form a separate legal entity is a different question from whether the business earns anything after the owner's wage; the canonical page says so, and this document gives no legal advice.

## Sources this family draws on

Zook, C. and Allen, J., "Growth Outside the Core", *Harvard Business Review*, December 2003 · Churchill, N. and Mullins, J., "How Fast Can Your Company Afford to Grow?", *Harvard Business Review*, May 2001 · Stancill, J., "How Much Money Does Your New Venture Need?", *Harvard Business Review*, May–June 1986 · Bruner, R., *Applied Mergers and Acquisitions*, Wiley, 2004, ch. 3 · Zook, C. and Allen, J., *Profit from the Core*, Harvard Business Press, 2010, ch. 2 · Ruback, R., "Capital Cash Flows: A Simple Approach to Valuing Risky Cash Flows", *Financial Management*, Summer 2002.

## Cite

McHenry, J. (2026). *Business Frameworks*, document version 1.2, `business-frameworks/<handle>@1.2`. https://huggingface.co/datasets/Matryoshka-Paradigms/business-frameworks

*If this page helped, a like on the dataset's page on Hugging Face is how the next reader finds it.*
