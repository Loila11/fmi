#include <fstream>
#include <algorithm>
using namespace std;
ifstream in("joben.in");
ofstream out("joben.out");

bool check() {
    string s1, s2;
    in >> s1 >> s2;
    int c1[27], c2[27];
    for (int i = 0; i < 27; i ++) {
        c1[i] = 0;
        c2[i] = 0;
    }
    for (int i = 0; i < s1.size(); i ++) {
        c1[s1[i] - 'a'] ++;
        c2[s2[i] - 'a'] ++;
    }
    sort(c1, c1 + 27);
    sort(c2, c2 + 27);
    for (int i = 1; i < 27; i ++) {
        if (c1[i] != c2[i]) return false;
    }
    return true;
}

int main() {
    int t;
    in >> t;
    while (t --) {
        if(check()) {
            out << "DA\n";
        } else {
            out << "NU\n";
        }
    }
    return 0;
}