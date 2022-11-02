#include <fstream>
#include <algorithm>
#include <set>
using namespace std;
ifstream in("arbsat2.in");
ofstream out("arbsat2.out");
set<pair<int, int>> sol;

void div_et_imp(pair<int, int> v[], int left, int right) {
    if (left >= right)  return ;
    int mid = (left + right) / 2;
    div_et_imp(v, left, mid);
    div_et_imp(v, mid + 1, right);
    for (int i = left; i < right; i ++) {
        if (v[mid].first != v[i].first) {
            sol.insert({v[mid].first, v[i].second});
        }
    }
}

int main() {
    int n, m;
    in >> n >> m;
    pair<int, int> v[n];
    for (int i = 0; i < n; i ++) {
        in >> v[i].first >> v[i].second;
    }
    sort(v, v + n);
    div_et_imp(v, 0, n);
    out << sol.size() << '\n';
    for (auto it = sol.begin(); it != sol.end(); it ++) {
        out << it->first << ' ' << it->second << '\n';
    }
    return 0;
}
