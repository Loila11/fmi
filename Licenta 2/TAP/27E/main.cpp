#include <iostream>
#include <limits>
using namespace std;
#define N 10
#define INF numeric_limits<unsigned long long>::max()
int v[N + 1] = {0, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29}, viz[N + 1];
unsigned long long sol_m = INF;

int div_number(int p) {
    int sol = 1;
    for (int i = 1; i <= p; i ++)   sol *= (viz[i] + 1);
    return sol;
}

unsigned long long calc_number(int p) {
    unsigned long long sol = 1, ver;
    for (int i = 1; i <= p; i ++) {
        for (int j = 0; j < viz[i]; j ++) {
            ver = sol;
            sol *= v[i];
            if (sol < ver)  return INF;
        }
    }
    return sol;
}

void bkt(int p, int n) {
    int x = div_number(p);
    if (x == n) sol_m = min(sol_m, calc_number(p));
    if (x >= n) return ;

    for (int i = 1; i <= viz[p - 1]; i ++) {
        viz[p] = i;
        bkt(p + 1, n);
        viz[p] = 0;
    }
}

int main() {
    int n;
    cin >> n;
    viz[0] = 60;
    bkt(1, n);

    cout << sol_m;
    return 0;
}
