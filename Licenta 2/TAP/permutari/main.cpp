#include <fstream>
using namespace std;
ifstream in("permutari.in");
ofstream out("permutari.out");

int v[10], viz[10];

void afisare(int n) {
    for (int i = 1; i <= n; i ++) {
        out << v[i] << ' ';
    }
    out << '\n';
}

void bkt(int n, int p) {
    if (p == n + 1) {
        afisare(n);
    }
    for (int i = 1; i <= n; i ++) {
        if (viz[i] == 0) {
            viz[i] = 1; v[p] = i;
            bkt(n, p + 1);
            viz[i] = 0;
        }
    }
}

int main() {
    int n;
    in >> n;
    bkt(n, 1);
    return 0;
}