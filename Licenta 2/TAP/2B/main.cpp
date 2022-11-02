#include <iostream>
using namespace std;

int power(int x, int w) {
    if (x == 0) return 1;
    int p = 0;
    while (x % w == 0) {
        p ++;
        x /= w;
    }
    return p;
}

void print(int i, int j, int **pr) {
    if (i == 0 && j == 0) {
        return ;
    }
    if (pr[i][j] == 0) {
        print(i, j - 1, pr);
        cout << 'R';
    } else {
        print(i - 1, j, pr);
        cout << 'D';
    }
}

void add(int i, int j, int i2, int j2, int **m, int **pr) {
    m[i][j] = m[i2][j2];
    pr[i][j] = (j == j2);
}

int main() {
    int n;
    cin >> n;
    int *a[n], *pra[n], *b[n], *prb[n], pnul = -1;
    for (int i = 0; i < n; i ++) {
        a[i] = static_cast<int *>(malloc(n * sizeof(int)));
        pra[i] = static_cast<int *>(malloc(n * sizeof(int)));
        b[i] = static_cast<int *>(malloc(n * sizeof(int)));
        prb[i] = static_cast<int *>(malloc(n * sizeof(int)));
        for (int j = 0; j < n; j ++) {
            int x;
            cin >> x;
            if (i + j == 0) {
                a[i][j] = b[i][j] = 0;
            } else if (j != 0 && i == 0) {
                add(i, j, i, j - 1, a, pra);
                add(i, j, i, j - 1, b, prb);
            } else if (i != 0 && j == 0) {
                add(i, j, i - 1, j, a, pra);
                add(i, j, i - 1, j, b, prb);
            } else {
                if (a[i][j - 1] < a[i - 1][j]) {
                    add(i, j, i, j - 1, a, pra);
                } else {
                    add(i, j, i - 1, j, a, pra);
                }
                if (b[i][j - 1] < b[i - 1][j]) {
                    add(i, j, i, j - 1, b, prb);
                } else {
                    add(i, j, i - 1, j,  b, prb);
                }
            }
            if (x == 0) pnul = i;
            a[i][j] += power(x, 5);
            b[i][j] += power(x, 2);
        }
    }
    if (pnul != -1 && min(a[n - 1][n - 1], b[n - 1][n - 1]) > 1) {
        cout << "1\n";
        for (int j = 1; j <= pnul; j ++) {
            cout << 'D';
        }
        for (int i = 1; i < n; i ++) {
            cout << 'R';
        }
        for (int j = pnul + 1; j < n; j ++) {
            cout << 'D';
        }
    } else {
        cout << min(a[n - 1][n - 1], b[n - 1][n - 1]) << '\n';
        if (a[n - 1][n - 1] < b[n - 1][n - 1]) {
            print(n - 1, n - 1, pra);
        } else {
            print(n - 1, n - 1, prb);
        }
    }
    return 0;
}
