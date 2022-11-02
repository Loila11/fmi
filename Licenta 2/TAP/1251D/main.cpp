#include <iostream>
#include <algorithm>
using namespace std;
#define l first
#define r second

bool check(pair<int, int> v[], int n, long long s, long long x) {
    int rest[n], m = 0, l = 0, r = 0;
    for (int i = 0; i < n; i ++) {
        if (v[i].r < x) {
            l ++;
            s -= v[i].l;
        } else if (v[i].l > x) {
            r ++;
            s -= v[i].l;
        } else {
            rest[m] = v[i].l;
            m ++;
        }
    }
    if (r > n / 2 || l > n / 2 || s < 0) return false;
    sort(rest, rest + m);
    for (int i = 0; i + l < n / 2; i ++) {
        s -= rest[i];
    }
    s -= x * (n / 2 - r + 1);
    return s >= 0;
}

long long bin_search(pair<int, int> v[], int n, long long s) {
    sort(v, v + n);
    long long st = v[n / 2].l, dr = s;
    while (st <= dr) {
        long long mid = (st + dr) / 2;
        if (check(v, n, s, mid)) st = mid + 1;
        else    dr = mid - 1;
    }
    return st - 1;
}

int main() {
    int t;
    cin >> t;
    while (t --) {
        int n;
        long long s;
        cin >> n >> s;
        pair <int, int> v[n];
        for (int i = 0; i < n; i ++) {
            cin >> v[i].l >> v[i].r;
        }
        cout << bin_search(v, n, s) << '\n';
    }
    return 0;
}
