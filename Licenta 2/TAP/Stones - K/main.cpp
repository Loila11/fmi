#include <fstream>
using namespace std;
ifstream in("podm.in");
ofstream out("podm.out");
int main ()
{
    // dp[i][j] = numarul minim de inmultiri scalare intre matricea i si matricea j
    int n;
    in >> n;
    long long d[n + 1], dp[n + 1][n + 1];
    in >> d[0];
    for (int i = 1; i <= n; i ++) {
        in >> d[i];
        dp[i][i] = 0;
        dp[i - 1][i] = d[i - 2] * d[i - 1] * d[i];
    }

    for (int l = 1; l < n; l ++) {
        for (int i = 1; i <= n - l; i ++) {
            int j = i + l;
            long long minim = -1;
            for (int k = i; k < j; k ++) {
                long long cost = dp[i][k] + dp[k + 1][j] + d[i - 1] * d[k] * d[j];
                if (minim == -1 || minim > cost)
                    minim = cost;
            }
            dp[i][j] = minim;
        }
    }
    out << dp[1][n];
    return 0;
}
