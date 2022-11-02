#include <fstream>
using namespace std;
ifstream in("maxsubsum.in");
ofstream out("maxsubsum.out");
int main() {
    int n, m;
    in >> n >> m;
    long long a[n + 1], b[m + 1], spa[n + 1],  spb[m + 1];

    in >> a[0];
    for (int i = 1; i < n; i ++) {
        in >> a[i];
        a[i] += a[i - 1];
    }
    in >> b[0];
    for (int i = 1; i < m; i ++) {
        in >> b[i];
        b[i] += b[i - 1];
    }

    for (int i = 1; i <= n; i ++) {
        spa[i] = a[i - 1];
        for (int j = i + 1; j <= n; j ++) {
            spa[i] = max(spa[i], a[j - 1] - a[j - i - 1]);
        }
    }
    for (int i = 1; i <= m; i ++) {
        spb[i] = b[i - 1];
        for (int j = i + 1; j <= m; j ++) {
            spb[i] = max(spb[i], b[j - 1] - b[j - i - 1]);
        }
    }

    long long ans = 0;
    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= m; j ++) {
            ans = max(ans, spa[i] * j + spb[j] * i);
        }
    }
    out << ans;
    return 0;
}
