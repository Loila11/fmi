#include <fstream>
#include <map>
#include <deque>
#include <vector>
#include <set>
#include <string.h>
#include <stdio.h>

using namespace std;

ifstream in ("date.in");
ofstream out ("date.out");

struct automat {
    int Q, E, F, q0, T;
    set <int> q, f;
    set <char> e;
    map <pair <int, char>, vector <int>> cuvinte;
};

void citire_stari(automat &a) {
    in >> a.Q;
    a.q.clear();
    for (int i = 1; i <= a.Q; i ++) {
        int stare;
        in >> stare;
        a.q.insert(stare);
    }
}

void citire_litere(automat &a) {
    in >> a.E;
    a.e.clear();
    for (int i = 1; i <= a.E; i ++) {
        char litera;
        in >> litera;
        a.e.insert(litera);
    }
}

void citire_stari_finale(automat &a) {
    in >> a.F;
    a.f.clear();
    for (int i = 1; i <= a.F; i ++) {
        int stare;
        in >> stare;
        a.f.insert(stare);
    }
}

void citire_tranzitii(automat &a) {
    in >> a.T;
    for (int i = 1; i <= a.T; i ++) {
        int stare_initiala, stare_finala;
        char litera;
        in >> stare_initiala >> litera >> stare_finala;
        a.cuvinte[{stare_initiala, litera}].push_back(stare_finala);
    }
}

void citire(automat &a) {
    citire_stari(a);
    citire_litere(a);
    in >> a.q0;
    citire_stari_finale(a);
    citire_tranzitii(a);
}

bool lnfa(automat a, int q, char s[], set <pair <int, char*>> &vizitat) {
    // verific daca am mai parcurs aceasta tranzitie fiind in aceeasi pozitie in cuvant
    if (vizitat.find({q, s}) != vizitat.end())
        return false;
    vizitat.insert({q, s});

    // parcurg toate l-tranzitiile care pornesc din starea actuala
    for (int i : a.cuvinte[{q, '.'}]) {
        if(lnfa(a, i, s, vizitat) == 1) {
            return true;
        }
    }

    // verific daca mai exista litere care nu au fost parcurse din cuvantul dat
    if (s[0] == '\0' || s[0] == ' ') {
        if (a.f.find(q) == a.f.end()) {
            return false;
        }
        return true;
    }

    // verific daca din starea actuala exista tranzitia urmatoare in automat
    if (a.cuvinte.find({q, s[0]}) == a.cuvinte.end()) {
        return false;
    }


    // parcurg toate tranzitiile s[0] care pornesc din starea actuala
    for (int i : a.cuvinte[{q, s[0]}]) {
        if(lnfa(a, i, s + 1, vizitat) == 1) {
            return true;
        }
    }

    return false;
}

void rezolvare(automat a) {
    int t;
    in >> t;

    char c;
    in.get(c);

    while (t --) {
        char s[1000];
        in.getline(s, 1000);

        set <pair <int, char*>> vizitat;
        vizitat.clear();

        if (lnfa(a, a.q0, s, vizitat)) {
            out << "DA\n";
        } else {
            out << "NU\n";
        }
    }
}

int main() {
    automat a;
    citire(a);
    rezolvare(a);
    return 0;
}
