#include <iostream>
using namespace std;
int main() {
    long long r, y;
    cin >> r;
    for (long long x = 1; x*x < r; x ++) {
        y = r - x*x - x - 1;
        if (y <= 0) {
            continue;
        }
        if (y % (2*x) == 0) {
            y /= 2;
            y /= x;
        } else {
            continue;
        }
        cout << x << " " << y;
        return 0;
    }
    cout << "NO";
    return 0;
}