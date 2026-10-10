---
description: "Not a business question. The skill should stay unloaded even with the pin in place."
tags: [scope]
max_turns: 12
allowed_tools: [Read, Glob, Grep, Skill]
append_system_prompt: "If the business-frameworks skill is installed, load and follow it for business questions."
---

Write a Python function that removes duplicate rows from a CSV file, keeping the first occurrence of each row.
