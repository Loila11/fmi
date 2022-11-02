// Lab 1 GC
//
//de testat daca 3 puncte din R^3 sunt coliniare
//daca sunt, sa se scrie unul dintre ele ca si combinatie baricentrica (afina) de celelalte 2

#include <iostream>
using namespace std;

bool check(double a, double x1, double x2, double x3) {
    return x1 * a + x2 * (1 - a) == x3;
}

int main() {
    double x[4], y[4], z[4];

    for (int i = 1; i < 4; i ++) {
        cin >> x[i] >> y[i] >> z[i];
    }

    double a = 0;
    if (x[1] != x[2]) a = (x[3] - x[2]) / (x[1] - x[2]);
    else if (y[1] != y[2]) a = (y[3] - y[2]) / (y[1] - y[2]);
    else if (z[1] != z[2]) a = (z[3] - z[2]) / (z[1] - z[2]);
    else {
        cout << "Punctele sunt coliniare\n";
        cout << "P1 = 1 * P2 + (1 - 1) * P3";
        return 0;
    }

    if (check(a, x[1], x[2], x[3]) &&
        check(a, y[1], y[2], y[3]) &&
        check(a, z[1], z[2], z[3])) {
        cout << "Punctele sunt coliniare\n";
        if (a >= 0) cout << "P3 = " << a << " * P1 + (1 - " << a << ") * P2";
        else cout << "P3 = " << a << " * P1 + (1 - (" << a << ")) * P2";
    } else {
        cout << "Punctele nu sunt coliniare";
    }
    return 0;
}
