#include <iostream>
#include <vector>
#include <algorithm>
#define N 100002
#define M 513
#define INF 1e9
using namespace std;
int b[M];
vector<pair<int, int> > a[N];

void citire(int &n, int &m) {
    cin >> n >> m;
    for (int i = 0; i < n; i ++) {
        int nr, masca = 0;
        cin >> nr;
        while (nr --) {
            int x;
            cin >> x;
            x --;
            masca += (1 << x);
        }
        b[masca] ++;
    }
    for (int i = 0; i < m; i ++) {
        int nr, c, masca = 0;
        cin >> c;
        cin >> nr;
        while (nr --) {
            int x;
            cin >> x;
            x --;
            masca += (1 << x);
        }
        a[masca].push_back({c, i});
    }

    for (int i = 0; i < M; i ++) {
        sort(a[i].begin(), a[i].end());
        while (a[i].size() > 2) {
            a[i].pop_back();
        }
    }
}

int main() {
    int n, m;
    citire(n, m);

    int ans_fin = 0, cost = 2 * INF + 1, pizza1 = -1, pizza2 = -1;
    for (int i = 0; i < M; i ++) {
        for(int j = 0; j < M; j ++) {
            int p1, p2, cost_curent = 0;
            if (i == j) {
                if (a[i].size() < 2)    continue;
                cost_curent = a[i][0].first + a[i][1].first;
                p1 = a[i][0].second;
                p2 = a[i][1].second;
            } else {
                if (a[i].size() == 0 || a[j].size() == 0)   continue;
                cost_curent = a[i][0].first + a[j][0].first;
                p1 = a[i][0].second;
                p2 = a[j][0].second;
            }

            int ans = 0, masca = i | j;
            for (int pp = 0; pp < M; pp ++) {
                if((masca & pp) == pp) {
                    ans += b[pp];
                }
            }

            if (ans > ans_fin || (ans == ans_fin && cost_curent < cost)) {
                ans_fin = ans;
                cost = cost_curent;
                pizza1 = p1;
                pizza2 = p2;
            }
        }
    }
    cout << pizza1 + 1 << " " << pizza2 + 1;
    return 0;
}