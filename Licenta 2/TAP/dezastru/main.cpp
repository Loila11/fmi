#include <fstream>
#include <iomanip>

using namespace std;
ifstream in("dezastru.in");
ofstream out("dezastru.out");

double fact(int n) {
    double f = 1;
    for (int i = 1; i <= n; i ++) {
        f *= i;
    }
    return f;
}

void bkt(double v[], int n, int k, int i, int cate, double p, double &fin) {
    if (cate == k) {
        fin += p;
        return ;
    }
    for (int j = i + 1; j < n; j ++) {
        bkt(v, n, k, j, cate + 1, p * v[j], fin);
    }
}

int main() {
    int n, k;
    in >> n >> k;
    double p[n];
    for(int i = 0; i < n; i ++) {
        in >> p[i];
    }
    double sol = 0;
    for (int i = 0; i < n; i ++) {
        bkt(p, n, k, i, 1, p[i], sol);
    }
    out << setprecision(6) << sol * fact(n - k) * fact(k) / fact(n);
    return 0;
}
