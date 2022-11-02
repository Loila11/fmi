// Lab 2 GC
//
//Se dau 4 puncte distincte in R^2
//
//Sa se determine 2 multimi I, J ai
//1) I U J = {A1, A2, A3, A4}
//2) I intersect J = mult vida
//3) Conv(I) intersect Conv(J) != mult vida
//
//Cazuri:
// -  patrulater convex :
//    I = diag 1, J = diag 2
// -  triunghi:
//    I = varfurile, J = punctul din interior
// -  segment:
//    I = capetele, J = celelalte

#include <iostream>
#include <cmath>
using namespace std;
#define x first
#define y second

void afisare(pair<double, double> a) {
    cout << "(" << a.x << "," << a.y << ")";
}

double coliniare(pair<double, double> a, pair<double, double> b, pair<double, double> c) {
    double det = a.x * b.y + b.x * c.y + c.x * a.y - a.x * c.y - b.x * a.y - c.x * b.y;
    return det;
}

double arie_triunghi(pair<double, double> a, pair<double, double> b, pair<double, double> c) {
    double arie = abs((b.y - a.y) * c.x - (b.x - a.x) * c.y - (b.y - a.y) * a.x + (b.x - a.x) * a.y);
    return (arie / 2);
}
void afisare_coliniare(pair<double, double> a[5]) {
    for (int i = 1; i < 5; i ++) {
        for (int j = i + 1; j < 5; j ++) {
            if (a[j].x < a[i].x || (a[i].x == a[j].x && a[i].y > a[j].y)) {
                pair<double, double> aux = a[i];
                a[i] = a[j];
                a[j] = aux;
            }
        }
    }

    cout << "I = {";
    afisare(a[1]);
    cout << ", ";
    afisare(a[4]);
    cout << "}\nJ = {";
    afisare(a[2]);
    cout << ", ";
    afisare(a[3]);
    cout << "}";
}

bool triunghi(pair<double, double> a[5]) {
    double a1 = arie_triunghi(a[1], a[2], a[3]);
    double a2 = arie_triunghi(a[1], a[2], a[4]);
    double a3 = arie_triunghi(a[1], a[3], a[4]);
    double a4 = arie_triunghi(a[2], a[3], a[4]);
    if (a1 + a2 + a3 == a4) {
        cout << "I = {";
        afisare(a[4]);
        cout << ", ";
        afisare(a[2]);
        cout << ", ";
        afisare(a[3]);
        cout << "}\nJ = {";
        afisare(a[1]);
        cout << "}";
        return true;
    } else if (a1 + a2 + a4 == a3) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[4]);
        cout << ", ";
        afisare(a[3]);
        cout << "}\nJ = {";
        afisare(a[2]);
        cout << "}";
        return true;
    } else if (a1 + a4 + a3 == a2) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[2]);
        cout << ", ";
        afisare(a[4]);
        cout << "}\nJ = {";
        afisare(a[3]);
        cout << "}";
        return true;
    } else if (a4 + a2 + a3 == a1) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[2]);
        cout << ", ";
        afisare(a[3]);
        cout << "}\nJ = {";
        afisare(a[4]);
        cout << "}";
        return true;
    }
    return false;
}

void patrulater(pair<double, double> a[5]) {
    if (coliniare(a[1], a[2], a[3]) * coliniare(a[1], a[2], a[4]) < 0) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[2]);
        cout << "}\nJ = {";
        afisare(a[3]);
        cout << ", ";
        afisare(a[4]);
        cout << "}";
    } else if (coliniare(a[1], a[3], a[2]) * coliniare(a[1], a[3], a[4]) < 0) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[3]);
        cout << "}\nJ = {";
        afisare(a[2]);
        cout << ", ";
        afisare(a[4]);
        cout << "}";
    } else if (coliniare(a[1], a[4], a[3]) * coliniare(a[1], a[4], a[2]) < 0) {
        cout << "I = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[4]);
        cout << "}\nJ = {";
        afisare(a[3]);
        cout << ", ";
        afisare(a[2]);
        cout << "}";
    } else {
        cout << "I = {";
        afisare(a[3]);
        cout << ", ";
        afisare(a[2]);
        cout << "}\nJ = {";
        afisare(a[1]);
        cout << ", ";
        afisare(a[4]);
        cout << "}";
    }
}

int main() {
    pair<double, double> a[5];
    for (int i = 1; i < 5; i ++) {
        cin >> a[i].x >> a[i].y;
    }
    if (coliniare(a[1], a[2], a[3]) == 0 && coliniare(a[1], a[2], a[4]) == 0) {
        afisare_coliniare(a);
    } else if (!triunghi(a)) {
        patrulater(a);
    }
    return 0;
}
