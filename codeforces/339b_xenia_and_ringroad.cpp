// Codeforces 339B - Xenia and Ringroad
// https://codeforces.com/problemset/problem/339/B

#include <iostream>
using namespace std;


int main() {
    std::ios::sync_with_stdio(false);
    std::cin.tie(nullptr);

    int n, m;
    cin >> n >> m;
    long long time = 0;
    int a = 0;
    for (int i = 0; i < m; i++) {
        int b;
        cin >> b;
        b = b - 1;
        if (a <= b) {
            time += b - a;
        }
        else {
            time += (n - (a % n)) + b;
        }
        a = b;

    }

    cout << time << '\n';

    // 3-1 = 2; 2-0=2;2 mod 4 = 2
    // 0 1 2 3 0 1 2 3
    // 1 2 3 4 1 2 3 4
    // 0+2= 2; 2 mod 4 = 2
    // 2+1=3 ; 3 mod 4 = 3;
    // 1+2=3 ; 3 mod 4 =


    // 0 1 2 3 0 1 2 3
    // 1 2 3 4 1 2 3 4
    // if b < a;
    // a mod n ; n - a= n'
    // b mod n;


    return 0;
}
