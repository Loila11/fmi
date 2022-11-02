#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
char t[2000000];
int main() {
    int n, m = 0;
    cin >> n;
    for (int i = 0; i < n; i ++) {
        string s;
        int l, x, prev = 1;
        cin >> s >> l;
        for (int j = 0; j < l; j ++) {
            cin >> x;
            m = max(m, x + (int)s.size());
            for (int k = max(0, prev - x); k < s.size(); k ++) {
                t[k + x] = s[k];
            }
            prev = max(prev, x + (int)s.size());
        }
    }

    for (int i = 1; i < m; i ++) {
        if (!t[i]) t[i] = 'a';
        cout << t[i];
    }
    return 0;
}
