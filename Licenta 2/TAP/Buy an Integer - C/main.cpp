#include <iostream>
using namespace std;

int d(long long n) {
    int sol = 1;
    while (n /= 10) {
        sol ++;
    }
    return sol;
}

int binary_search(long long a, long long b, long long x) {
    long long left = 1, right = 1000000000;
    while (left <= right) {
        long long mid = left + (right - left) / 2;
        if (a * mid + b * d(mid) > x) {
            right = mid - 1;
        } else {
            left = mid + 1;
        }
    }
    return left - 1;
}

int main() {
    long long a, b, x;
    cin >> a >> b >> x;
    cout << binary_search(a, b, x);
    return 0;
}
