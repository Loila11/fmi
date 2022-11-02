#include <fstream>
#include <algorithm>
#include <vector>
using namespace std;
ifstream in("nogame.in");
ofstream out ("nogame.out");

int opr_bin(int ba, int bb, int op) {
    if ((ba + bb == 0 && op >= 8) || (ba == 0 && bb == 1 && (op / 4) % 2 == 1) ||
        (ba == 1 && bb == 0 && (op / 2) % 2 == 1) || (ba + bb == 2 && op % 2 == 1)) {
            return 1;
    }
    return 0;
}

int opr(int a, int b, int op) {
    int p = 1, nr = 0;
    while (a || b) {
        int c = opr_bin(a % 2, b % 2, op);
        nr += c * p;
        p *= 2;    a /= 2;    b /= 2;
    }
    return nr;
}

bool egal(vector<int> v[16], vector<int> w[16], int n) {
    for (int i = 0; i < 16; i ++) {
        for (int j = 0; j < n; j ++) {
            if (v[i][j] != w[i][j]) {
                return 0;
            }
        }
    }
    return 1;
}

void afisare(vector<int> v[16], int n) {
    for (int i = 0; i < 16; i ++) {
        for (int j = 0; j < n; j ++) {
            out << v[i][j] << " ";
        }
        out << endl;
    }
}

int main() {
    int t;
    in >> t;
    while (t --) {
        int n;
        in >> n;
        vector<int> v[17];
        for (int i = 0; i < 16; i ++) {
            for (int j = 0; j < n; j ++) {
                int x;
                in >> x;
                v[i].push_back(x);
            }
        }

        bool pp = false;
        sort(v, v + 16);

        for (int i = 0; i < 16; i ++) {              // selectez vectorul de verificat
            vector <int> w[17];
            for (int ind = 0; ind < 16; ind ++) {   // indicele vectorului / operatiei la care am ajuns
                w[ind].push_back(v[0][0]);
                for (int j = 1; j < n; j++) {       // la al catelea element din vector sunt
                    w[ind].push_back(opr(w[ind][j - 1], v[i][j], ind));
                }
            }
            sort(w, w + 16);

            if (egal(v, w, n)) {
                for (int j = 0; j < n; j++) {
                    out << w[i][j] << " ";
                }
                pp = true;
                i = 16;
            }
        }

        if (!pp) {
            out << "-1";
        }
        out << '\n';
    }
    return 0;
}