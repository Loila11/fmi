#include <fstream>
#include <vector>
using namespace std;
ifstream in("inel.in");
ofstream out("inel.out");

int v[20], total = 0;
bool viz[20], nr_prim[] = {0,0,1,1,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,1,0,0,0,0,0};
vector <int> sum_prim[20];

void bkt(int n, int p) {
    if (p == n + 1 && nr_prim[v[n] + 1]) {
        total ++;
    }
    for (int i = 0; i < sum_prim[v[p - 1]].size(); i ++) {
        int next = sum_prim[v[p - 1]][i];
        if (!viz[next]) {
            v[p] = next;
            viz[next] = true;
            bkt(n, p + 1);
            viz[next] = false;
        }
    }
}

int main() {
    int n;
    in >> n;
    v[1] = 1;   viz[1] = true;

    for (int i = 1; i < n; i ++) {
        for (int j = i + 1; j <= n; j ++) {
            if (nr_prim[i + j]) {
                sum_prim[i].push_back(j);
                sum_prim[j].push_back(i);
            }
        }
    }

    bkt(n, 2);
    out << total;
    return 0;
}