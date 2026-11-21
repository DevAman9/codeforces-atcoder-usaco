# codeforces-atcoder-usaco

Personal repo for competitive programming practice in C++.

I'm working through standard techniques using USACO Guide and CSES, and practising unfamiliar problems and contests on AtCoder and Codeforces.

All solutions here are my own attempts (including unfinished or revised ones when useful). I use AI tooling to help with local testing, organisation, and keeping notes tidy, not to write solutions for me.

## Compiling and testing locally

Requires `clang++` (or `g++`) and Python 3. Defaults to C++17:

```bash
python3 scripts/test.py path/to/solution.cpp
python3 scripts/test.py path/to/solution.cpp --std 20 --san
```

Local test cases live under `tests/` matching the solution path. Passing local tests only checks the sample or custom cases, not official judge acceptance.

Notes and session entries are in `notes/learning-log.md`.
