#include <iostream>
#include <GL/freeglut.h>
#include <algorithm>
#include <iomanip>
#include "Graphics.h"
using namespace std;
#define CIRCLE_SIZE 5

int n, i, ind, k;
double MAX,X,Y;

struct puncte{
    double x, y;
} v[120010], p, st[120010];

double afla(puncte a, puncte b, puncte c){
    return (a.x * b.y + b.x * c.y + c.x * a.y) - (c.x * b.y + c.y * a.x + b.x * a.y);
}

bool cmp(puncte a, puncte b){
    if (afla(v[1], a, b) > 0) {
        return 1;
    }
    return 0;
}

double schimb_y(double x) {
    return WINDOW_HEIGHT / 10 + x * (WINDOW_HEIGHT - WINDOW_X) / MAX;
}

double schimb_x(double x) {
    return WINDOW_WIDTH / 10 + x * (WINDOW_HEIGHT - WINDOW_Y) / MAX;
}

void drawScene() {
    clearWindow();
    setColor(RED);
    for (i = 1; i <= n; ++i){
        if(v[i].x == X && v[i].y == Y){
            setColor(BLUE);
            drawFilledCircle(schimb_x(v[i].x), schimb_y(v[i].y), CIRCLE_SIZE);
            setColor(RED);
        }
        else
            drawFilledCircle(schimb_x(v[i].x), schimb_y(v[i].y), CIRCLE_SIZE);
    }

    setColor(BLACK);
    st[0] = st[k];
    for (i = k; i > 0; --i) {
        if ((st[i - 1].x == X && st[i - 1].y == Y) ||
            (st[i].x == X && st[i].y == Y)){
            setColor(GREEN);
            drawLine(schimb_x(st[i - 1].x), schimb_y(st[i - 1].y),
                     schimb_x(st[i].x), schimb_y(st[i].y));
            setColor(BLACK);
        }
        else
            drawLine(schimb_x(st[i - 1].x), schimb_y(st[i - 1].y),
                     schimb_x(st[i].x), schimb_y(st[i].y));
        if(st[i].x == X && st[i].y == Y){
            setColor(GREEN);
            drawFilledCircle(schimb_x(st[i].x), schimb_y(st[i].y), CIRCLE_SIZE);
            setColor(BLACK);
        }
        else{
            setColor(BLACK);
            drawFilledCircle(schimb_x(st[i].x), schimb_y(st[i].y), CIRCLE_SIZE);
            setColor(BLACK);
        }

    }
    glEnd();
    glutSwapBuffers();
}

int main(int argc, char ** argv){
    cout << "Coordonatele punctului:\n";
    cin >> v[1].x >> v[1].y;
    X = v[1].x;
    Y = v[1].y;
    cout << "Numarul de puncte ale poligonului:\n";
    cin >> n;
    cout << "Punctele poligonului:\n";
    n++;
    p.x = v[1].x;
    p.y = v[1].y;
    for (i = 2; i <= n; ++i) {
        cin >> v[i].x >> v[i].y;
        if (v[i].x < p.x || (v[i].x == p.x && v[i].y < p.y) ) {
            p = v[i];
            ind = i;
        }
    }
    swap (v[1], v[ind]);
    sort (v + 2, v + n + 1, cmp);
    st[++k] = v[1];
    st[++k] = v[2];
    for (i = 3; i <= n; ++i) {
        while (k >= 2 && afla(st[k - 1], st[k], v[i]) < 0) {
            --k;
        }
        st[++k] = v[i];
    }
    cout << "Varfurile acoperirii convexe Conv(P U {A}) (ca lista ordonata, parcursa in sens trigonometric) sunt:\n";
    for (i = k; i > 0; --i) {
        MAX = max(MAX, st[i].x);
        MAX = max(MAX, st[i].y);
        cout << setprecision(6) << st[i].x << " " << st[i].y << "\n";
    }
    cout << "Explicatii desen : \n"
            "Punct Rosu - punct in set, dar nu in infasuratoare\n"
            "Punct Albastru - punctul dat daca e in interior\n"
            "Punct Verde - punctul dat daca e in afara poligonului\n"
            "Punct Negru - punct in set si in infasuratoare\n"
            "Linie Neagra - segment intre 2 puncte din set\n"
            "Linie Verde - segment cu un capat in punctul dat\n";
    graphicsSetup(argc, argv);
    glutDisplayFunc(drawScene);
    glutMainLoop();
    return 0;
}
