#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int a[n + 1], b[n + 1];
    for (int i = 0; i < n; i ++) {
        cin >> a[i];
    }

    int msum = n + 1;
    for (int aux1 = -1; aux1 <= 1; aux1 ++) {
        b[0] = a[0] + aux1;
        for (int aux2 = -1; aux2 <= 1; aux2 ++) {
            b[1] = a[1] + aux2;
            int sum = abs(aux2);
            int k = b[1] - b[0];
            bool pp1 = true;
            for (int i = 2; i < n; i ++) {
                b[i] = a[i];
                bool pp2 = false;
                for (int aux3 = -1; aux3 <= 1; aux3 ++) {
                    if (b[i] + aux3 - b[i - 1] == k) {
                        b[i] += aux3;
                        pp2 = true;
                        sum += abs(aux3);
                    }
                }

                if (!pp2) {
                    i = n;
                    pp1 = false;
                }
            }

            if (pp1) {
                sum += abs(aux1);
                if (sum < msum) {
                    msum = sum;
                }
            }
        }
    }

    if (msum == n + 1) {
        cout << "-1";
        return 0;
    }

    cout << msum;
    return 0;
}