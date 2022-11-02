#include <fstream>
#include <vector>
using namespace std;
ifstream in("jocul.in");
ofstream out("jocul.out");
int main() {
    int n;
    in >> n;
    int x, sum = 0;
    vector<int> dp(n * 100, 0);
    for (int i = 0; i < n; i ++) {
        in >> x;
        sum += x;
        for (int j = sum; j >= 0; j --) {
            if (dp[j])  dp[j + x] ++;
        }
        dp[x] ++;
    }
    for (int j = sum / 2; j <= sum; j ++) {
        if (dp[j]) {
            out << min(j, sum - j) << ' ' << max(j, sum - j);
            return 0;
        }
    }
    return 0;
}
