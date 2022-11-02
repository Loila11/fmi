#include <iostream>
#include <algorithm>
using namespace std;
#define l first
#define r second
#define N 10000007
bool is_taken[N];
int main() {
    int n;
    cin >> n;
    pair <pair<int, int>, int> v[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> v[i].l.r >> v[i].l.l;
        v[i].r = i;
    }
    sort(v, v + n);
    int sol[n + 1];
    for (int i = 0; i < n; i ++) {
        int j = v[i].l.r;
        while (is_taken[j] == 1)    j ++;
        is_taken[j] = 1;
        sol[v[i].r] = j;
    }
    for (int i = 0; i < n; i ++) {
        cout << sol[i] << ' ';
    }
    return 0;
}
