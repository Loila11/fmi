#include <iostream>
using namespace std;

void ask(int a, int b) {
    cout << "? " << a << ' ' << b << '\n' << flush;
}

bool check(int a, int b, int v[]) {
    bool ppa = 0, ppb = 0;
    for (int i = 1; i < 7; i ++) {
        if (v[i] == a)  ppa = 1;
        else if (v[i] == b) ppb = 1;
    }
    return ppa * ppb == 1;
}

void half(int x, int a[], int v[]) {
    int aux1, aux2;
    ask(x, x + 1);
    cin >> aux1;
    ask(x + 1, x + 2);
    cin >> aux2;
    int aux = aux1 * aux2;
    for (int i = 1; i < 7; i ++) {
        if (aux % (v[i] * v[i]) == 0) {
            a[x + 1] = v[i];
            v[i] = 19;
            if (check(aux1 / a[x + 1], aux2 / a[x + 1], v)) {
                a[x] = aux1 / a[x + 1];
                a[x + 2] = aux2 / a[x + 1];
                return ;
            }
            else    v[i] = a[x + 1];
        }
    }
}

int main() {
    int v[7] = {0, 4, 8, 15, 16, 23, 42};
    int a[7] = {0, 0, 0, 0, 0, 0, 0};
    half(1, a, v);
    half(4, a, v);
    cout << "!";
    for (int i = 1; i < 7; i ++) {
        cout << ' ' << a[i];
    }
    return 0;
}
