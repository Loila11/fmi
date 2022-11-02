#include <iostream>
#include <algorithm>
using namespace std;
#define votes first
#define pos second

bool sortare(pair<int, pair<int, int>> a, pair<int, pair<int, int>> b) {
    if (a.votes == b.votes) return a.pos.votes < b.pos.votes;
    return a.votes > b.votes;
}

bool can_win(int pos, pair<int, pair<int, int>> v[], int k, int r) {
    int votes = v[pos].votes + r;
    return (votes > v[k].votes || pos <= k) && votes > 0;
}

bool can_lose(int pos, pair<int, pair< int, int>> v[], int k, int r, int n) {
    if (k == n && v[pos].votes > 0) return false;
    if (k > 1 && v[pos].votes == 0) return true;
    for (int i = pos + 1; i <= k + 1; i ++) {
        int dif = v[pos].votes - v[i].votes + 1;
        if (dif > r)    return false;
        r -= dif;
    }
    return true;
}

int main() {
    int nr_candidates, nr_seats, nr_citizens, nr_votes;
    cin >> nr_candidates >> nr_seats >> nr_citizens >> nr_votes;
    int remaining_votes = nr_citizens - nr_votes;
    pair <int, pair<int, int>> v[nr_candidates + 1];
    for (int i = 1; i <= nr_candidates; i ++) {
        v[i].pos.pos = i;
    }
    for (int i = 1; i <= nr_votes; i ++) {
        int x;
        cin >> x;
        v[x].votes ++;
        v[x].pos.votes = i;
    }
    sort(v + 1, v + nr_candidates + 1, sortare);
    int f[nr_candidates + 1];
    for (int i = 1; i <= nr_candidates; i ++) {
        if (can_win(i, v, nr_seats, remaining_votes)) {
            if (can_lose(i, v, nr_seats, remaining_votes, nr_candidates)) {
                f[v[i].pos.pos] = 2;
            } else {
                f[v[i].pos.pos] = 1;
            }
        } else {
            f[v[i].pos.pos] = 3;
        }
    }
    for (int i = 1; i <= nr_candidates; i ++) {
        cout << f[i] << ' ';
    }
    return 0;
}
