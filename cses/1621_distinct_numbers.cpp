// CSES 1621 - Distinct Numbers
// https://cses.fi/problemset/task/1621/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);
    int n;
    cin >> n;
    vector<int> num(n);
    for (int i = 0; i < n; i++){
        cin >> num[i];
    }

    sort(num.begin(), num.end());
    int ans = 1;

    for (int i = 1; i < n; i++) {
        ans += (num[i] != num[i - 1]);
    }

    cout << ans << endl;





    return 0;
};
