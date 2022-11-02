#include <fstream>
using namespace std;

ifstream in ("date.in");
ofstream out ("date.out");

#define M 10000
int Q, E, F, q0, n;
int q[M], e[27], f[M], v[M][27];

void citire_i(int &n, int v[]) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        int x;
        in >> x;
        v[x] = 1;
    }
}

void citire_c(int &n, int v[]) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        char x;
        in >> x;
        v[x - 'a'] = 1;
    }
}

void citire_t(int &n, int v[][27]) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        int x, y;
        char z;
        in >> x >> z >> y;
        v[x][z - 'a'] = y;
    }
}

void citire() {
    citire_i(Q, q);
    citire_c(E, e);
    in >> q0;
    citire_i(F, f);
    citire_t(n, v);
}

bool dfa() {
    int q = q0;

    string s;
    in >> s;
    for (char i : s) {
        q = v[q][i - 'a'];
        if (q == 0) {
            return false;
        }
    }

    return f[q] == 1;
}

void rezolvare() {
    int t;
    in >> t;
    while (t --) {
        bool pp = dfa();
        if (pp == 0) {
            out << "NU\n";
        } else {
            out << "DA\n";
        }
    }
}

int main() {
    citire();
    rezolvare();
    return 0;
}

