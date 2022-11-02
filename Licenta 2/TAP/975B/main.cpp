#include <iostream>
using namespace std;
#define n 14
int main() {
    int v[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> v[i];
    }

    long long best = 0;
    for (int i = 0; i < n; i ++) {
        long long j = i + 1, nr = v[i], sum = 0, x = v[i], c = nr / n, r = nr % n;
        v[i] = 0;
        while (nr) {
            if (j == n) {
                j = 0;
            }
            bool pp = r > 0;
            long long aux = v[j] + c + pp;
            if (aux % 2 == 0) {
                sum += aux;
            }
            nr -= c + pp;
            j ++;
            r --;
        }
        v[i] = x;
        if (sum > best) {
            best = sum;
        }
    }

    cout << best;
    return 0;
}

/*
0 0 0 0 0 0 0 0 0 0 0 0 0 14
 */