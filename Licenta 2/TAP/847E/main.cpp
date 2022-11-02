#include <iostream>
using namespace std;

bool check(int pasi, int n, char s[]) {
    int a = -1, viz[n + 1];
    for (int i = 0; i < n; i ++) {
        viz[i] = 0;
    }
    for (int i = 0; i < n; i ++) {
        if (i > 0)  viz[i] += viz[i - 1];
        if (s[i] == '*' && viz[i] == 0 && a == -1) a = i;
        if (s[i] == 'P') {
            int nxt = pasi;
            if (a != -1) {
                if (i - a > pasi) return false;
                nxt = max(pasi - 2 * (i - a), (pasi - i + a) / 2);
            }
            viz[i] ++;
            if (i + nxt + 1 < n)    viz[i + nxt + 1] --;
            a = -1;
        }
    }
    return a == -1;
}

int main() {
    int n;
    cin >> n;
    char s[n + 1];
    cin >> s;
    int st = 1, dr = 2 * n;
    while (st <= dr) {
        int mij = (st + dr) / 2;
        if (check(mij, n, s))   dr = mij - 1;
        else    st = mij + 1;
    }
    cout << dr + 1;
    return 0;
}
