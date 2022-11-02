#include <iostream>
using namespace std;
int v[200003];

int verif(int x, int n) {
    int ct = 0;
    for (int i = 0; i < n; i ++) {
        if (v[i] <= ct) ct ++;
        else if (x > 0) {
            x --;
            ct ++;
        }
    }
    return ct;
}

void bin(int st, int dr, int n, int m) {
    while (st <= dr) {
        int mij = (st + dr) / 2;
        if (verif(mij, n) >= m) {
            dr = mij - 1;
        }
        else st = mij + 1;
    }
    cout << dr + 1;
}

int main() {
    int n, m;
    cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        cin >> v[i];
    }
    bin(0, m, n, m);
    return 0;
}
