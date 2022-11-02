#include <iostream>
#include <string>
using namespace std;
#define mod 1000000007
int main() {
    string k;
    int d;
    cin >> k >> d;
    int dp[k.size() + 1][d + 1], extra[k.size() + 1][d + 1];
    for (int i = 0; i <= k.size(); i ++) {
        for (int j = 0; j <= d; j ++) {
            dp[i][j] = 0;
            extra[i][j] = 0;
        }
    }
    extra[0][0] = 1;
    for (int i = 0; i < k.size(); i ++) {
        for (int j = 0; j < d; j ++) {
            for (int h = 0; h < 10; h ++) {
                dp[i + 1][(j + h) % d] =
                        (dp[i + 1][(j + h) % d] + dp[i][j]) % mod;
                if (h < (k[i] - '0')) {
                    dp[i + 1][(j + h) % d] =
                            (dp[i + 1][(j + h) % d] + extra[i][j]) % mod;
                }
            }
            extra[i + 1][(j + (k[i] - '0')) % d] =
                    (extra[i + 1][(j + (k[i] - '0')) % d] + extra[i][j]) % mod;
        }
    }
    cout << (dp[k.size()][0] + extra[k.size()][0] - 1 + mod) % mod;
    return 0;
}
