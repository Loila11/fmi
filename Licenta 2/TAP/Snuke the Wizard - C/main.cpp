#include <iostream>
using namespace std;
#define t first
#define d second

int verif(int p, char s[], int q, pair <char, char> v[]) {
    for (int i = 0; i < q; i ++) {
        if (s[p] == v[i].t) {
            if (v[i].d == 'R')  p ++;
            else    p --;
        }
    }
    return p;
}

int caut_bin_left(int st, int dr, char s[],
                  int q, pair <char, char> v[]) {
    while (st <= dr) {
        int mij = (st + dr) / 2;
         if (verif(mij, s, q, v) > 0)    dr = mij - 1;
         else   st = mij + 1;
    }
    return dr;
}

int caut_bin_right(int st, int dr, char s[],
                   int q, pair <char, char> v[]) {
    int n = dr;
    while (st <= dr) {
        int mij = (st + dr) / 2;
        if (verif(mij, s, q, v) < n + 1)    st = mij + 1;
        else   dr = mij - 1;
    }
    return st;
}

int main() {
    int n, q;
    cin >> n >> q;
    char s[n + 2];
    s[0] = s[n + 1] = '0';
    for (int i = 1; i <= n; i ++)   cin >> s[i];
    pair <char, char> v[q + 1];
    for (int i = 0; i < q; i ++)    cin >> v[i].t >> v[i].d;
    cout << caut_bin_right(1, n, s, q, v) - 1 -
            caut_bin_left(1, n, s, q, v);
    return 0;
}
