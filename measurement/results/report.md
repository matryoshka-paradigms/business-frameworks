| Model | Condition | n | Correct | Rule right | Misattrib. | Cited | API calls | Context tokens read | New tokens | Output tokens | Endpoint calls | Web searches | Cost per answer | Seconds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| haiku | forced | 20 (20 graded) | 45% | 50% | 15% | 90% | 4.0 | 79638 | 12479 | 2585 | 2.0 | 0.0 | $0.0045 | 16.2 |
| haiku | paid | 20 (20 graded) | 65% | 75% | 15% | 95% | 3.5 | 72035 | 13994 | 2912 | 0.7 | 0.0 | $0.0048 | 16.4 |
| haiku | with | 20 (20 graded) | 15% | 30% | 30% | 20% | 1.4 | 24208 | 7325 | 2091 | 0.2 | 0.0 | $0.0027 | 12.5 |
| haiku | without | 20 (20 graded) | 10% | 15% | 20% | 0% | 1.1 | 17815 | 7006 | 1778 | 0.0 | 0.0 | $0.0024 | 10.5 |
| opus | forced | 8 (8 graded) | 25% | 50% | 38% | 100% | 4.0 | 75933 | 12063 | 1941 | 2.0 | 0.0 | $0.1481 | 24.2 |
| opus | paid | 8 (8 graded) | 62% | 62% | 12% | 100% | 4.0 | 76608 | 12652 | 1839 | 0.0 | 0.0 | $0.1508 | 22.9 |
| opus | with | 8 (8 graded) | 50% | 75% | 25% | 75% | 3.5 | 65058 | 9955 | 1940 | 1.5 | 0.0 | $0.1296 | 23.3 |
| opus | without | 8 (8 graded) | 25% | 25% | 38% | 0% | 1.0 | 15004 | 6876 | 1359 | 0.0 | 0.0 | $0.0838 | 18.1 |

Per question (correct: with / without):

haiku:
- q01 (qualitative, value/decide/reinvest-or-distribute): with ✗ / without ✗ · with: 4 calls, 80247 ctx, $0.0042 · without: 1 calls, 16131 ctx, $0.0020
- q02 (qualitative, cash-flow/decide/runway): with ✗ / without ✗ · with: 1 calls, 17038 ctx, $0.0020 · without: 1 calls, 16130 ctx, $0.0019
- q03 (qualitative, risk/decide/hurdle): with ✗ / without ✗ · with: 1 calls, 17038 ctx, $0.0023 · without: 1 calls, 16128 ctx, $0.0023
- q04 (qualitative, risk/decide/concentration): with ✗ / without ✗ · with: 1 calls, 17036 ctx, $0.0023 · without: 1 calls, 16126 ctx, $0.0021
- q05 (qualitative, growth/decide/pace): with ✗ / without ✗ · with: 1 calls, 17035 ctx, $0.0024 · without: 2 calls, 32549 ctx, $0.0023
- q06 (qualitative, growth/decide/price): with ✗ / without ✗ · with: 1 calls, 17031 ctx, $0.0023 · without: 1 calls, 16125 ctx, $0.0021
- q07 (qualitative, cash-flow/decide/owner-pay): with ✗ / without ✗ · with: 1 calls, 17044 ctx, $0.0026 · without: 1 calls, 16136 ctx, $0.0022
- q08 (qualitative, growth/decide/adjacency): with ✗ / without ✗ · with: 4 calls, 78954 ctx, $0.0041 · without: 1 calls, 16129 ctx, $0.0021
- q09 (numeric, cash-flow/decide/runway): with ✗ / without ✗ · with: 1 calls, 17165 ctx, $0.0038 · without: 1 calls, 16259 ctx, $0.0037
- q10 (qualitative, value/decide/build-or-run-for-cash): with ✗ / without ✗ · with: 2 calls, 34500 ctx, $0.0024 · without: 2 calls, 32602 ctx, $0.0023
- n01 (numeric, value/decide/reinvest-or-distribute): with ✗ / without ✓ · with: 1 calls, 17167 ctx, $0.0026 · without: 1 calls, 16259 ctx, $0.0023
- n02 (numeric, cash-flow/decide/cash-cycle): with ✗ / without ✗ · with: 1 calls, 17085 ctx, $0.0027 · without: 1 calls, 16181 ctx, $0.0025
- n03 (numeric, cash-flow/decide/runway): with ✗ / without ✗ · with: 1 calls, 17205 ctx, $0.0036 · without: 1 calls, 16299 ctx, $0.0031
- n04 (numeric, cash-flow/decide/owner-pay): with ✓ / without ✓ · with: 1 calls, 17075 ctx, $0.0020 · without: 1 calls, 16163 ctx, $0.0019
- n05 (numeric, risk/decide/hurdle): with ✓ / without ✗ · with: 1 calls, 17097 ctx, $0.0020 · without: 1 calls, 16189 ctx, $0.0018
- n06 (numeric, risk/decide/concentration): with ✗ / without ✗ · with: 1 calls, 17072 ctx, $0.0023 · without: 1 calls, 16166 ctx, $0.0042
- n07 (numeric, growth/decide/pace): with ✗ / without ✗ · with: 1 calls, 17085 ctx, $0.0025 · without: 1 calls, 16177 ctx, $0.0023
- n08 (numeric, growth/decide/price): with ✓ / without ✗ · with: 1 calls, 17099 ctx, $0.0026 · without: 1 calls, 16195 ctx, $0.0024
- n09 (numeric, growth/decide/adjacency): with ✗ / without ✗ · with: 1 calls, 17104 ctx, $0.0025 · without: 1 calls, 16196 ctx, $0.0025
- n10 (numeric, value/decide/build-or-run-for-cash): with ✗ / without ✗ · with: 1 calls, 17073 ctx, $0.0024 · without: 1 calls, 16165 ctx, $0.0022

opus:
- q01 (qualitative, value/decide/reinvest-or-distribute): with ✗ / without ✗ · with: 4 calls, 74865 ctx, $0.1393 · without: 1 calls, 14957 ctx, $0.0657
- q03 (qualitative, risk/decide/hurdle): with ✓ / without ✗ · with: 4 calls, 74724 ctx, $0.1428 · without: 1 calls, 14952 ctx, $0.0737
- q04 (qualitative, risk/decide/concentration): with ✗ / without ✗ · with: 5 calls, 94276 ctx, $0.1450 · without: 1 calls, 14952 ctx, $0.0659
- q08 (qualitative, growth/decide/adjacency): with ✓ / without ✗ · with: 4 calls, 75781 ctx, $0.1513 · without: 1 calls, 14953 ctx, $0.0744
- n01 (numeric, value/decide/reinvest-or-distribute): with ✓ / without ✓ · with: 1 calls, 15989 ctx, $0.0775 · without: 1 calls, 15081 ctx, $0.0710
- n03 (numeric, cash-flow/decide/runway): with ✗ / without ✗ · with: 1 calls, 16029 ctx, $0.1037 · without: 1 calls, 15121 ctx, $0.0991
- n06 (numeric, risk/decide/concentration): with ✓ / without ✗ · with: 5 calls, 93829 ctx, $0.1322 · without: 1 calls, 14992 ctx, $0.1424
- n09 (numeric, growth/decide/adjacency): with ✗ / without ✓ · with: 4 calls, 74970 ctx, $0.1447 · without: 1 calls, 15020 ctx, $0.0783
