#include <iostream>
using namespace std;

int main() {
    int r, c;
    cin >> r >> c;
    char a[r + 1][c + 1];
    for (int i = 0; i < r; i ++) {
        for (int j = 0; j < c; j ++) {
            cin >> a[i][j];
        }
    }

    int l[4] = {0, -1, 0, 1}, cl[4] = {-1, 0, 1, 0};
    for (int i = 0; i < r; i ++) {
        for (int j = 0; j < c; j++) {
            if (a[i][j] == 'S') {
                for (int k = 0; k < 4; k ++) {
                    int lin = i + l[k];
                    int col = j + cl[k];
                    if (lin >= 0 && col >= 0 && lin < r && col < c) {
                        if (a[lin][col] == 'W') {
                            cout << "NO";
                            return 0;
                        } else if (a[lin][col] == '.') {
                            a[lin][col] = 'D';
                        }
                    }
                }
            }
        }
    }

    cout << "YES\n";
    for (int i = 0; i < r; i ++) {
        for (int j = 0; j < c; j++) {
            cout << a[i][j];
        }
        cout << '\n';
    }
    return 0;
}
