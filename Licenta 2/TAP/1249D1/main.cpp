#include <iostream>
#include <algorithm>
using namespace std;
#define l first
#define r second
int cnt[201];

int main() {
    int n, k;
    cin >> n >> k;
    pair <pair<int, int>, int> v[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> v[i].l.l >> v[i].l.r;
        for (int j = v[i].l.l; j <= v[i].l.r; j ++) {
            cnt[j] ++;
        }
        v[i].r = i + 1;
    }
    sort(v, v + n);
    int segm = 0, p[n + 1];
    for (int i = 0; i < n; i ++) {
        while (cnt[v[i].l.l] > k) {
            int pmax = i;
            for (int j = 0; j < n; j ++) {
                if (v[j].l.l <= v[i].l.l && v[j].l.r > v[pmax].l.r) {
                    pmax = j;
                }
            }
            for (int j = v[pmax].l.l; j <= v[pmax].l.r; j ++) {
                cnt[j] --;
            }
            p[segm] = v[pmax].r;
            segm ++;
            v[pmax].l.l = 0;
            v[pmax].l.r = 0;
        }
    }
    cout << segm << '\n';
    for (int i = 0; i < segm; i ++) {
        cout << p[i] << ' ';
    }
    return 0;
}