#include <fstream>
#include <vector>
using namespace std;

ifstream in ("sortaret.in");
ofstream out ("sortaret.out");

vector <int> fin;

void dfs(int nod, vector <int> v[], bool viz[]) {
    if (viz[nod] == true) return ;
    viz[nod] = true;

    //out << nod << " ";
    for (int i = 0; i < v[nod].size(); i ++) {
        dfs(v[nod][i], v, viz);
    }

    fin.push_back(nod);
}

int main() {
    int n, m;
    in >> n >> m;

    vector <int> v[n + 1];

    int x, y;
    for (int i = 0; i < m; i ++) {
        in >> x >> y;
        v[x].push_back(y);
    }

    bool viz[n + 1];
    for (int i = 1; i <= n; i ++) {
        viz[i] = false;
    }

    for (int i = 1; i <= n; i ++) {
        if (viz[i] == false) {
            dfs(i, v, viz);
        }
    }

    for (int i = fin.size() - 1; i >= 0; i --) {
         out << fin[i] << " ";
    }

    return 0;
}