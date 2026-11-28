# Learning log

Short notes on what I worked on, what broke, and what I need to revisit.

## 2026-11-23

First proper C++ session (~2 hours). Got official ACs on three problems, though none were completely unaided yet.

- CSES 1621 (Distinct Numbers) — [submission](https://cses.fi/problemset/result/19423960/), AC. Looked up the structure since I wasn't sure how to set up vector input on my first problem. First CSES submission failed to compile because I only had `#include <iostream>` (macOS Clang compiled it anyway, GCC didn't). Added `<vector>` and `<algorithm>` and it passed.
- AtCoder ABC061 B (Counting Roads) — [submission](https://atcoder.jp/contests/abc061/submissions/81039520), AC (1 ms). Used a quick syntax reference for reading pairs and sizing a vector, then wrote the logic myself. Initially thought I'd need to store the cities and roads, then realised I just need to increment counts for both endpoints as each road comes in (O(N + M)).
- CSES 1646 (Static Range Sum Queries) — [submission](https://cses.fi/problemset/result/19424196/), AC. Wrote the first version from scratch without looking up code, then fixed three bugs caught by local sanitizer tests and hints: `int` overflow on large sums (switched to `long long`), out-of-bounds access on 1-based queries (resized `num` and `sums` to `n + 1`), and subtracting `sums[a]` instead of `sums[a - 1]`. Took a bit to see why `a - 1` works, then clicked — you only want to remove elements strictly before `a`.

Next session: try an unseen prefix-sum or sorting problem cold without syntax hints.

## 2026-11-28

First cold Codeforces session (~2 hours active, 12:09–14:13). Solved a 900 and a 1000 without any external help or syntax lookups, then hit a wall on an 1100.

- Codeforces 580A (Kefa and First Steps, 900) — unseen, solved cold in ~22 min. Passed 4/4 local tests with ASan/UBSan (O(n) time, O(1) space). First test run failed only because I'd left a debug `cout` inside the loop. Official judge submission not yet recorded.
- Codeforces 339B (Xenia and Ringroad, 1000) — unseen, worked out the circular wrap-around maths completely solo (~55 min, O(m) time, O(1) space). Passed 3/3 local tests, then a 60k-task stress test caught `int` overflow on `time` (`2147399999 + 99999`). Changed `time` to `long long` and passed the stress test cleanly. Official judge submission not yet recorded.
- Codeforces 1914C (Quests, 1100) — unfinished cold attempt (~30 min). Got the multi-testcase and `vector<pair<int, int>>` input set up cleanly without looking up syntax, then got stuck trying to simulate moves step by step with a `done` array. Felt like I'm fine with maths/logical scan problems, but weak at greedy — need to actually study greedy framing before retrying this one.

Next session: learn basic greedy framing (USACO Bronze Introduction to Greedy Algorithms), upsolve CF 1914C, and try a fresh unseen greedy CF 1000–1100 cold. Also submit 580A and 339B on Codeforces if not submitted yet.
