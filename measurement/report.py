#!/usr/bin/env python3
"""Aggregate runs + grades into the measurement table (markdown) and a JSON summary.
Usage: python3 report.py > results/report.md"""
import json, os, glob, statistics as st
from summarize_run import parse

HERE = os.path.dirname(os.path.abspath(__file__))
gpath = os.path.join(HERE, "results", "grades.json")
grades = json.load(open(gpath)) if os.path.exists(gpath) else {}
qs = {q["id"]: q for q in json.load(open(os.path.join(HERE, "questions.json")))}

rows = []
for f in sorted(glob.glob(os.path.join(HERE, "results", "*", "*", "*.jsonl"))):
    model, cond, fn = f.split(os.sep)[-3:]
    qid = fn[:-6]
    r = parse(f)
    if r.get("cost_usd") is None:
        continue
    g = grades.get(f"{model}/{cond}/{qid}", {})
    rows.append({"model": model, "cond": cond, "qid": qid, "kind": qs[qid]["kind"], **{k: r.get(k) for k in (
        "num_turns", "api_calls", "context_tokens", "new_tokens", "output_tokens", "thinking_tokens", "cost_usd", "duration_ms",
        "skill_loaded", "calls_endpoint", "web_searches", "web_fetches", "tool_calls")},
        "correct": g.get("correct"), "frame": g.get("frame"), "rule": g.get("rule"), "figures": g.get("figures"),
        "misattribution": g.get("misattribution"), "cited": g.get("cited")})

def mean(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return st.mean(xs) if xs else None
def pct(xs):
    xs = [x for x in xs if x is not None]
    return (100.0 * sum(1 for x in xs if x) / len(xs)) if xs else None

summary = {}
groups = sorted({(r["model"], r["cond"]) for r in rows})
print("| Model | Condition | n | Correct | Rule right | Misattrib. | Cited | API calls | Context tokens read | New tokens | Output tokens | Endpoint calls | Web searches | Cost per answer | Seconds |")
print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for m, c in groups:
    g = [r for r in rows if r["model"] == m and r["cond"] == c]
    graded = [r for r in g if r["correct"] is not None]
    s = {"n": len(g), "graded": len(graded), "correct_pct": pct([r["correct"] for r in g]), "rule_pct": pct([r["rule"] for r in g]),
         "misattrib_pct": pct([r["misattribution"] for r in g]), "cited_pct": pct([r["cited"] for r in g]),
         "api_calls": mean([r["api_calls"] for r in g]), "context_tokens": mean([r["context_tokens"] for r in g]),
         "new_tokens": mean([r["new_tokens"] for r in g]), "output_tokens": mean([r["output_tokens"] for r in g]),
         "endpoint_calls": mean([r["calls_endpoint"] for r in g]), "web_searches": mean([r["web_searches"] for r in g]),
         "cost_usd": mean([r["cost_usd"] for r in g]), "seconds": mean([r["duration_ms"] / 1000 for r in g if r["duration_ms"]])}
    summary[f"{m}/{c}"] = s
    f = lambda x, d=0: ("—" if x is None else (f"{x:.{d}f}"))
    print(f"| {m} | {c} | {s['n']} ({s['graded']} graded) | {f(s['correct_pct'])}% | {f(s['rule_pct'])}% | {f(s['misattrib_pct'])}% | {f(s['cited_pct'])}% | {f(s['api_calls'],1)} | {f(s['context_tokens'])} | {f(s['new_tokens'])} | {f(s['output_tokens'])} | {f(s['endpoint_calls'],1)} | {f(s['web_searches'],1)} | ${f(s['cost_usd'],4)} | {f(s['seconds'],1)} |")

print("\nPer question (correct: with / without):")
for m in sorted({r["model"] for r in rows}):
    print(f"\n{m}:")
    for qid in qs:
        w = next((r for r in rows if r["model"] == m and r["cond"] == "with" and r["qid"] == qid), None)
        wo = next((r for r in rows if r["model"] == m and r["cond"] == "without" and r["qid"] == qid), None)
        if not (w or wo):
            continue
        fmt = lambda r: "—" if r is None or r["correct"] is None else ("✓" if r["correct"] else "✗")
        print(f"- {qid} ({qs[qid]['kind']}, {qs[qid]['decision']}): with {fmt(w)} / without {fmt(wo)}"
              + (f" · with: {w['api_calls']} calls, {w['context_tokens']} ctx, ${w['cost_usd']:.4f}" if w else "")
              + (f" · without: {wo['api_calls']} calls, {wo['context_tokens']} ctx, ${wo['cost_usd']:.4f}" if wo else ""))
json.dump({"summary": summary, "rows": rows}, open(os.path.join(HERE, "results", "summary.json"), "w"), indent=1)
