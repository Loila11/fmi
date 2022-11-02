#include <iostream>
#include <algorithm>
using namespace std;

int rez(int power[], int a[], int n) {
    int sol = 1, d = 0, maxim = 0;
    for (int i = 0; i < n; i ++, d ++) {
        maxim = max(maxim, a[i]);
        if (power[d] < maxim) {
            maxim = a[i];
            if (power[0] < maxim) {
                return -1;
            }
            d = 0;
            sol++;
        }
    }
    return sol;
}

int main() {
    int t;
    cin >> t;
    while (t --) {
        int n;
        cin >> n;
        int a[n], power[n + 1];
        for (int i = 0; i < n; i++) {
            cin >> a[i];
            power[i] = 0;
        }
        int m;
        cin >> m;
        for (int i = 0; i < m; i ++) {
            int p, s;
            cin >> p >> s;
            power[s - 1] = max(power[s - 1], p);
        }
        power[n] = 0;
        for (int i = n - 1; i >= 0; i --) {
            power[i] = max(power[i], power[i + 1]);
        }
        cout << rez(power, a, n) << '\n';
    }
    return 0;
}
