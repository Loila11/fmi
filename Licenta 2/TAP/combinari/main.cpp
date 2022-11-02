#include <fstream>
using namespace std;
ifstream in ("combinari.in");
ofstream out("combinari.out");

int v[100];

void afisare(int k) {
    for (int i = 1; i <= k; i ++) {
        out << v[i] << ' ';
    }
    out << '\n';
}

void bkt(int n, int k, int p) {
    if(p == k + 1) {
        afisare(k);
    }
    for (int i = v[p - 1] + 1; i <= n; i ++) {
        v[p] = i;
        bkt(n, k, p + 1);
    }
}

int main() {
    int n, k;
    in >> n >> k;
    v[0] = 0;
    bkt(n, k, 1);
    return 0;
}