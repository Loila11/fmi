#include <iostream>
#include <vector>
using namespace std;

void base_change(vector<int> &v, int m, int w) {
    while (m) {
        v.push_back(m % w);
        m /= w;
    }
    v.push_back(0);
}

bool check() {
    int w, m;
    cin >> w >> m;
    vector<int> v;
    base_change(v, m, w);
    for (int i = 0; i < v.size(); i ++) {
        if (v[i] > 1) {
            if (v[i] == w - 1 || v[i] == w) {
                v[i + 1] ++;
            } else {
                return false;
            }
        }
    }
    return true;
}

int main() {
    if (check())    cout << "YES";
    else    cout << "NO";
    return 0;
}
