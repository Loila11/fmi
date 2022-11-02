#include <iostream>
using namespace std;
int f[26];
int main() {
    string s;
    cin >> s;
    int pp = 0;
    for (int i = 0; i < s.size(); i ++) {
        f[s[i] - 'a'] ++;
        if (f[s[i] - 'a'] % 2 == 1) {
            pp ++;
        } else {
            pp --;
        }
    }
    int j = 0;
    char c = ' ';
    for (int i = 0; i < 26; i ++) {
        if (f[i] % 2 == 1) {
            if (pp == 1) {
                c = i + 'a';
                pp --;
            } else if (pp) {
                s[j] = (i + 'a');
                j ++;
                pp -= 2;
            }
            f[i] --;
        }
        while (f[i]) {
            s[j] = (i + 'a');
            j ++;
            f[i] -= 2;
        }
    }
    for (int i = 0; i < j; i ++) {
        cout << s[i];
    }
    if (c != ' ') {
        cout << c;
    }
    for (int i = j - 1; i >= 0; i --) {
        cout << s[i];
    }
    return 0;
}
