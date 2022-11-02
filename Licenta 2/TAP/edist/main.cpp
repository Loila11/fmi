#include <fstream>
using namespace std;
ifstream in("edist.in");
ofstream out("edist.out");
int main() {
    int n, m, k;
    string s1, s2;
    in >> n >> m >> k >> s1 >> s2;

    int dp[2][m + 1];
    for (int i = 0; i <= m; i ++) {
        dp[0][i] = i;
    }
    int p = 1;
    for (int i = 1; i <= n; i ++) {
        dp[p][0] = i;
        for (int j = max(1, i - k); j <= min(m, i + k); j ++) {
            dp[p][j] = min(dp[1 - p][j - 1] + (s1[i - 1] != s2[j - 1]),
                       min(dp[p][j - 1] + 1, dp[1 - p][j] + 1));
        }
        p = 1 - p;
    }
    out << dp[1 - p][m];
    return 0;
}
