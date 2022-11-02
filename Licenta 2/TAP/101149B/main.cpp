#include <iostream>
#include <algorithm>
using namespace std;
#define b first
#define a second

bool sort_min (pair <long long, long long> a, pair <long long, long long> b) {
    return (a.a - a.b) > (b.a - b.b);
}

int main() {
    int n;
    cin >> n;
    pair <long long, long long> v[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> v[i].a >> v[i].b;
    }
    sort(v, v + n, sort_min);
    long long sol = v[0].a, curr = sol - v[0].b;
    for (int i = 1; i < n; i ++) {
        if (curr < v[i].a) {
            sol += v[i].a - curr;
            curr = v[i].a;
        }
        curr -= v[i].b;
    }
    cout << sol;
    return 0;
}
