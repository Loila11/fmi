#include <iostream>
using namespace std;

void read(int a[], int n, int i) {
    while (n --) {
        int x;
        cin >> x;
        a[x] = i;
    }
}

int main() {
    // dp[i][j] = numarul minim de schimbari necesare ca foaia i sa ajunga
        // la participantul j
    int k1, k2, k3, n;
    cin >> k1 >> k2 >> k3;
    n = k1 + k2 + k3;
    int a[n + 1];
    read(a, k1, 1);
    read(a, k2, 2);
    read(a, k3, 3);
    int dp[n + 1][4];
    dp[0][1] = dp[0][2] = dp[0][3] = 0;
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j < 4; j ++) {
            dp[i][j] = dp[i - 1][j];
            for (int k = 1; k < j; k ++) {
                dp[i][j] = min(dp[i][j], dp[i - 1][k]);
            }
            dp[i][j] += (a[i] != j);
        }
    }
    cout << min(dp[n][1], min(dp[n][2], dp[n][3]));
    return 0;
}
