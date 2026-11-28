// Codeforces 580A - Kefa and First Steps
// https://codeforces.com/problemset/problem/580/A

#include <iostream>

using namespace std;

int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int t;

    cin >> t;
    int row = 1;
    int crow = 1;
    int a;
    cin >> a;
    for (int i = 1; i < t; i++) {
        int b;
        cin >> b;
        if (b < a) {
            crow = 1;

        }
        else {
            crow++;
        }
        if (crow > row) {
            row = crow;
        };

        a = b;
    }
    cout << row << '\n';

    return 0;
}
