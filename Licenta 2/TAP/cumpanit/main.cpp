#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
ifstream in("cumpanit.in");
ofstream out("cumpanit.out");
#define N 12
int prim[N] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
vector <long long> v;
long long a, b;

void bkt(int p, long long put, long long sum_baz, long long sum_exp) {
    if (put > b)    return ;
    if (p == N) {
        if (sum_exp == sum_baz && put >= a) v.push_back(put);
        return;
    }

    bkt(p + 1, put, sum_baz, sum_exp);
    int i = 1;
    put *= prim[p];
    while (put <= b) {
        bkt(p + 1, put, sum_baz + prim[p], sum_exp + i);
        put *= prim[p];
        i ++;
    }
}

int main() {
    in >> a >> b;
    bkt(0, 1, 0, 0);
    sort(v.begin(), v.end());
    for (auto i : v)    out << i << '\n';
    return 0;
}
