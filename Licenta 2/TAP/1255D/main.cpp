#include <iostream>
using namespace std;
#define M 101
char v[62], s[M][M], f[M][M];

void update(int k, int i, int j, int &x, int &h, int &rest, int cat) {
    f[i][j] = v[h];
    if (s[i][j] == 'R') {
        x ++;
        if (x == cat && rest != 0) {
            rest --;
        } else if (x >= cat) {
            if (h < k - 1) h ++;
            x = 0;
        }
    }
}

int main() {
    int t;
    cin >> t;
    char aux = 'a';
    for (char & i : v) {
        i = aux;
        if (aux == 'z')   aux = 'A';
        else if (aux == 'Z')  aux = '0';
        else    aux ++;
    }
    while (t --) {
        int r, c, k;
        cin >> r >> c >> k;
        int nr = 0;
        for (int i = 0; i < r; i ++) {
            for (int j = 0; j < c; j ++) {
                cin >> s[i][j];
                if (s[i][j] == 'R') nr ++;
                f[i][j] = ' ';
            }
        }
        int h = 0, x = 0, rest = nr % k;
        for (int i = 0; i < r; i ++) {
            if (i % 2 == 0) {
                for (int j = 0; j < c; j ++) {
                    if (f[i][j] != ' ') continue;
                    update(k, i, j, x, h, rest, nr / k);
                }
            } else {
                for (int j = c - 1; j >= 0; j --) {
                    if (f[i][j] != ' ') continue;
                    update(k, i, j, x, h, rest, nr / k);
                }
            }
            f[i][c] = '\0';
            cout << f[i] << '\n';
        }
    }
    return 0;
}
