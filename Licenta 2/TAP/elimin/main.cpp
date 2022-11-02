#include <fstream>
using namespace std;
ifstream in("elimin.in");
ofstream out("elimin.out");

void elimin(int l[]) {

}

void bkt(int n, int m, int v[], int i, int r, int c) {
    for (int j = 0; j < n; j ++) {
        v[i] = j;
        if (v[i] > v[i - 1]) {
            if (i == c) {
                elimin();
            } else {
                bkt(n, m, v, i + 1, r, c);
            }
        }
    }
}

int main() {
    int n, m, r, c;
    in >> n >> m >> c >> r;
    int a[min(n, m)][max(n, m)], lin[min(n, m)], col[max(n, m)];
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (n <= m) {
                in >> a[i][j];
                lin[i] += a[i][j];
                col[j] += a[i][j];
            }
            else {
                in >> a[j][i];
                lin[j] += a[j][i];
                col[i] += a[j][i];
            }
        }
    }
    if (n > m) {
        swap(n, m);
        swap(r, c);
    }
    return 0;
}
