#include <iostream>
#include <cstring>
using namespace std;
#define N 200002
char a[4][N], sol[N];
int pp = 0;

void bkt(int i, int n, int v[4]) {
    if (i == n) {
        pp ++;
        strcpy(sol, a[1]);
        return ;
    }
    if (pp > 1) {
        return ;
    }

    if (a[1][i] == a[2][i] && a[2][i] == a[3][i]) {
        bkt(i + 1, n, v);
        return ;
    }

    if (a[1][i] != a[2][i] && a[2][i] != a[3][i] && a[1][i] != a[3][i]) {
        char aux1, aux2;
        for (int j = 1; j < 3; j ++) {
            for (int k = j + 1; k <= 3; k ++) {
                int l = 6 - j - k;
                if (v[j] + v[k] == 0) {
                    aux1 = a[j][i];     aux2 = a[k][i];
                    a[j][i] = a[l][i];  a[k][i] = a[l][i];
                    v[j] = 1;           v[k] = 1;
                    bkt(i + 1, n, v);
                    a[j][i] = aux1;     a[k][i] = aux2;
                    v[j] = 0;           v[k] = 0;
                }
            }
        }
        return ;
    }

    char aux;
    for (int j = 1; j < 3; j ++) {
        for (int k = j + 1; k <= 3; k ++) {
            int l = 6 - j - k;
            if (a[j][i] == a[k][i]) {
                if (v[l] == 0) {
                    aux = a[l][i];  a[l][i] = a[j][i];  v[l] = 1;
                    bkt(i + 1, n, v);
                    a[l][i] = aux;  v[l] = 0;
                }
                if (v[j] + v[k] == 0) {
                    aux = a[j][i];  a[j][i] = a[l][i];  a[k][i] = a[l][i];  v[j] = 1;   v[k] = 1;
                    bkt(i + 1, n, v);
                    a[j][i] = aux;  a[k][i] = aux;  v[j] = 0;   v[k] = 0;
                }
            }
        }
    }
}

int main ()
{
    cin >> a[1] >> a[2] >> a[3];
    if (strlen(a[1]) != strlen(a[2]) || strlen(a[2]) != strlen(a[3])) {
        cout << "Impossible";
        return 0;
    }

    if (strcmp(a[1], a[2]) == 0 && strcmp(a[2], a[3]) == 0) {
        cout << "Ambiguous";
        return 0;
    }

    int v[4] = {0, 0, 0, 0};
    bkt(0, strlen(a[1]), v);

    if (pp == 0) {
        cout << "Impossible";
    } else if (pp > 1) {
        cout << "Ambiguous";
    } else {
        cout << sol;
    }
    return 0;
}