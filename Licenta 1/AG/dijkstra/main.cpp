#include <fstream>
#include <vector>
#include <queue>
using namespace std;

#define INF 1000000000

ifstream in ("dijkstra.in");
ofstream out ("dijkstra.out");

int main() {
    int n, m;
    in >> n >> m;

    vector <pair <int, int>> muchii[n + 1];
    int viz[n + 1], dist[n + 1];

    for (int i = 1; i <= n; i ++) {
        viz[i] = false;
        dist[i] = INF;
    }

    for (int i = 0; i < m; i ++) {
        int x, y, c;
        in >> x >> y >> c;
        muchii[x].push_back({y, c});
    }

    priority_queue <pair<int, int>> q;
    q.push({0, 1});
    dist[1] = 0;

    while(!q.empty()) {
        int x = q.top().second;
        q.pop();

        if (viz[x] != 0) continue;
        viz[x] = true;

        for (auto y : muchii[x]) {
            int d = dist[x] + y.second;
            if (d < dist[y.first]) {
                dist[y.first] = d;
                q.push({-d, y.first});
            }
        }
    }

    for (int i = 2; i <= n; i ++) {
        if (dist[i] == INF) {
            out << "0 ";
        } else {
            out << dist[i] << " ";
        }
    }

    return 0;
}
