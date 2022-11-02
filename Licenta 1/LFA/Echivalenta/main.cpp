#include <fstream>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <vector>
using namespace std;

ifstream in ("date.in");
ofstream out ("date.out");

struct automat {
    int Q, E, F, q0, n;
    set <int> q, f;
    set <char> e;
    map <pair <int, char>, int> v;
};

void citire(int &n, set <int> &v) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        int stare;
        in >> stare;
        v.insert(stare);
    }
}

void citire(int &n, set <char> &v) {
    in >> n;
    for (int i = 1; i <= n; i++) {
        char litera;
        in >> litera;
        v.insert(litera);
    }
}

void citire(automat &a) {
    in >> a.n;
    for (int i = 1; i <= a.n; i++) {
        int stare_initiala, stare_finala;
        char litera;
        in >> stare_initiala >> litera >> stare_finala;
        a.v[{stare_initiala, litera}] = stare_finala;
    }
}

void citireT(automat &a) {
    citire(a.Q, a.q);
    citire(a.E, a.e);
    in >> a.q0;
    citire(a.F, a.f);
    citire(a);
}

bool verif(automat a, automat b, int qa, int qb) {
    return !((a.f.find(qa) != a.f.end() && b.f.find(qb) == b.f.end())
             || (a.f.find(qa) == a.f.end() && b.f.find(qb) != b.f.end()));

}

bool rezolvare(automat a, automat b) {
    if (verif(a, b, a.q0, b.q0) == 0) {
        return false;
    }

    set <pair <int, int>> viz;
    queue <pair <int, int>> q;

    q.push({a.q0, b.q0});
    viz.insert(q.front());

    while (!q.empty()) {
        pair <int, int> x = q.front();
        int qa, qb;
        q.pop();

        for (auto i = a.e.begin(); i != a.e.end(); i ++) {
            if (a.v.find({x.first, *i}) == a.v.end()) {
                qa = -1;
            } else {
                qa = a.v[{x.first, *i}];
            }

            if (b.v.find({x.second, *i}) == b.v.end()) {
                qb = -1;
            } else {
                qb = b.v[{x.second, *i}];
            }

            if (verif(a, b, qa, qb) == 0) {
                return false;
            }

            if (viz.find({qa, qb}) == viz.end()) {
                q.push({qa, qb});
                viz.insert({qa, qb});
            }
        }
    }
    return true;
}

int main() {
    automat a, b;
    citireT(a);
    citireT(b);
    if (rezolvare(a, b)) {
        out << "DA";
    } else {
        out << "NU";
    }

    return 0;
}
