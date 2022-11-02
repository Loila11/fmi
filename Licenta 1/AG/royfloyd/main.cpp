#include <fstream>
using namespace std;

ifstream in ("royfloyd.in");
ofstream out ("royfloyd.out");

int main() {
    int n;
    in >> n;
    int a[n + 1][n + 1];

    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= n; j ++) {
            in >> a[i][j];
        }
    }

    for (int k = 1; k <= n; k ++) {
        for (int i = 1; i <= n; i ++) {
            for (int j = 1; j <= n; j ++) {
                if (i != j && a[i][k] != 0 && a[k][j] != 0) {
                    if (a[i][j] == 0) {
                        a[i][j] = a[i][k] + a[k][j];
                    } else {
                        a[i][j] = min(a[i][j], a[i][k] + a[k][j]);
                    }
                }
            }
        }
    }

    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= n; j ++) {
            out << a[i][j] << " ";
        }
        out << '\n';
    }

    return 0;
}