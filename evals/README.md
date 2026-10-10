# Evals — the free layer, with the plugin and without

A suite for `claude plugin eval` (Claude Code 2.1.269 or later). Each case is run with this plugin loaded and again with no plugin, three times each (ten for one guard case). The table at the end shows both scores and the difference.

## What it tests, and what it does not

- **It tests the free layer:** the six free nodes and the skill's conduct — cite the handle, name the paid node that goes deeper and its price, never claim a purchase, stay inside the stated scope.
- **It does not test the paid nodes.** A run loads this plugin and nothing else: there is no wallet in it, and there is no paid text in this repository. Every scored grader rests on text anyone can read for nothing — a free node, `SKILL.md`, or the question itself. The table under "Where each grader comes from" names the source case by case.
- **It does not show that the framework's rules are right.** A pass means the answer agrees with the framework's free layer, as judged by graders the publisher wrote. The sources behind the rules are cited on the nodes.

## Run it

From the repository root:

```bash
claude plugin eval . \
  --model haiku --judge-model haiku \
  --allow-tools "WebFetch(domain:business-frameworks.matryoshka-paradigms.workers.dev)"
```

For an installed copy, replace `.` with `business-frameworks@matryoshka-paradigms`.

- **The grant matters.** Without it the agent cannot read the endpoint and the plugin arm has only `SKILL.md` to go on.
- **Every run is a model call on your own account.** 21 cases at 3 runs and one at 10, in 2 arms, is 146 runs, plus judge calls. On 2026-10-09 a full pass cost about $0.60 at list prices on Claude Haiku 5.5 with a Haiku judge.
- **The exit code is 1 unless every case scores 1.0** (the tool's default threshold). This suite is a measurement, not a gate; add `--threshold 0` if only the table is wanted.
- **Pin both models** so two runs can be compared. `--model opus` gives the frontier-model column; `--judge-model sonnet` gives a stronger judge at a higher cost.
- Results are written to `evals/results/`, which is in `.gitignore`.

## The three groups

| Group | Cases | Pin in the system prompt | What is scored |
|---|---|---|---|
| `pinned/` | 14 | yes | The answer. `frame` and `verdict` graders are rubrics read by a judge model; `figure-*` graders are regular expressions on a figure that follows from the question's own numbers and a free node's definition. |
| `unpinned/` | 4 | no | Whether the skill loads on its own, on a question in scope phrased the way a user would type it. |
| `scope/` | 4 | yes | Guards: a company above the document's size limit (ten runs per arm), a tax question, a spending approval with no wallet present, a request that is not a business question. The expected result is the same score in both arms. |

The pin is one line: "If the business-frameworks skill is installed, load and follow it for business questions." It stands for what an operator adds to `CLAUDE.md` or the system prompt. It sits in both arms; in the no-plugin arm there is no such skill, so the line does nothing there.

**Indicators.** In the plugin arm each pinned case also reports seven checks that are shown but not scored, since they cannot pass without the plugin: `skill-loaded`, `read-free-layer` (a free node was fetched), `asked-fit` (the free fit block was requested), `cites-handle`, `names-a-price` (the reply says what a deeper node costs), `no-paid-claim` (the reply does not claim a purchase; a judge rubric) and `skill-text-intact` (the skill's payment cap reached the model as written).

## Where each grader comes from

| Case | Scored grader | Rests on |
|---|---|---|
| `q01-second-location-or-pay-out` | `frame` | `business-frameworks/value@1.0`: value is created only when capital inside the business earns more than it could elsewhere at the same risk |
| `q02-profit-but-no-payroll` | `frame` | `business-frameworks/cash-flow@1.0`: profit is not cash |
| `q03-discount-rate-family-manufacturer` | `frame` | `business-frameworks/risk@1.0`: the market-built rate, the concentrated owner's floor, the survival probability kept apart from the rate below $5M |
| `q05-grow-forty-percent` | `frame` | `business-frameworks/growth@1.0`: the ceiling on growth a business can fund itself |
| `q07-owner-sixty-hours` | `frame` | `business-frameworks/cash-flow@1.0`, sub-$1M band: cash flow after the owner's market wage |
| `q08-unrelated-acquisition` | `frame` | `business-frameworks/growth@1.0`, $25–50M band: add only what the core already touches |
| `q10-build-to-sell-or-income` | `frame` | `business-frameworks/value@1.0`, sub-$1M band: a buyer pays only to the degree the business runs without its owner; a short-lived opportunity or a durable position |
| `n01-four-uses-of-cash` | `figure-reinvested`, `figure-distributed` | the question's figures and `value@1.0` |
| `n02-cash-cycle-days` | `figure-cycle-days` | `cash-flow@1.0`, $1–5M band: inventory days plus receivable days less supplier-credit days |
| `n04-owner-pay` | `figure-wage`, `figure-after-wage` | `cash-flow@1.0`, sub-$1M band |
| `n05-hurdle-rate` | `figure-rate`, `final-rate` | `risk@1.0`: a risk-free rate plus a scaled premium; for a diversified owner that is the number |
| `n07-outside-capital` | `verdict` | `growth@1.0`: growth adds value only when the capital it uses earns more than r |
| `n09-solar-installer` | `verdict` | `growth@1.0`, $25–50M band |
| `n10-not-durable` | `verdict` | `value@1.0`, sub-$1M band |
| `scope/*` | `scope-respected`, `not-tax-advice`, `no-paid-claim`, `no-key-request`, `skill-not-loaded` | `SKILL.md`: the scope and the payment rules |

The questions are the twenty in `measurement/questions.json`. Six of them (q04, q06, q09, n03, n06, n08) have no answer grader here, because what decides them is stated in paid nodes and not in the free layer; four of the six serve as the `unpinned/` cases.

## Reading the result

- **A difference on one case is three runs against three.** Read the suite as a whole, and read the failed runs in the report before trusting a number.
- **Where the baseline already passes, the plugin has nothing to add.** The figure cases are arithmetic on the question's own numbers; a capable model gets them without help. They are here to show that the plugin does no harm.
- **The agent reads nodes through `WebFetch`,** which hands it a summary of the page and not the page itself.
- **The judge is a model reading a rubric the publisher wrote.** Each rubric is in the case's `graders/` folder; the judge's votes are in the report. Two judge models do not always agree on the same answer, so pin the judge, and re-run a case with a second judge before leaning on it.
- **The plugin arm reads a live endpoint.** A deploy between two passes changes what the agent reads; note the endpoint's `worker_version` (`GET /health`) with each result.
- **The model matters.** Small models load the skill on their own far less often than frontier models, which is what the `unpinned/` cases measure.
