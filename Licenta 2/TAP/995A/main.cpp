#include <iostream>
using namespace std;
#define M 20001
pair<int, pair<int, int>> sol[M];

pair<int, int> next(pair<int, int> x, int n) {
    pair<int, int> y = x;
    if (x.first == 1) {
        if (x.second == n - 1) {
            y = {2, n - 1};
        } else {
            y.second ++;
        }
    } else {
        if (x.second == 0) {
            y = {1, 0};
        } else {
            y.second --;
        }
    }
    return y;
}

void print(int m) {
    if (m >= M) {
        cout << "-1";
        return ;
    }
    cout << m << '\n';
    for (int i = 0; i < m; i ++) {
        cout << sol[i].first << ' ' << sol[i].second.first << ' ';
        cout << sol[i].second.second << '\n';
    }
}

int main() {
    int n, k, m = 0;
    cin >> n >> k;
    int a[4][n];
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < n; j ++) {
            cin >> a[i][j];
        }
    }
    int rest = k;
    while (rest && m < M) {
        pair<int, int> x = {0, 0}, y, z;
        for (int i = 0; i < n; i ++) {
            if (a[1][i] == a[0][i] && a[1][i] != 0) {
                a[1][i] = 0;
                sol[m] = {a[0][i], {1, i + 1}};
                m ++;
                rest --;
            }
            if (a[2][i] == a[3][i] && a[2][i] != 0) {
                a[2][i] = 0;
                sol[m] = {a[3][i], {4, i + 1}};
                m ++;
                rest --;
            }
            if (a[1][i] == 0) {
                x = {1, i};
            } else if (a[2][i] == 0) {
                x = {2, i};
            }
        }
        if (x.first == 0) {
            m = M;
            break;
        }
        z = x;
        y = next(x, n);
        while (y != z) {
            a[x.first][x.second] = a[y.first][y.second];
            a[y.first][y.second] = 0;
            if (a[x.first][x.second] != 0) {
                sol[m] = {a[x.first][x.second], {x.first + 1, x.second + 1}};
                m ++;
            }
            x = y;
            y = next(x, n);
        }
    }
    print(m);
    return 0;
}
