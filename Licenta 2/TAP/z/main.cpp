#include <fstream>
using namespace std;
ifstream in("z.in");
ofstream out("z.out");

int div_imp(int x_start, int y_start, int dim, int nr, int x, int y) {
    if (dim == 1)   return nr;
    dim /= 2;
    if (x - x_start < dim) {
        if (y - y_start < dim)  return div_imp(x_start, y_start, dim, nr, x, y);
        else    return div_imp(x_start, y_start + dim, dim, nr + dim * dim, x, y);
    } else {
        if (y - y_start < dim)  return div_imp(x_start + dim, y_start, dim, nr + dim * dim * 2, x, y);
        else   return div_imp(x_start + dim, y_start + dim, dim, nr + dim * dim * 3, x, y);
    }
}

int main() {
    int n, k;
    in >> n >> k;
    int p = 1;
    for (int i = 0; i < n; i ++) {
        p *= 2;
    }
    while (k --) {
        int x, y;
        in >> x >> y;
        out << div_imp(1, 1, p, 1, x, y) << '\n';
    }
    return 0;
}