#include <fstream>
#include <vector>
using namespace std;
ifstream in("text3.in");
ofstream out("text3.out");
#define M 20002
pair<int, int> dp[M];
vector<string> s;
vector<int> last(27, -1);
int maxim, pmax;

void print(int i) {
    if (dp[i].second == i) {
        out << s[i] << '\n';
        return ;
    }
    print(dp[i].second);
    out << s[i] << '\n';
}

int main() {
    // dp[i] = nr maxim de cuvinte pastrate cu i ultimul cuvant
    // last[i] = pozitia cuvantului cu ultima litera i si dp maxim
    string x;
    int i = 0;
    while (in >> x) {
        s.push_back(x);
        dp[i] = {1, i};
        int let = s[i][0] - 'a';
        if (last[let] != -1) {
            dp[i] = max(dp[i],
                    {dp[last[let]].first + 1, last[let]});
        }
        let = s[i][s[i].size() - 1] - 'a';
        if (last[let] == -1 || dp[last[let]] < dp[i]) {
            last[let] = i;
        }
        if (dp[i].first > maxim) {
            maxim = dp[i].first;
            pmax = i;
        }
        i ++;
    }
    out << s.size() << '\n' << s.size() - maxim << '\n';
    print(pmax);
    return 0;
}
