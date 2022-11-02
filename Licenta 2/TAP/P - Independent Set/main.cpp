#include <iostream>
#include <vector>
using namespace std;
#define N 100002
#define MOD 1000000007
vector <int> v[N];
bool viz[N];

void dfs(int n, int i, long long &dpa, long long &dpn) {
    viz[i] = true;
    long long da = 1, dn = 1;
    for (int j : v[i]) {
        if (!viz[j]) {
            dfs(n, j, dpa, dpn);
            da = da * (dpa + dpn) % MOD;
            dn = dn * dpa % MOD;
        }
    }
    dpa = da;
    dpn = dn;
}

int main() {
    int n;
    cin >> n;
    for (int i = 1; i < n; i ++) {
        int x, y;
        cin >> x >> y;
        v[x].push_back(y);
        v[y].push_back(x);
    }
    int root = 0;
    for (int i = 1; i <= n && root == 0; i ++) {
        if (v[i].size() == 1) {
            root = i;
        }
    }
    long long dpa = 0, dpn = 0;
    dfs(n, root, dpa, dpn);
    cout << (dpa + dpn) % MOD;
    return 0;
}
