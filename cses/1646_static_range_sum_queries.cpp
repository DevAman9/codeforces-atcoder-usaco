// CSES 1646 - Static Range Sum Queries
// https://cses.fi/problemset/task/1646/

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n , q ;
    cin >> n >> q ;
    vector<int> num(n+1);

    for (int i = 1; i < n+1 ; i ++ ) {
        cin >> num[i];
    }


 // changed to long long myself because of int error.
    vector<long long> sums(n+1, 0);
    sums[0] = 0;
    for (int i = 1; i < n+1; i++) {
        sums[i] = sums[i-1] + num[i];
    }


    for (int i = 0; i < q; i++) {
        int a, b;
        cin >> a >> b;
        cout << sums[b] - sums[a-1] << '\n';
    }


    return 0;
}


