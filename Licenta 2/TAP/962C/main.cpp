#include <iostream>
#include <queue>
#include <set>
using namespace std;
#define M 2000000009
queue <pair<int, string> > q;
set <int> sqr;

int string_to_int(basic_string<char> s) {
    int n = 0, p = 1;
    for (int i = 0; i < s.size() - 1; i ++) {
        n += s[i] - '0';
        n *= 10;
    }
    n += s[s.size() - 1] - '0';
    return n;
}

int main() {
    while (!q.empty())  q.pop();

    for (int i = 1; i * i < M; i ++) {
        sqr.insert(i * i);
    }

    string s;
    cin >> s;
    q.push({0, s});

    while (!q.empty()) {
        s = q.front().second;
        int n = string_to_int(s);
        if (sqr.find(n) != sqr.end()) {
            cout << q.front().first;
            return 0;
        }
        int p = q.front().first;
        q.pop();

        for (int i = 1; i < s.size(); i ++) {
            string s2 = s;
            s2.erase(i, 1);
            if (s2 != q.back().second) {
                q.push({p + 1, s2});
            }
        }
        s.erase(0, n=1);
        if (s[0] != '0' && s.size())    q.push({p + 1, s});
    }

    cout << "-1";
    return 0;
}