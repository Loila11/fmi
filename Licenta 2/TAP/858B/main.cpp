#include <iostream>
using namespace std;
int main() {
    int n, m, nf = -1;
    cin >> n >> m;
    pair<int, int> v[m];
    for (int i = 0; i < m; i ++) {
        cin >> v[i].first >> v[i].second;
    }

    for (int f = 1; f <= 100; f ++) {
        bool pp = 1;
        for (int i = 0; i < m; i ++) {
            if ((v[i].first - 1) / f + 1 != v[i].second) {
                pp = 0;
                i = m;
            }
        }

        if (pp == 1) {
            if (nf != -1 &&  (n - 1) / f + 1 != nf) {
                cout << "-1";
                return 0;
            }
            nf = (n - 1) / f + 1;
        }
    }

    cout << nf;

    return 0;
}