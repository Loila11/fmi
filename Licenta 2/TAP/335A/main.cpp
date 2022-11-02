#include <iostream>
#include <cstring>
using namespace std;
int v[27];
int main() {
    char s[1003];
    int n;
    cin >> s >> n;

    for (int i = 0; i < strlen(s); i ++) {
        v[s[i] - 'a'] ++;
    }

    for (int k = 1; k <= 1000; k ++) {
        int sum = 0;
        for (int i = 0; i < 26; i ++) {
            bool pp = v[i] % k > 0;
            sum += v[i] / k + pp;
        }
        if (sum <= n) {
            cout << k << '\n';
            for (int i = 0; i < 26; i ++) {
                bool pp = v[i] % k > 0;
                int x = v[i] / k + pp;
                for (int j = 0; j < x; j ++) {
                    n --;
                    cout << char('a' + i);
                }
            }

            while (n) {
                cout << 'a';
                n --;
            }
            return 0;
        }
    }
    cout << "-1";
    return 0;
}