//Se dau punctele A1, A2, A3, A4.
// Verificati daca poligonul cu punctele A1, A2, A3, A4 (in aceasta ordine)
// este convex sau concav.
// Daca este convex, spuneti pozitia relativa a punctului A4 fata de
// cercul circumscris al triunghiului format de A1, A2 si A3
// (in cerc, pe cerc, sau in afara lui)

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;
#define x first
#define y second
double a[3], b[3], c[3];
pair<double, double> p[5];

void dreapta(int i, int j) {
    a[j] = p[i + 1].y - p[i].y;
    b[j] = p[i].x - p[i + 1].x;
    c[j] = p[i].y * p[i + 1].x - p[i].x * p[i + 1].y;
}

double det(double a1, double b1, double a2, double b2) {
    return a1 * b2 - a2 * b1;
}

bool intersectie () {
    double delta = det(a[1], b[1], a[2], b[2]);
    if (delta != 0) {
        double x = det(-c[1], b[1], -c[2], b[2]) / delta;
        double y = det(a[1], -c[1], a[2], -c[2]) / delta;
        if (x >= p[1].x && x <= p[2].x && x >= p[3].x && x <= p[4].x &&
            ((y >= p[1].y && y <= p[2].y) || (y <= p[1].y && y >= p[2].y)) &&
            ((y >= p[3].y && y <= p[4].y) || (y <= p[3].y && y >= p[4].y))) {
            return 1;
        }
    } else if (det(a[1], c[1], a[2], c[2]) == 0 && det(b[1], c[1], b[2], c[2]) == 0) {
        if (p[2].x == p[3].x && p[2].y == p[3].y) {
            return 1;
        } else if (p[4].x >= p[2].x && p[4].y >= p[2].y) {
            if (p[3].x <= p[1].x && p[3].y <= p[1].y) {
                return 1;
            } else if (p[3].x >= p[1].x && p[3].y >= p[1].y && p[3].x <= p[2].x && p[3].y <= p[2].y) {
                return 1;
            }
        } else if (p[4].x <= p[2].x && p[4].y <= p[2].y && p[4].x >= p[1].x && p[4].y >= p[1].y) {
            if (p[3].x <= p[1].x && p[3].y <= p[1].y) {
                return 1;
            } else if (p[3].x >= p[1].x && p[3].y >= p[1].y) {
                return 1;
            }
        }
    }
    return 0;
}

double square_x(int i) {
    return p[i].x * p[i].x;
}

double square_y(int i) {
    return p[i].y * p[i].y;
}

double Ssquare(double i) {
    return square_x(i) + square_y(i);
}

double square(double x) {
    return x * x;
}

double dist(double x, int j, int h) {
    return x * (p[j].y - p[h].y);
}

double afla_dist(int i, int j) {
    return sqrt(square(p[i].x - p[j].x) + square(p[i].y - p[j].y));
}

int main() {
    cin >> p[1].x >> p[1].y >> p[3].x >> p[3].y;
    cin >> p[2].x >> p[2].y >> p[4].x >> p[4].y;
    dreapta(1, 1);
    dreapta(3, 2);
    sort(p + 1, p + 3);
    sort(p + 3, p + 5);

    if(!intersectie()) {
        cout << "Poligonul nu este convex\n";
        return 0;
    }
    cout << "Poligonul este convex\n";

    double d = 2 * (dist(p[1].x, 2, 3) + dist(p[2].x, 3, 1) +  dist(p[3].x, 1, 2));
    p[0].x = (dist(Ssquare(1), 2, 3) + dist(Ssquare(2), 3, 1) + dist(Ssquare(3), 1, 2)) / d;
    p[0].y = (dist(Ssquare(1), 3, 2) + dist(Ssquare(2), 1, 3) + dist(Ssquare(3), 2, 1)) / d;

    double raza = afla_dist(0, 1);
    double distanta = afla_dist(0, 4);
    if (abs(distanta - raza) < 1e-8) {
        cout << "Punctul A4 se afla pe cerc.\n";
    } else if (distanta <= raza) {
        cout << "Punctul A4 se afla in cerc.\n";
    } else {
        cout << "Punctul A4 se afla in afara cercului.\n";
    }
    return 0;
}
