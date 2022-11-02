#include <fstream>
using namespace std;
ifstream in("fractal.in");
ofstream out("fractal.out");

int div_et_imp(int dim, int x, int y) {
    if (dim == 1)   return 0;
    dim /= 2;
    if (x <= dim) {
        if (y <= dim)  return div_et_imp(dim, y, x);
        else    return div_et_imp(dim, 2 * dim - y + 1, dim - x + 1) + dim * dim * 3;
    } else {
        if (y <= dim)  return div_et_imp(dim, x - dim, y) + dim * dim;
        else    return div_et_imp(dim, x - dim, y - dim) + dim * dim * 2;
    }
}

int main() {
    int k, x, y;
    in >> k >> y >> x;
    int p = 1;
    for (int i = 0; i < k; i ++) {
        p *= 2;
    }
    out << div_et_imp(p, x, y);
    return 0;
}
