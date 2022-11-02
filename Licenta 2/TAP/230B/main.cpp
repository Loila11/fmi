#include <iostream>
using namespace std;

bool prim(long long x) {
    if ((x % 2 == 0 && x != 2) || x == 1) return false;
    for (int i = 3; i * i <= x; i += 2) {
        if (x % i == 0) return false;
    }
    return true;
}

bool sqrt(long long x) {
    long long st = 1, dr = x;
    while(st <= dr) {
        long long mij = (st + dr) / 2;
        if (x % mij == 0 && x / mij == mij) return prim(mij);
        else if (mij > x / mij)  dr = mij - 1;
        else    st = mij + 1;
    }
    return false;
}

int main() {
    int n;
    cin >> n;
    while (n --) {
        long long x;
        cin >> x;
        if (sqrt(x))   cout << "YES\n";
        else cout << "NO\n";
    }
    return 0;
}
