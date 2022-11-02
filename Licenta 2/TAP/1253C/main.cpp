#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n, m;
    cin >> n >> m;
    long long sum[n], dp[n];
    for (int i = 0; i < n; i ++) {
        cin >> sum[i];
    }
    sort(sum, sum + n);
    for (int i = 1; i < n; i ++) {
        sum[i] += sum[i - 1];
    }
    for (int i = 0; i < m; i ++) {
        dp[i] = sum[i];
        cout << dp[i] << ' ';
    }
    for (int k = m; k < n; k ++) {
        dp[k] = sum[k] + dp[k - m];
        cout << dp[k] << ' ';
    }
    return 0;
}
