#include <iostream>
#include <algorithm>
using namespace std;

int main() {
   int n, m, p = 0;
   cin >> n >> m;
   int v[n + 1], o[m + 1];
   for (int i = 0; i < n; i ++) cin >> v[i];
   sort(v, v + n);
   v[n] = 1000000000;
   for (int i = 0; i < m; i ++) {
       int x1, x2, y;
       cin >> x1 >> x2 >> y;
       if (x1 == 1) {
           o[p] = x2;
           p ++;
       }
   }
   m = p;
   sort(o, o + m);

   int j = 0, sol = n + m;
   if (v[0] > o[m - 1]) sol = 0;
   else {
       for (int i = 0; i <= n; i++) {
           while (j < m && o[j] < v[i]) j ++;
           sol = min(sol, i + m - j);
       }
   }
   cout << sol;
   return 0;
}
