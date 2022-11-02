#include <iostream>
using namespace std;
int main() {
    int n, m, k, t = 0;
    cin >> n >> m >> k;
    char a[n + 1][m + 1];
    for (int i = 0; i < n; i ++) {
        int l = 0;
        for (int j = 0; j < m; j ++) {
            cin >> a[i][j];
            if (a[i][j] == '.') {
                l ++;
                if (l >= k) {
                    t ++;
                }
            } else {
                l = 0;
            }
        }
    }

    if (k == 1) {
        cout << t;
        return 0;
    }

    for (int i = 0; i < m; i ++) {
        int l = 0;
        for (int j = 0; j < n; j ++) {
            if (a[j][i] == '.') {
                l ++;
                if (l >= k) {
                    t ++;
                }
            } else {
                l = 0;
            }
        }
    }

    cout << t;
    return 0;
}