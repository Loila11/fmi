#include <fstream>
using namespace std;
ifstream in("copii.in");
ofstream out("copii.out");
#define N 11
int v[N], pos = 0;
char s[N][N];

void solve(int nr_grupe, int n) {
    if (nr_grupe < 1) {
        return ;
    }

    bool a[nr_grupe + 1][nr_grupe + 1];

    for (int i = 0; i <= nr_grupe; i ++) {
        for (int j = 0; j <= nr_grupe; j ++) {
            a[i][j] = false;
        }
    }

    for (int i = 0; i < n; i ++) {
        int grupa1 = v[i + 1];
        for (int j = 0; j < n; j ++) {
            if (s[i][j] == '1') {
                int grupa2 = v[j + 1];
                a[grupa1][grupa2] = true;
            }
        }
    }

    for (int i = 0; i <= nr_grupe; i ++) {
        for (int j = 0; j <= nr_grupe; j ++) {
            if (i != j && !a[i][j]) {
                return ;
            }
        }
    }
    pos ++;
}

void bkt(int p, int et_max, int n) {
    if (p == n + 1) {
        solve(et_max, n);
        return ;
    }
    for (int i = 0; i <= et_max; i ++) {
        v[p] = i;
        bkt(p + 1, et_max, n);
    }
    v[p] = et_max + 1;
    bkt(p + 1, et_max + 1, n);
}

int main() {
    int n;
    in >> n;
    for (int i = 0; i < n; i ++) {
        in >> s[i];
    }
    v[1] = 0;
    bkt(2, 0, n);
    out << pos;
    return 0;
}