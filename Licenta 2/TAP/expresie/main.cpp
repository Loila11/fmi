#include <fstream>
using namespace std;

ifstream in("expresie.in");
ofstream out("expresie.out");
int main() {
    int n;
    in >> n;
    long long v[n + 1], sum = 0;
    for (int i = 0 ; i < n; i ++) {
        in >> v[i];
        sum += v[i];
    }

    long long best = 0;
    sum -= v[0];
    for (int i = 1; i < n - 1; i ++) {
        sum -= v[i] + v[i + 1];
        sum += v[i - 1] * v[i] * v[i + 1];

        if (sum > best) {
            best = sum;
        }

        sum += v[i + 1];
        sum -= v[i - 1] * v[i] * v[i + 1] - v[i] * v[i - 1];

        for (int j = i + 2; j < n; j ++) {
            sum -= v[j - 1] + v[j];
            sum += v[j] * v[j - 1];

            if (sum > best) {
                best = sum;
            }

            sum -= v[j] * v[j - 1];
            sum += v[j - 1] + v[j];
        }
        sum -= v[i] * v[i - 1];
        sum += v[i-1];
    }

    out << best;

    return 0;
}