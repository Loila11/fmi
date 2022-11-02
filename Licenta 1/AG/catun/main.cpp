#include <fstream>
#include <vector>
#include <queue>
using namespace std;

ifstream in ("catun.in");
ofstream out ("catun.out");

#define INF 1000000000

int main() {
    int n, m, k;
    in >> n >> m >> k;

    int dist[n + 1], tata[n + 1];
    bool viz[n + 1];
    for (int i = 1; i <= n; i ++) {
        dist[i] = INF;
        tata[i] = i;
        viz[i] = false;
    }

    priority_queue <pair <int, int>> pq;
    for (int i = 0; i < k; i ++) {
        int x;
        in >> x;
        dist[x] = 0;
        pq.push({0, x});
    }

    vector <pair <int, int>> muchie[n + 1];
    for (int i = 0; i < m; i ++) {
        int x, y, z;
        in >> x >> y >> z;
        muchie[x].push_back({y, z});
        muchie[y].push_back({x, z});
    }

    while (!pq.empty()) {
        int x = pq.top().second;
        pq.pop();

        if (viz[x]) continue;
        viz[x] = true;

        for (int i = 0; i < muchie[x].size(); i ++) {
            int nod = muchie[x][i].first, d = dist[x] + muchie[x][i].second;
            if (dist[nod] > d) {
                dist[nod] = d;
                tata[nod] = tata[x];
                pq.push({-d, nod});
            } else if (dist[nod] == d) {
                tata[nod] = min(tata[nod], tata[x]);
            }
        }
    }

    for (int i = 1; i <= n; i ++) {
        if (dist[i] == 0 || dist[i] == INF) {
            out << "0 ";
        } else {
            out << tata[i] << " ";
        }
    }

    return 0;
}