#include <fstream>
using namespace std;
ifstream in("immortal.in");
ofstream out("immortal.out");
#define x first
#define y second
#define M 30
#define T 30
int l[4] = {0, 1, 0, -1}, c[4] = {1, 0, -1, 0};
int m, n, t, a[M][M];
pair <int, int> poz[T], rez_st[T], rez_fin[T];
bool pp;

void bkt(int);

void afisare() {
    for (int i = 1; i < t; i ++) {
        out << rez_st[i].x << ' ' << rez_st[i].y << ' ';
        out << rez_fin[i].x << ' ' << rez_fin[i].y << '\n';
    }
}

void salt(int &x, int &y, int p) {
    rez_st[p] = {x, y};
    a[x][y] = 0;

    for (int i = 0; i < 4; i ++) {
        x += 2 * l[i];
        y += 2 * c[i];
        if (a[x - l[i]][y - c[i]] == 1 && a[x][y] == 0) {
            rez_fin[p] = {x, y};
            a[x][y] = 1;
            a[x - l[i]][y - c[i]] = 0;
            bkt(p + 1);
            a[x][y] = 0;
            a[x - l[i]][y - c[i]] = 1;
        }
        x -= 2 * l[i];
        y -= 2 * c[i];
    }
    a[x][y] = 1;
}

void bkt(int p = 1) {
    if (p == t) {
        afisare();
        pp = 1;
    }
    if (pp) return ;

    for (int i = 0; i < t; i ++) {
        if (a[poz[i].x][poz[i].y]) {
            salt(poz[i].x, poz[i].y, p);
        }
    }
}

int main() {
    in >> n >> m >> t;
    for (int i = 0; i < t; i ++) {
        in >> poz[i].x >> poz[i].y;
        a[poz[i].x][poz[i].y] = 1;
    }

    for (int i = 0; i <= m + 1; i ++) {
        a[0][i] = -1;
        a[n + 1][i] = -1;
    }

    for(int i = 0; i <= n + 1; i ++) {
        a[i][0] = -1;
        a[i][m + 1] = -1;
    }

    bkt();
    return 0;
}
