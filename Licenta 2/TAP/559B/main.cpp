#include <iostream>
#include <string>
using namespace std;

void div(string &a) {
    if (a.size() % 2 != 0) return ;
    int n = a.size() / 2;
    string a1 = a.substr(0, n);
    string a2 = a.substr(n, n);

    div(a1);
    div(a2);

    if (a1 > a2) a = a2 + a1;
    else  a = a1 + a2;
}

int main() {
    string a, b;
    cin >> a >> b;
    div(a);
    div(b);
    if (a == b) cout << "YES";
    else cout << "NO";
    return 0;
}
