#include <fstream>
using namespace std;
ifstream in("pic.in");
ofstream out("pic.out");

void var1() {
    int n, x, sol = 0, l = 0;
    in >> n;
    for (int i = 0; i < n; i ++) {
        int s = 0;
        for (int j = 0; j <= i; j ++) {
            in >> x;
            s += x;
        }
        if (s > sol) {
            sol = s;
            l = i + 1;
        }
    }
    out << l;
}

void var2() {
    int n;
    in >> n;
    int v[n][n], sum = 0;
    for (int i = 0; i < n; i ++) {
        for (int j = 0; j <= i; j++) {
            in >> v[i][j];
            sum += v[i][j];
        }
    }
}

int main() {
    int V;
    in >> V;
    if (V == 1) {
        var1();
    } else {
        var2();
    }
    return 0;
}
