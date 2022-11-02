#include <iostream>
using namespace std;
int main() {
    int n;
    cin >> n;
    int arr[n + 1];
    fflush(stdout);

    int s12, s23, s13, sum;
    cout << "? 1 2\n" << flush;
    cin >> s12;
    cout << "? 2 3\n" << flush;
    cin >> s23;
    cout << "? 1 3\n" << flush;
    cin >> s13;
    sum = s12 + s23 + s13;
    sum /= 2;
    arr[1] = sum - s23;
    arr[2] = sum - s13;
    arr[3] = sum - s12;

    for (int i = 4; i <= n; i ++) {
        cout << "? " << i - 1 << " " << i << '\n' << flush;
        cin >> sum;
        arr[i] = sum - arr[i - 1];
    }

    cout << "!";
    for (int i = 1; i <= n; i ++) {
        cout << ' ' << arr[i];
    }
    return 0;
}