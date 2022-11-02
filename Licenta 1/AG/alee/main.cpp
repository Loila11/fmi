#include <fstream>
#include <queue>
using namespace std;

ifstream in ("alee.in");
ofstream out ("alee.out");

int main() {
    int n, m;
    in >> n >> m;
    int a[n + 3][n + 3];

    for (int i = 0; i <= n + 1; i ++) {
        for (int j = 1; j <= n; j++) {
            a[i][j] = 0;
        }
    }

    for (int i = 0; i <= n + 1; i ++) {
        a[0][i] = -1;
        a[i][0] = -1;
        a[n + 1][i] = -1;
        a[i][n + 1] = -1;
    }

    for (int i = 0; i < m; i ++) {
        int x, y;
        in >> x >> y;
        a[x][y] = -1;
    }

    int linie_start, coloana_start, linie_fin, coloana_fin;
    in >> linie_start >> coloana_start >> linie_fin >> coloana_fin;

    queue <pair <int, int>> q;
    q.push({linie_start, coloana_start});

    int lin[4] = {0, 1, 0, -1}, col[4] = {1, 0, -1, 0};
    a[linie_start][coloana_start] = 1;

    while (!q.empty()) {
        int l = q.front().first;
        int c = q.front().second;
        q.pop();

        for (int i = 0; i < 4; i ++) {
            if (a[l + lin[i]][c + col[i]] == 0) {
                a[l + lin[i]][c + col[i]] = a[l][c] + 1;
                q.push({l + lin[i], c + col[i]});
            }
        }
    }

    out << a[linie_fin][coloana_fin];

    return 0;
}