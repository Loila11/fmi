#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

ifstream in ("grade.in");
ofstream out ("grade.out");

int main() {
    int n;
    in >> n;

    vector <pair <int, int>> v;
    for (int i = 0; i < n; i ++) {
        int x;
        in >> x;
        v.push_back({x, i + 1});
    }

    sort(v.begin(), v.end(), greater<>());

    for (int i = 0; i < v.size(); i ++) {
        for (int j = i + 1; j <= i + v[i].first; j ++) {
            v[j].first --;
            out << v[i].second << " " << v[j].second << '\n';
        }

        inplace_merge(v.begin(), v.begin() + i + v[i].first + 1, v.end(), greater<>());
    }

    return 0;
}