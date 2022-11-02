#include <fstream>
#include <vector>
#include <queue>
#include <map>
using namespace  std;

ifstream in("apm.in");
ofstream out("apm.out");

#define INF 2000

struct graf {
    vector <pair <int, int>> vecin;
};

struct graf2 {
    int y, c;
};

int main() {
    int n, m;
    in >> n >> m;

    graf v[n + 1];
    int x, y, c;
    for (int i = 0; i < m; i ++) {
        in >> x >> y >> c;
        v[x].vecin.push_back({y, c});
        v[y].vecin.push_back({x, c});
    }

    graf2 dist[n + 1];
    bool viz[n + 1];
    for (int i = 0; i < n; i ++) {
        dist[i].c = INF;
        dist[i].y = 0;
        viz[i] = false;
    }

    priority_queue <pair <int, pair <int, int>>> pq;
    int cost = 0;
    pq.push({0, {0, 1}});

    while(!pq.empty()) {
        int x = pq.top().second.second;
        c = -pq.top().first;
        pq.pop();

        if (viz[x] == true) continue;
        viz[x] = true;
        cost += c;

        for (int i = 0; i < v[x].vecin.size(); i ++) {
            c = v[x].vecin[i].second;
            y = v[x].vecin[i].first;
            if (c < dist[y].c && viz[y] == false) {
                dist[y].c = c;
                dist[y].y = x;
                pq.push({-c, {x, y}});
            }
        }
    }

    out << cost << "\n";
    for (int i = 2; i <= n; i ++) {
        out << i << " " << dist[i].y << endl;
    }

    return 0;
}