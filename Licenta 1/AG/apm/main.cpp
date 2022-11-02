#include <fstream>
#include <set>
#include <map>
using namespace std;

#define MAX 400100

ifstream in ("apm.in");
ofstream out ("apm.out");

set <pair <int, pair<int, int>>> muchii;
int tata[MAX];

void citire(int &n, int &m) {
    in >> n >> m;

    int x, y, c;
    for (int i = 0; i < m; i ++) {
        in >> x >> y >> c;
        muchii.insert({c, {x, y}});
    }
}

void createTata(int n) {
    for (int i = 1; i <= n; i ++) {
        tata[i] = i;
    }
}

int findTata(int x) {
    if (tata[x] == x)
        return x;

    tata[x] = findTata(tata[x]);
    return tata[x];
}

int main() {
    int n, m;
    citire(n, m);
    createTata(n);

    int cost = 0;
    for (auto i = muchii.begin(); i != muchii.end();) {
        int x = findTata(i->second.first), y = findTata(i->second.second);
        if (x != y) {
            tata[y] = x;
            cost += i->first;
            i ++;
        } else {
            i = muchii.erase(i);
        }
    }

    out << cost << '\n' << muchii.size() << '\n';
    for (auto i = muchii.begin(); i != muchii.end(); i ++) {
        out << i->second.first << " " << i->second.second << '\n';
    }

    return 0;
}