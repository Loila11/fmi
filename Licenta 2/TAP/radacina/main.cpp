#include <fstream>
using namespace std;
ifstream in("radacina.in");
ofstream out("radacina.out");

bool verif(double x, int n, double v[]) {
    double p = 1, sum = 0;
    for (int i = 0; i <= n; i ++) {
        sum += (p * v[i]);
        p *= x;
    }
    return sum > 0;
}

void caut_bin(double st, double dr, int n, double v[]) {
    while (dr - st >= 0.00001) {
        double mij = (dr + st) / 2;
        if (verif(mij, n, v) == verif(st, n, v))    st = mij;
        else dr = mij;
    }
    out << st;
}

int main() {
    int n;
    in >> n;
    double v[n + 1];
    for (int i = 0; i <= n; i ++) {
        in >> v[i];
    }
    caut_bin(-20, 20, n, v);
    return 0;
}
