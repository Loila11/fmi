#include <fstream>
using namespace std;
ifstream in("submultimi.in");
ofstream out("submultimi.out");
int main() {
    int n;
    in >> n;
    int p = 1 << n;
    for (int i = 1; i < p; i ++) {
        for (int j = 0; j < n; j ++) {
            if(i & (1 << j)) {
                out << j + 1 << " ";
            }
        }
        out << '\n';
    }
    return 0;
}
