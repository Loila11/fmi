#include <fstream>
using namespace std;
ifstream in("dusman.in");
ofstream out("dusman.out");
#define N 10001
bool d[N][N], pp;
int v[N], viz[N], ct = 0;

void afisare(int n) {
    for (int i = 1; i <= n; i ++) {
        out << v[i] << ' ';
    }
}

void bkt(int p, int k, int n) {
    if (p == n + 1) {
        ct ++;
        if(ct == k) {
            afisare(n);
            pp = true;
        }
    }
    if (pp) return;
    for (int i = 1; i <= n; i ++) {
        if (viz[i] == 0 && d[v[p - 1]][i] == 0) {
            viz[i] = 1;
            v[p] = i;
            bkt(p + 1, k, n);
            viz[i] = 0;
        }
    }
}

int main() {
    int n, m, k;
    in >> n >> k >> m;
    while (m -- ) {
        int x, y;
        in >> x >> y;
        d[x][y] = true;
        d[y][x] = true;
    }
    bkt(1, k, n);
    return 0;
}