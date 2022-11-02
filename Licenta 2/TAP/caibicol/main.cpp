#include <fstream>
using namespace std;
#define INF 250000
ifstream in("caibicol.in");
ofstream out("caibicol.out");

int main() {
    int n, k;
    in >> n >> k;
    int a[n + 1], b[n + 1], dp[k][n + 1];
    a[0] = b[0] = 0;    dp[0][0] = 0;
    for (int i = 1; i <= n; i ++) {
        int x;
        in >> x;
        a[i] = a[i - 1] + (x == 1);
        b[i] = b[i - 1] + (x == 0);
        dp[0][i] = a[i] * b[i];
    }
    for (int i = 1; i < k; i ++) {
        dp[i][0] = 0;
        for (int j = 1; j <= n; j ++) {
            dp[i][j] = INF;
            for (int h = 1; h <= j; h ++) {
                dp[i][j] = min(dp[i][j], dp[i - 1][h - 1] + (a[j] - a[h - 1]) * (b[j] - b[h - 1]));
            }
        }
    }
    out << dp[k - 1][n];
    return 0;
}
