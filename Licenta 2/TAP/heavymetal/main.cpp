#include <fstream>
#include <algorithm>
using namespace std;
ifstream in("heavymetal.in");
ofstream out("heavymetal.out");

bool sort_right(pair<int, int> a, pair<int, int> b) {
    if (a.second == b.second)   return a.first < b.first;
    return a.second < b.second;
}

int bin(int r, int x, pair<int, int> v[]) {
    int l = 0;
    while (l <= r) {
        int mid = (l + r) / 2;
        if (v[mid].second <= x) {
            l = mid + 1;
        } else {
            r = mid - 1;
        }
    }
    return l - 1;
}

int main() {
    int n;
    in >> n;
    n ++;
    pair<int, int> v[n];
    for (int i = 1; i < n; i ++) {
        in >> v[i].first >> v[i].second;
    }
    v[0] = {0, 0};
    sort(v, v + n, sort_right);
    int dp[n];
    dp[0] = 0;
    for (int i = 1; i < n; i ++) {
        dp[i] = max(dp[i - 1], dp[bin(i, v[i].first, v)] + v[i].second - v[i].first);
    }
    out << dp[n - 1];
    return 0;
}
