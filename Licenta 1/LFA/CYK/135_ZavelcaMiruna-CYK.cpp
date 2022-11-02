// g++ -std=c++14 main.cpp -o _main
#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <queue>
#include <stack>
using namespace std;

ifstream in ("date.in");

void citire (map <string, vector<char>> &v, int n) {
    for (int i = 0; i < n; i ++) {
        string x;
        in >> x;

        string str;
        for (int j = 1; j < x.size(); j ++) {
            if ((x[j] >= 'A' && x[j] <= 'Z') || (x[j] >= 'a' && x[j] <= 'z')) {
                str.push_back(x[j]);
            } else {
                if (str.size() > 0) {
                    v[str].push_back(x[0]);
                    str.clear();
                }
            }
        }

        if (str.size() > 0) {
            v[str].push_back(x[0]);
        }
    }
}

void verificare(map<string, vector<char>> v) {
    string s;
    in >> s;

    vector <pair <pair <int, int>, pair<int, int>>> a[s.size() + 1][s.size() + 1];
    vector <char> m[s.size() + 1][s.size() + 1];
    for (int linie = 0; linie < s.size(); linie ++) {
        for (int coloana = 0; coloana < s.size() - linie; coloana ++) {
            m[linie][coloana].clear();
            string str;

            if (linie == 0) {
                str.push_back(s[coloana]);
                for (int casuta = 0; casuta < v[str].size(); casuta++) {
                    m[linie][coloana].push_back(v[str][casuta]);
                }
            } else {
                for (int indice1 = 0; indice1 < linie; indice1 ++) {
                    if (m[indice1][coloana].empty())    continue;

                    for (int l = 0; l < m[indice1][coloana].size(); l ++) {

                        int indice2 = linie - indice1 - 1;
                        if (m[indice2][coloana + indice1 + 1].empty())    continue;

                        for (int h = 0; h < m[indice2][coloana + indice1 + 1].size(); h ++) {
                            str.clear();
                            str.push_back(m[indice1][coloana][l]);
                            str.push_back(m[indice2][coloana + indice1 + 1][h]);

                            for (int casuta = 0; casuta < v[str].size(); casuta ++) {
                                m[linie][coloana].push_back(v[str][casuta]);
                                a[linie][coloana].push_back({{indice1, coloana}, {indice2, coloana + indice1 + 1}});
                            }
                        }
                    }
                }
            }
        }
    }

    for (int i = 0; i < m[s.size() - 1][0].size(); i ++) {
        if (m[s.size() - 1][0][i] == 'S') {
            cout << "DA\n";
            cout << "S ";

            queue <pair<int, int>> q;
            q.push({s.size() - 1,0});

            while (!q.empty()) {
                auto x = a[q.front().first][q.front().second][i].first;
                auto y = a[q.front().first][q.front().second][i].second;

                cout << "(" << m[x.first][x.second][0] << ", " << m[y.first][y.second][0] << ") ";

                if (x.first != 0) {
                    q.push({x.first, x.second});
                }
                if (y.first != 0) {
                    q.push({y.first, y.second});
                }

                q.pop();
            }

            cout << "\n";

            return ;
        }
    }

    cout << "NU\n";
}

int main() {
    // alfabet A->Z
    int n;
    in >> n;

    map <string, vector<char>> v;
    citire (v, n);

    int m;
    in >> m;
    for (int i = 0; i < m; i ++) {
        verificare(v);
    }

    return 0;
}
