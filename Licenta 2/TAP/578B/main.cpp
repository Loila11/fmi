#include <iostream>
using namespace std;

int main() {
    int n, k, x;
    cin >> n >> k >> x;
    long long p = 1;
    while (k --) {
        p *= x;
    }
    long long prefix[n + 2];    prefix[0] = 0;
    long long sufix[n + 2];     sufix[n + 1] = 0;
    long long a[n + 2]; a[0] = 0;   a[n + 1] = 0;
    for (int i = 1; i <= n; i ++) {
        cin >> a[i];
        prefix[i] = prefix[i - 1] | a[i];
    }
    for (int i = n; i > 0; i --) {
        sufix[i] = sufix[i + 1] | a[i];
    }
    long long ans = 0;
    for (int i = 1; i <= n; i ++) {
        ans = max(ans, prefix[i - 1] | (a[i] * p) | sufix[i + 1]);
    }
    cout << ans;
    return 0;
}
