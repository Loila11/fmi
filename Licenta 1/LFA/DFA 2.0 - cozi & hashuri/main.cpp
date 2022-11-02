#include <fstream>
#include <map>
#include <deque>
#include <vector>
using namespace std;

ifstream in ("date.in");
ofstream out ("date.out");

map <pair <int, char>, int> v;
deque <pair<int, char*>> h;

int Q, E, F, q0, n;
map <int, bool> q, f;
map <char, bool> e;

void citire_i(int &n, map <int, bool> &v) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        int x;
        in >> x;
        v[x] = true;
    }
}

void citire_c(int &n, map <char, bool> &v) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        char x;
        in >> x;
        v[x] = true;
    }
}

void citire_t() {
    in >> n;
    for (int i = 1; i <= n; i++) {
        int x, y;
        char z;
        in >> x >> z >> y;
        v[{x, z}] = y;
    }
}

void citire() {
    citire_i(Q, q);
    citire_c(E, e);
    in >> q0;
    citire_i(F, f);
    citire_t();
}

bool dfa(int q, char s[]) {
    pair <int, char*> r;
    h.emplace_back(q, s);

    while(!h.empty()) {
        r = h.front();
        h.pop_front();

        if (s[0] == '\0') {
            return f[q];
        }

        if (v.find({q, s[0]}) == v.end()) {
            return false;
        }

        return dfa(v[{q, s[0]}], s + 1);
    }
}

void clear() {
    while (!h.empty()) {
        h.pop_front();
    }
}

void rezolvare() {
    int t;
    in >> t;

    while (t --) {
        char s[1000];
        in >> s;

        clear();

        if (dfa(q0, s)) {
            out << "DA\n";
        } else {
            out << "NU\n";
        }
    }
}

int main() {
    citire();
    rezolvare();
    return 0;
}
