#include <iostream>
#include <algorithm>
using namespace std;
int v[1004];

int caut_bin(int st, int fin, int sum) {
    int p = st;
    while (st <= fin) {
        int mij = (st + fin) / 2;
        if (v[mij] >= sum) {
            fin = mij - 1;
        } else {
            st = mij + 1;
        }
    }
    return st - p;
}

int main() {
    int n;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        cin >> v[i];
    }
    int sum = 0;
    sort(v, v + n);
    for (int i = 0; i < n; i ++) {
        for (int j = i + 1; j < n; j ++) {
            sum += caut_bin(j + 1, n - 1, v[i] + v[j]);
        }
    }
    cout << sum;
    return 0;
}