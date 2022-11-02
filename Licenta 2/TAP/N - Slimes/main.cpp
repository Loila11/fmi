#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    long long dp[n + 1][n + 1];
    for (int i = 1; i <= n; i ++) {
        cin >> dp[i][i];
        dp[i][i - 1] = dp[i - 1][i] = dp[i - 1][i - 1] + dp[i][i];
        for (int j = i - 2; j > 0; j --) {
            dp[i][j] = -1;
            dp[j][i] = -1;
            for (int k = i; k > j; k --) {
                long long sum = dp[i][k] + dp[k - 1][j];
                if (dp[i][j] == -1 || dp[i][j] > sum) {
                    dp[i][j] = sum;
                }
                sum = dp[k][i] + dp[i][k] * (i != k) +
                        dp[j][k - 1] + dp[k - 1][j] * (j != k - 1);
                if (dp[j][i] == -1 || dp[j][i] > sum) {
                    dp[j][i] = sum;
                }
            }
        }
    }
    cout << dp[1][n];
    return 0;
}
