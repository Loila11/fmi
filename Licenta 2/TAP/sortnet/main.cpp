#include <cstdio>
using namespace std;
#define N 21
#define M 33
int v[M][N], w[M], l[N];

bool sortat(int x) {
    return ((x & (x + 1)) == 0);
}

bool bit_find(int x, int poz) {
    return x & (1 << poz);
}

void bit_swap(int &x, int p1, int p2) {
    x |= (1 << p2);
    x &= ~(1 << p1);
}

inline int verif(int k, int x, int n, int m) {
    for (int i = 0; i < m; i ++) {
        int y = v[i][x + 1] - 1;
        if (x > y && bit_find(w[i - 1], x) > bit_find(w[i - 1], y)) {
            bit_swap(k, x, y);
        }
        w[i] ^= (1 << x);
    }
    return (x >> l[x & (-x)]) == ((1 << (n - l[x & (-x)])) - 1);;
}

int main() {
    freopen("sortnet.in", "r", stdin);
    freopen("sortnet.out", "w", stdout);
    int n, m;
    scanf("%d %d\n", &n, &m);
    for (int i = 0; i < N; ++i) {
        l[1 << i] = i;
    }
    for (int i = 0; i < m; i ++) {
        for (int j = 0; j < n / 2; j ++) {
            int a, b;
            scanf("<%d,%d> ", &a, &b);
            v[i][a] = b;
            v[i][b] = a;
        }
    }
    int sol = 0, fin = (1 << n);
    for (int i = 0; i < fin; i ++) {
        w[0] = i ^ (i >> 1);
        sol += verif(i, l[w[0] ^ ((i - 1) ^ ((i - 1) >> 1))], n, m);
    }
    printf("%d\n", sol);
    return 0;
}
