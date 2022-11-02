#include <fstream>
using namespace std;

ifstream in ("semne3.in");
ofstream out ("semne3.out");

int main () {
    int n;
    string s;
    in >> n >> s;

    int v[n + 1];
    
    v[0] = 1;
    v[1] = -1;
    for (int i = 2; i <= n; i ++) {
        v[i] = 0;
    }
    
    int fin = 0, poz = 1;

    for (int i = 0; i < s.size(); i++) {
        if (s[i] == '<') {
            poz = i + 2;
            fin = i + 1;
        } else {
            v[fin] ++;
            v[i + 1] --;
        }

        v[i + 1] += poz;
        v[i + 2] -= poz;
    }

    out << v[0] << " ";
    for (int i = 1; i < n; i++) {
        v[i] += v[i - 1];
        out << v[i] << " ";
    }

    return 0;
}
