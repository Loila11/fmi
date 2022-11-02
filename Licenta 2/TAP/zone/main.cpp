#include <fstream>
#include <algorithm>
using namespace std;
ifstream in("zone.in");
ofstream out("zone.out");
#define N 514
#define M 9
long long a[N][N], zona[M], p[M];

bool find(long long x) {
    for (long long i : zona)  if (i == x)  return true;
    return false;
}

bool verif() {
    for (int i = 0; i < M; i ++ )   if (p[i] != zona[i])    return false;
    return true;
}

bool fin(int l1, int c1, int l2, int c2, int n) {
    p[1] = a[l1][c1];
    p[2] = a[l1][c2] - a[l1][c1];
    p[3] = a[l1][n] - a[l1][c2];
    p[4] = a[l2][c1] - a[l1][c1];
    p[5] = a[l2][c2] - a[l1][c2] + a[l1][c1] - a[l2][c1];
    p[6] = a[l2][n] - a[l1][n] + a[l1][c2] - a[l2][c2];
    p[7] = a[n][c1] - a[l2][c1];
    p[8] = a[n][c2] - a[l2][c2] + a[l2][c1] - a[n][c1];
    p[0] = a[n][n] - a[l2][n] + a[l2][c2] - a[n][c2];
    sort (p, p + M);
    if (verif()) {
        out << l1  << ' ' << l2 << ' ' << c1 << ' ' << c2;
        return true;
    }
    return false;
}

void solve(int n) {
    for (int l1 = 1; l1 < n; l1 ++)
        for (int c1 = 1; c1 < n; c1 ++)
            if (find(a[l1][c1]))
                for (int l2 = l1 + 1; l2 < n; l2 ++)
                    if(find(a[l2][c1] - a[l1][c1]))
                        for (int c2 = c1 + 1; c2 < n; c2 ++)
                            if(find(a[l1][c2] - a[l1][c1]))
                                if (fin(l1, c1, l2, c2, n))
                                    return ;
}

int main() {
    int n;
    in >> n;
    for (long long & i : zona)    in >> i;
    sort(zona, zona + 9);

    for (int i = 1; i <= n; i ++) {
        for (int j = 1; j <= n; j ++) {
            in >> a[i][j];
            a[i][j] += a[i - 1][j] - a[i - 1][j - 1] + a[i][j - 1];
        }
    }

    solve(n);
    return 0;
}
