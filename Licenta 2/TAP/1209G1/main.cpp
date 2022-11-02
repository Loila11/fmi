#include <iostream>
#include <algorithm>
using namespace std;
#define N 200001
#define st first
#define dr second
int cnt[N], start[N], last[N];

int main() {
    int n, q;
    cin >> n >> q;
    int a[n + 1];
    for (int i = 1; i <= n; i ++) {
        cin >> a[i];
        cnt[a[i]] ++;
        if (start[a[i]] == 0) {
            start[a[i]] = i;
        }
        last[a[i]] = i;
    }
    pair<int, int> v = {start[a[1]], last[a[1]]};
    int  sol = 0, maxx = cnt[a[1]];
    for (int i = 2; i <= n; i ++) {
        if (start[a[i]] == i) {
            if (v.dr > i) {
                v.dr = max(v.dr, last[a[i]]);
                maxx = max(maxx, cnt[a[i]]);
            } else {
                sol += v.dr - v.st + 1 - maxx;
                v = {start[a[i]], last[a[i]]};
                maxx = cnt[a[i]];
            }
        }
    }
    sol += v.dr - v.st + 1 - maxx;
    cout << sol;
    return 0;
}
