#include <iostream>
using namespace std;

char ask(int v[], int n) {
    cout << '?';
    for (int i = 0; i < n; i ++) {
        cout << ' ' << v[i];
    }
    cout << '\n' << flush;
    string s;
    cin >> s;
    return s[0];
}

void generate(int v[], int n, int x) {
    for (int i = 0; i < n; i ++) {
        v[i] = x + i + 1;
    }
}

int binary_search(char first_color, int n) {
    int left = 0, right = n;
    int v[n];
    while (left <= right) {
        int mid = (left + right) / 2;
        generate(v, n, mid);
        char color = ask(v, n);
        if (color == '-')   return -1;
        if (first_color != color) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return right;
}

int main() {
    int n;
    cin >> n;
    char sol[2 * n];
    int v[n];
    generate(v, n, 0);
    char first_color = ask(v, n);
    int poz = binary_search(first_color, n);
    sol[poz] = first_color;
    sol[poz + n] = 'R';
    if (first_color == 'R') sol[poz + n] = 'B';
    generate(v, n, poz);
    for (int i = 0; i < poz; i ++) {
        v[0] = i + 1;
        sol[i] = ask(v, n);
    }
    for (int i = poz + n + 1; i < 2 * n; i ++) {
        v[0] = i + 1;
        sol[i] = ask(v, n);
    }
    int j = 0;
    for (int i = 0; i < poz; i ++, j ++) {
        v[j] = i + 1;
    }
    for (int i = poz + n + 1; i < 2 * n; i ++, j ++) {
        v[j] = i + 1;
    }
    for (int i = poz + 1; i < poz + n; i ++) {
        v[j] = i + 1;
        sol[i] = ask(v, n);
    }
    sol[2 * n] = '\0';
    cout << "! " << sol;
    return 0;
}
