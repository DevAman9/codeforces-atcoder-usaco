// AtCoder ABC061 B - Counting Roads
// https://atcoder.jp/contests/abc061/tasks/abc061_b

#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

// alright no cheating this time.
// i did use antigravity for the syntax but not for the logic.
// one thing i learnt is that, before i was thinking of storing each of the cities and the roads
// but i realised, we dont have to store any cities.
// we just have to add one when we see the road.

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    vector<int> count(n+1, 0);

    for (int i = 0; i < m; i ++) {
        int a, b;
        cin >> a >> b;

        count[a] += 1;
        count[b] += 1;

    }

    for (int i = 1; i < n+1 ; i++) {
        cout << count[i] << endl;
    }
    return 0;
}
