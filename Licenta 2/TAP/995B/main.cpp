#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int v[2 * n + 1], p[n + 1], t = 0;
    for (int i = 0; i < 2 * n; i ++) {
        cin >> v[i];
        p[v[i]] = i;
    }
    for (int i = 0; i < 2 * n; i += 2) {
        if (p[v[i]] != i + 1) {
            for (int j = p[v[i]]; j > i + 1; j --) {
                if (p[v[j - 1]] == j - 1) {
                    p[v[j - 1]] = j;
                }
                swap(v[j], v[j - 1]);
                t ++;
            }
        }
    }
    cout << t;
    return 0;
}