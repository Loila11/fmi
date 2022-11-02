#include <iostream>
using namespace std;
#define N 1002
int a[N + 1][N + 1];
int lin[] = {0, 1, 0, -1, 1, -1, 1, -1, 0}, col[] = {1, 0, -1, 0, 1, 1, -1, -1, 0};

bool verif(int x, int y, int n) {
    return !(x <= 0 || y <= 0 || x > n || y > n || a[x][y] == 0);
}

bool verif_patrat(int l, int c, int n) {
    for (int i = 0; i < 8; i ++) {
        int x = lin[i] + l, y = col[i] + c;
        if (!verif(x, y, n)) return false;
    }
    return true;
}

bool centru(int l, int c, int n) {
    for (int i = 0; i < 9; i ++) {
        int x = lin[i] + l, y = col[i] + c;
        if (verif(x, y, n) && verif_patrat(x, y, n))  return true;
    }
    return false;
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 1; i <= m; i ++) {
        int x, y;
        cin >> x >> y;
        a[x][y] = 1;
        if (centru(x, y, n)) {
            cout << i;
            return 0;
        }
    }
    cout << "-1";
    return 0;
}
/*
3 9
2 3
1 3
3 1
1 1
3 3
2 1
1 2
3 2
2 2
 */