#include <fstream>
using namespace std;
ifstream in ("fact.in");
ofstream out("fact.out");

int count_zero(int x) {
    int p = 5, ct = 0;
    while (p <= x) {
        ct += x / p;
        p *= 5;
    }
    return ct;
}

void fin(int x, int p) {
    while (count_zero(x - 1) == p && x > 1)  x --;
    out << x;
}

void binary_search(int p, int st, int dr) {
    while (st <= dr) {
        int mij = (st + dr) / 2;
        int x = count_zero(mij);
        if (x == p) {
            fin(mij, p);
            return ;
        } else if (x > p) {
            dr = mij - 1;
        } else {
            st = mij + 1;
        }
    }
    out << "-1";
}

int main() {
    int p;
    in >> p;
    if (p == 0) out << "1";
    else binary_search(p, 1, 5 * p);
    return 0;
}