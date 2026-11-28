// Codeforces 1914C - Quests
// https://codeforces.com/problemset/problem/1914/C

#include <iostream>
#include <vector>
using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    // n quests
    // 1st is always available
    // ith quest is available if every quest <i is completed atleast once.

    int t;
    cin >> t;

    while (t--) {
        int n, k;
        long long max = 0;
        long long cmax = 0;
        cin >> n >> k;
        vector<bool> done(n, false);
        vector<pair<int, int>> values(n, {0, 0});

        for (int i = 0; i < n; i++) {
            cin >> values[i].first;
        }
        for (int i = 0; i < n; i++) {
            cin >> values[i].second;
        }

        int q = 0;
        while (q <= k) {

        }


    }

    return 0;
}
