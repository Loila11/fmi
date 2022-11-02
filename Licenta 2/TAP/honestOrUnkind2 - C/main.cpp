#include <iostream>
using namespace std;
#define N 16
pair<int, int> v[N][N];
int l[N];

bool bit_find(int number, int pos) {
    return number & (1 << pos);
}

int bit_count(int number, int n) {
    int sol = 0;
    for (int i = 0; i < n; i ++) {
        sol += bit_find(number, i);
    }
    return sol;
}

bool check(int number, int n) {
    for (int i = 0; i < n; i ++) {
        int pp = bit_find(number, i), p = 1;
        for (int j = 0; j < l[i]; j ++) {
            if (v[i][j].second != bit_find(number, v[i][j].first)) {
                if (pp) return false;
                p = 0;
            }
        }
        if (pp != p)    return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> l[i];
        for (int j = 0; j < l[i]; j ++) {
            cin >> v[i][j].first >> v[i][j].second;
            v[i][j].first --;
        }
    }
    int fin = (1 << n), sol = 0;
    for (int i = 0; i < fin; i ++) {
        if (check(i, n)) {
            sol = max(sol, bit_count(i, n));
        }
    }
    cout << sol;
    return 0;
}
