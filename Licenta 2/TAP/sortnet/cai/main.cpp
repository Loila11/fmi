#include <fstream>
#include <algorithm>
using namespace std;
ifstream in("cai.in");
ofstream out("cai.out");
int main() {
    int t;
    in >> t;
    while (t --) {
        int n;
        in >> n;
        int a[n], b[2 * n];
        for (int i = 0; i < n; i ++) {
            in >> a[i];
        }
        sort(a, a + n);
        for (int i = 0; i < n; i ++) {
            in >> b[i];
        }
        sort(b, b + n);
        int sol = -1 * n;
        for (int i = 0; i < n; i ++) {
            b[i + n] = b[i];
        }
        for (int i = 0; i < n; i ++) {
            int s = 0;
            for (int j = 0; j < n; j ++) {
                if (a[j] < b[i + j]) {
                    s --;
                } else if (a[j] > b[i + j]) {
                    s ++;
                }
            }
            sol = max(sol, s);
        }
        out << sol * 200 << '\n';
    }
    return 0;
}
