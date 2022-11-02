#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int n;
    cin >> n;
    pair <int, int> v[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> v[i].first >> v[i].second;
        if (v[i].second < v[i].first) {
            swap(v[i].first, v[i].second);
        }
    }
    sort(v, v + n);
    int segm = 0, w[n + 1], end = v[0].second;
    for (int i = 1; i < n; i ++) {
        if (v[i].first > end) {
            w[segm] = end;
            segm ++;
            end = v[i].second;
        } else if (v[i].second < end) {
            end = v[i].second;
        }
    }
    w[segm] = end;
    segm ++;
    cout << segm << '\n';
    for (int i = 0; i < segm; i ++) {
        cout << w[i] << ' ';
    }
    return 0;
}