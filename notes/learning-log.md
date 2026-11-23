# Learning log

Short notes on what I worked on, what broke, and what I need to revisit.

## 2026-11-23

First proper C++ session (~2 hours). Got official ACs on three problems, though none were completely unaided yet.

- CSES 1621 (Distinct Numbers) — [submission](https://cses.fi/problemset/result/19423960/), AC. Looked up the structure since I wasn't sure how to set up vector input on my first problem. First CSES submission failed to compile because I only had `#include <iostream>` (macOS Clang compiled it anyway, GCC didn't). Added `<vector>` and `<algorithm>` and it passed.
- AtCoder ABC061 B (Counting Roads) — [submission](https://atcoder.jp/contests/abc061/submissions/81039520), AC (1 ms). Used a quick syntax reference for reading pairs and sizing a vector, then wrote the logic myself. Initially thought I'd need to store the cities and roads, then realised I just need to increment counts for both endpoints as each road comes in (O(N + M)).
- CSES 1646 (Static Range Sum Queries) — [submission](https://cses.fi/problemset/result/19424196/), AC. Wrote the first version from scratch without looking up code, then fixed three bugs caught by local sanitizer tests and hints: `int` overflow on large sums (switched to `long long`), out-of-bounds access on 1-based queries (resized `num` and `sums` to `n + 1`), and subtracting `sums[a]` instead of `sums[a - 1]`. Took a bit to see why `a - 1` works, then clicked — you only want to remove elements strictly before `a`.

Next session: try an unseen prefix-sum or sorting problem cold without syntax hints.
