#include <fstream>
using namespace std;
ifstream in("damesah.in");
ofstream out("damesah.out");

int v[15], c[15], d1[30], d2[30], total = 0;
bool pp = false;

void afisare(int n) {
    for (int i = 1; i <= n; i ++) {
        out << v[i] << ' ';
    }
    out << '\n';
}

void bkt(int n, int p) {
    if (p == n + 1) {
        if (!pp) {
            afisare(n);
            pp = true;
        }
        total ++;
    }

    for (int i = 1; i <= n; i ++) {
        if (!c[i] && !d1[n - p + i] && !d2[p + i]) {
            v[p] = i;   c[i] = 1;   d1[n - p + i] = 1;  d2[p + i] = 1;
            bkt(n, p + 1);
            c[i] = 0;   d1[n - p + i] = 0;  d2[p + i] = 0;
        }
    }
}

int main() {
    int n;
    in >> n;
    bkt(n, 1);
    out << total;
    return 0;
}