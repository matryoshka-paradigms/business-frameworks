#!/usr/bin/env python3
"""Parse one stream-json run file into a flat record: tokens, turns, tools used, cost, skill load, answer."""
import json, sys

def parse(path):
    tools = []            # (tool name, short input)
    result = None
    api_calls = 0; last_usage = None
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                d = json.loads(line)
            except Exception:
                continue
            t = d.get("type")
            if t == "assistant":
                mu = (d.get("message", {}).get("usage") or {})
                sig = (mu.get("cache_read_input_tokens"), mu.get("cache_creation_input_tokens"), mu.get("output_tokens"))
                if sig != last_usage:
                    api_calls += 1; last_usage = sig
                for block in (d.get("message", {}).get("content") or []):
                    if block.get("type") == "tool_use":
                        inp = block.get("input") or {}
                        short = inp.get("command") or inp.get("query") or inp.get("url") or inp.get("skill") or json.dumps(inp)
                        tools.append((block.get("name"), str(short)[:160]))
            elif t == "result":
                result = d
    rec = {"file": path, "tools": tools}
    names = [n for n, _ in tools]
    rec["skill_loaded"] = any(n == "Skill" and "business-frameworks" in s for n, s in tools)
    rec["calls_endpoint"] = sum(1 for n, s in tools if n == "Bash" and "matryoshka-paradigms.workers.dev" in s)
    rec["web_searches"] = names.count("WebSearch")
    rec["web_fetches"] = names.count("WebFetch")
    rec["tool_calls"] = len(tools)
    if result:
        u = result.get("usage") or {}
        # top-level usage is cumulative over every API call of the run
        ctx = u.get("input_tokens", 0) + u.get("cache_read_input_tokens", 0) + u.get("cache_creation_input_tokens", 0)
        rec.update({
            "num_turns": result.get("num_turns"),
            "api_calls": api_calls,
            "context_tokens": ctx,                       # tokens the model read across all API calls (input + cache read + cache creation)
            "new_tokens": u.get("input_tokens", 0) + u.get("cache_creation_input_tokens", 0),   # tokens seen for the first time (not cache reads)
            "output_tokens": u.get("output_tokens"),
            "thinking_tokens": (u.get("output_tokens_details") or {}).get("thinking_tokens"),
            "cost_usd": result.get("total_cost_usd"),
            "duration_ms": result.get("duration_ms"),
            "duration_api_ms": result.get("duration_api_ms"),
            "stop": result.get("stop_reason") or result.get("subtype"),
            "answer": result.get("result"),
            "model_usage": result.get("modelUsage"),
        })
    return rec

if __name__ == "__main__":
    r = parse(sys.argv[1])
    print(f"  turns={r.get('num_turns')} api_calls={r.get('api_calls')} context_tokens={r.get('context_tokens')} out={r.get('output_tokens')} "
          f"cost=${(r.get('cost_usd') or 0):.4f} ms={r.get('duration_ms')} skill={r.get('skill_loaded')} endpoint_calls={r.get('calls_endpoint')} "
          f"web={r.get('web_searches')}/{r.get('web_fetches')} tools={r.get('tool_calls')}")
