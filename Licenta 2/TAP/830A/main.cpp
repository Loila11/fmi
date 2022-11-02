#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n, k, p;
    cin >> n >> k >> p;
    int a[n], b[k];
    for (int i = 0; i < n; i ++) {
        cin >> a[i];
    }
    sort(a, a + n);
    for (int i = 0; i < k; i ++) {
        cin >> b[i];
    }
    sort(b, b + k);
    long long fin = 2 * max(b[k - 1], max(a[n - 1], p));
    for (int i = 0; i <= k - n; i ++) {
        long long sol = 0;
        for (int j = 0; j < n; j ++) {
            sol = max(sol, (long long)(abs(p - b[i + j]) + abs(b[i + j] - a[j])));
        }
        fin = min(fin, sol);
    }
    cout << fin;
    return 0;
}
