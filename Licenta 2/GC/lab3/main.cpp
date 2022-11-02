// Intersectia a doua segmente

#include <iostream>
#include <algorithm>
using namespace std;
#define x first
#define y second

void dreapta(int i, int j, pair <int, int> p[], int a[], int b[], int c[]) {
    cin >> p[i].x >> p[i].y >> p[i + 1].x >> p[i + 1].y;
    a[j] = p[i + 1].y - p[i].y;
    b[j] = p[i].x - p[i + 1].x;
    c[j] = p[i].y * p[i + 1].x - p[i].x * p[i + 1].y;
}

int det(int a1, int b1, int a2, int b2) {
    return a1 * b2 - a2 * b1;
}

void afis_segment(pair<int, int> p[], int i, int j) {
    cout << "Intersectia este segmentul: [(" << p[i].x << ", " << p[i].y << "), (" << p[j].x << ", " << p[j].y << ")]";
}

int main() {
    int a[3], b[3], c[3];
    pair<int, int> p[5];
    dreapta(1, 1, p, a, b, c);
    dreapta(3, 2, p, a, b, c);
    sort(p + 1, p + 3);
    sort(p + 3, p + 5);
    int delta = det(a[1], b[1], a[2], b[2]);
    if (delta != 0) {
        int x = det(-c[1], b[1], -c[2], b[2]) / delta;
        int y = det(a[1], -c[1], a[2], -c[2]) / delta;
        if (x >= p[1].x && x <= p[2].x && x >= p[3].x && x <= p[4].x &&
            ((y >= p[1].y && y <= p[2].y) || (y <= p[1].y && y >= p[2].y)) &&
            ((y >= p[3].y && y <= p[4].y) || (y <= p[3].y && y >= p[4].y))) {
            cout << "Intersectia este punctul: (" << x << ", " << y << ")";
            return 0;
        }
    } else if (det(a[1], c[1], a[2], c[2]) == 0 && det(b[1], c[1], b[2], c[2]) == 0) {
        if (p[2].x == p[3].x && p[2].y == p[3].y) {
            cout << "Intersectia este punctul: (" << p[2].x << ", " << p[2].y << ")";
            return 0;
        } else if (p[4].x >= p[2].x && p[4].y >= p[2].y) {
            if (p[3].x <= p[1].x && p[3].y <= p[1].y) {
                afis_segment(p, 1, 2);
                return 0;
            } else if (p[3].x >= p[1].x && p[3].y >= p[1].y && p[3].x <= p[2].x && p[3].y <= p[2].y) {
                afis_segment(p, 3, 2);
                return 0;
            }
        } else if (p[4].x <= p[2].x && p[4].y <= p[2].y && p[4].x >= p[1].x && p[4].y >= p[1].y) {
            if (p[3].x <= p[1].x && p[3].y <= p[1].y) {
                afis_segment(p, 3, 1);
                return 0;
            } else if (p[3].x >= p[1].x && p[3].y >= p[1].y) {
                afis_segment(p, 3, 4);
                return 0;
            }
        }
    }
    cout << "Intersectia e multimea vida";
    return 0;
}
