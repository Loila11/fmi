#include <iostream>
using namespace std;

void find_min(int x, int &min) {
    char c;
    cout << "? " << x << ' ' << min << '\n' << flush;
    cin >> c;
    if (c == '<')   min = x;
}

void find_max(int x, int &max) {
    char c;
    cout << "? " << x << ' ' << max << '\n' << flush;
    cin >> c;
    if (c == '>')   max = x;
}

int main() {
    int t;
    cin >> t;
    while (t --) {
        int n;
        cin >> n;
        if (n == 1) cout << "! 1 1\n" << flush;
        else {
        int a[n + 1], b[n + 1], l = 0;
        char c;
        for (int i = 2; i <= n; i += 2) {
            cout << "? " << i - 1 << ' ' << i << '\n' << flush;
            cin >> c;
            l ++;
            if (c == '<') {
                a[l] = i - 1;
                b[l] = i;
            } else {
                a[l] = i;
                b[l] = i - 1;
            }
        }

        int min = a[1], max = b[1];
        for (int i = 2; i <= n / 2; i ++) {
            find_min(a[i], min);
            find_max(b[i], max);
        }

        if (n % 2 != 0) {
            find_min(n, min);
            find_max(n, max);
        }

        cout << "! " << min << ' ' << max << '\n' << flush;
    }}
    return 0;
}
