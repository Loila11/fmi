#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

bool verif(long long x, long long y) {
    while (y) {
        if (x % 2 == 0 && y % 2 == 1)   return false;
        x /= 2; y /= 2;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    pair<long long, long long> a[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> a[i].first;
    }
    for (int i = 0; i < n; i ++) {
        cin >> a[i].second;
    }
    sort(a, a + n);

    vector <long long> group;
    long long skill = 0;
    queue <int> q;
    for (int i = 1; i < n; i ++) {
        if (a[i].first == a[i - 1].first) {
            skill += a[i].second;
            a[i].second = -1;
            if (q.empty() || a[q.back()].first != a[i].first) {
                q.push(i);
                group.push_back(a[i].first);
                skill += a[i - 1].second;
                a[i - 1].second = -1;
            }
        }
    }

    while (!q.empty()) {
        int p = q.front();
        q.pop();

        for (int i = 0; i < n; i ++) {
            if (a[i].second != -1 && verif(a[p].first, a[i].first)) {
                q.push(i);
                group.push_back(a[i].first);
                skill += a[i].second;
                a[i].second = -1;
            }
        }
    }
    cout << skill;
    return 0;
}
