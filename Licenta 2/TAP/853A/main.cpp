#include <iostream>
#include <algorithm>
using namespace std;
#define N 600002
long long next_free[N];

long long update(long long i) {
    if (next_free[i] == i) {
        return i;
    }
    next_free[i] = update(next_free[i]);
    return next_free[i];
}

int main() {
    int n, k;
    cin >> n >> k;
    pair<long long, int> c[n + 1];
    for (int i = 1; i <= n; i ++) {
        cin >> c[i].first;
        c[i].second = i;
    }
    for (int i = 0; i <= k; i ++) {
        next_free[i] = k + 1;
    }
    for (int i = k + 1; i < N; i ++) {
        next_free[i] = i;
    }
    sort(c + 1, c + n + 1, greater<>());
    long long t[n + 1];
    long long cost = 0;
    for (int i = 1; i <= n; i ++) {
        long long j = update(next_free[c[i].second]);
        next_free[j] = update(j + 1);
        next_free[c[i].second] = next_free[j];
        t[c[i].second] = j;
        cost += c[i].first * (j - c[i].second);
    }
    cout << cost << '\n';
    for (int i = 1; i <= n; i ++) {
        cout << t[i] << ' ';
    }
    return 0;
}
