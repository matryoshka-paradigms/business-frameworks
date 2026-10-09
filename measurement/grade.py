#!/usr/bin/env python3
"""Grade every run against the question keys with a Claude grader (headless, JSON out).
Usage: python3 grade.py [--grader sonnet] [--only model/cond ...]
Writes results/grades.json: one record per run with frame/rule/figures/misattribution/cited and a correct flag.
Correct = frame and rule and (figures, when numeric) and no misattribution."""
import json, os, subprocess, sys, glob, tempfile
from summarize_run import parse

HERE = os.path.dirname(os.path.abspath(__file__))

def scrubbed_env():
    """Path, home, proxy and certificate settings only, each read by its literal name. No credential is forwarded;
    the nested Claude Code uses the login stored under HOME."""
    pairs = (
        ("HOME", os.environ.get("HOME")), ("PATH", os.environ.get("PATH")),
        ("HTTPS_PROXY", os.environ.get("HTTPS_PROXY")), ("HTTP_PROXY", os.environ.get("HTTP_PROXY")), ("NO_PROXY", os.environ.get("NO_PROXY")),
        ("https_proxy", os.environ.get("https_proxy")), ("http_proxy", os.environ.get("http_proxy")), ("no_proxy", os.environ.get("no_proxy")),
        ("NODE_EXTRA_CA_CERTS", os.environ.get("NODE_EXTRA_CA_CERTS")), ("SSL_CERT_FILE", os.environ.get("SSL_CERT_FILE")),
        ("REQUESTS_CA_BUNDLE", os.environ.get("REQUESTS_CA_BUNDLE")), ("CURL_CA_BUNDLE", os.environ.get("CURL_CA_BUNDLE")),
        ("ANTHROPIC_BASE_URL", os.environ.get("ANTHROPIC_BASE_URL")), ("TERM", os.environ.get("TERM")), ("LANG", os.environ.get("LANG")),
    )
    return {name: value for name, value in pairs if value}
GRADER = "sonnet"
if "--grader" in sys.argv:
    GRADER = sys.argv[sys.argv.index("--grader") + 1]

RUBRIC = """You are grading an answer to a business question against an answer key. The key states the framework's frame, rule, figures and the misattributions to avoid. Judge only against the key; do not reward eloquence.
Return ONLY a JSON object with these keys:
- "frame": 1 if the answer identifies the decision in the key's terms (the right test or rule to apply), else 0.
- "rule": 1 if the answer applies the key's rule correctly (order of steps, thresholds, what is compared with what), else 0. A partially correct rule with a contradicted step is 0.
- "figures": 1 if every figure the key requires appears and is right (tolerance: rounding), 0 if any required figure is wrong or missing, null if the key requires no figures.
- "misattribution": 1 if the answer presents a figure, threshold or rule as the framework's (or as "the rule", "the standard") that the key says is not the framework's, else 0. A figure the answer labels as its own assumption is 0.
- "cited": 1 if the answer cites a business-frameworks handle (business-frameworks/<path>@<version>) or names Business Frameworks / Joseph McHenry as the source, else 0.
- "note": one sentence on the decisive point.
"""

def grade_one(q, answer):
    prompt = (RUBRIC + "\n\nQUESTION:\n" + q["question"] + "\n\nANSWER KEY (kind: " + q["kind"] + "):\n" + q["key"]
              + "\n\nANSWER TO GRADE:\n" + (answer or "(empty)") + "\n\nJSON:")
    keep = scrubbed_env()
    with tempfile.TemporaryDirectory() as wd:
        out = subprocess.run(["claude", "-p", prompt, "--model", GRADER, "--output-format", "json", "--max-turns", "1",
                              "--no-session-persistence", "--setting-sources", "project", "--disallowedTools", "Projects", "Bash", "WebSearch", "WebFetch", "Read", "Glob", "Grep"],
                             cwd=wd, env=keep, capture_output=True, text=True, timeout=300)
    try:
        d = json.loads(out.stdout)
        txt = d.get("result", "")
        s = txt[txt.find("{"): txt.rfind("}") + 1]
        g = json.loads(s)
        g["grader_cost_usd"] = d.get("total_cost_usd")
        return g
    except Exception as e:
        return {"error": str(e), "raw": out.stdout[-500:], "stderr": out.stderr[-300:]}

def main():
    qs = {q["id"]: q for q in json.load(open(os.path.join(HERE, "questions.json")))}
    gpath = os.path.join(HERE, "results", "grades.json")
    grades = json.load(open(gpath)) if os.path.exists(gpath) else {}
    only = sys.argv[sys.argv.index("--only") + 1:] if "--only" in sys.argv else None
    for f in sorted(glob.glob(os.path.join(HERE, "results", "*", "*", "*.jsonl"))):
        model, cond, fn = f.split(os.sep)[-3:]
        qid = fn[:-6]
        key = f"{model}/{cond}/{qid}"
        if only and not any(key.startswith(o) for o in only):
            continue
        if key in grades and "error" not in grades[key]:
            continue
        r = parse(f)
        if not r.get("answer"):
            grades[key] = {"error": "no answer"}; continue
        g = grade_one(qs[qid], r["answer"])
        q = qs[qid]
        if "error" not in g:
            g["correct"] = bool(g.get("frame") and g.get("rule") and (g.get("figures") in (1, None)) and not g.get("misattribution"))
        g.update({"model": model, "cond": cond, "qid": qid, "kind": q["kind"], "decision": q["decision"]})
        grades[key] = g
        json.dump(grades, open(gpath, "w"), indent=1)
        print(key, {k: g.get(k) for k in ("frame", "rule", "figures", "misattribution", "cited", "correct")}, "|", g.get("note", g.get("error")))

if __name__ == "__main__":
    main()
