# Problema 1

import copy
import math
import time


class Nod:
    varianta = 1
    numar_stive = 0
    inaltimi = []

    def __init__(self, info):
        """ Validari si optimizari: Mod de reprezentare eficient.

        Blocurile sunt pastrate intr-o lista de liste, iar succesorii intr-un dictionar impreuna cu costul aferent.
        """
        self.info = info                # informatia pastrata in nod: lista stivelor in momentul actual
        self.h = self.estimare_cost()   # estimarea costului pentru nod
        self.suc = {}                   # lista de succesori cu costul aferent

    def __str__(self):
        nod = "\n"
        for stiva in self.info:
            for element in stiva:
                nod += f"{element} "
            nod += "\n"
        return nod

    def __eq__(self, nod):
        return self.info == nod.info

    def __hash__(self):
        return id(self)

    def adauga(self, nod, cost):
        """ Adauga un nod in lista succesorilor.

        :param nod: nodul de adaugat in lista succesorilor
        :param cost: costul acestei mutari
        """
        if nod not in self.suc:
            self.suc[nod] = cost

    def euristica_1(self):
        """ Calculeaza diferenta intre inaltimile actuale ale stivelor si inaltimile finale impartita la 2.

        Este admisibila, intrucat in cel mai bun caz am cateva stive cu un bloc in plus fata de inaltimea ceruta si
        acelasi numar de stive cu un bloc in minus. Asadar, dintr-o mutare aduc 2 stive la inaltimea ceruta.

        Este consistenta deoarece presupune costul mutarii unui bloc 1, numar mai mic sau egal decat costul real,
        iar euristica nodului urmator este mai mare sau egala cu euristica curenta - 1 (prin mutarea unui bloc ajung 2
        stive la inaltimea ceruta). Asadar, suma celor 2 costuri va fi mai mare sau egala cu costul euristicii actuale.
        """
        return sum([abs(len(self.info[i]) - Nod.inaltimi[i]) for i in range(len(self.info))]) / 2

    def euristica_2(self):
        """ Calculeaza diferenta maxima intre o inaltime actuala a unei stive si inaltimea sa finala.

        Este admisibila deoarece euristica de la fiecare pas returneaza o estimare a costului mai mica decat costul real
        pana la starea finala. Costul real pentru a trece dintr-o stare intr-o stare succesoare este egal cu costul
        mutarii unui bloc. Costul real pentru a ajunge in starea finala este egal cu suma acestor costuri pentru toti
        pasii necesari. In cadrul acestei euristici, consider costul mutarii unui bloc = 1. Stim ca acest cost este mai
        mic sau egal cu costul real deoarece costul mutarii unui bloc este egal cu numarul de divizori ai acelui bloc,
        iar un bloc are minim un divizor. De asemenea, in cadrul acestei euristici consider ca numarul de blocuri care
        trebuie mutate pentru a ajunge in starea finala este egal cu diferenta maxima de nivel la un anumit moment. In
        realitate, nu doar ca ar trebui luate in calcul toate aceste diferente de nivel, ci si faptul ca in cadrul unei
        mutari s-ar putea ca pozitia optima pentru a pune un bloc sa nu fie pozitia pe care va ramane pana la final
        (deci am cel putin 2 mutari pentru acelasi bloc). Asadar, si numarul de mutari din euristica este mai mic decat
        cel din realitate. Am stabilit ca costul final este egal cu suma costurilor tuturor mutarilor necesare, iar cum
        in euristica atat costul unei mutari este mai mic sau egal decat costul real cat si numarul mutarilor este mai
        mic sau egal, este evident ca si costul final va fi mai mic sau egal.

        O euristica este consistenta in cazul in care costul dintr-o stare n1 este mai mic sau egal cu suma dintre
        costul dintr-o stare n2 imediat succesoare si costul mutarii care ma duce in acea stare. In cazul actual,
        euristica urmatoare unei mutari poate fi egala cu euristica anterioara (mut un bloc care nu are legatura cu
        stiva de diferenta maxima sau aduc o alta stiva la diferenta maxima), cu euristica anterioara - 1 (aduc stiva
        de diferenta maxima cu un bloc mai aproape de inaltimea dorita, iar restul inaltimilor sunt mai mici de atat)
        sau cu euristica anterioara + 1 (aduc stiva de diferenta maxima cu un bloc mai departe de inaltimea dorita)
        Asadar, euristica urmatoarei mutari va fi mai mare sau egala cu euristica actuala - 1. Costul unei mutari este
        egal cu numarul de divizori ai blocului mutat, deci este mai mare sau egal cu 1. Daca inlocuim in formula
        initiala, observam ca euristica actuala este mai mica sau egala decat suma dintre euristica urmatoare si costul
        asociat ((cost actual - 1) + 1 = cost actual). Deci, euristica este consistenta.
        """
        return max([abs(len(self.info[i]) - Nod.inaltimi[i]) for i in range(len(self.info))])

    def euristica_3(self):
        """ Returneaza suma intre suma valorilor blocurilor de pe fiecare stiva inmultita cu indicele stivei.

        Evident, nu este admisibila deoarece aceasta valoare nu are nicio legatura cu drumul care trebuie calculat.
        """
        return sum(i * sum(self.info[i]) for i in range(self.numar_stive))

    def estimare_cost(self):
        """ Functia de estimare a costului. Este aleasa euristica in functie de varianta selectata in Nod.varianta. """
        if Nod.varianta == 1:
            return self.euristica_1()
        if Nod.varianta == 2:
            return self.euristica_2()
        return self.euristica_3()


class NodArbore:
    def __init__(self, nod, parinte, g, f, vizitat=False):
        self.nod = nod          # variabila de tip Nod
        self.parinte = parinte  # variabila de tip Nod, parintele nodului curent
        self.g = g              # costul de la radacina pana la nodul curent
        self.f = f              # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.vizitat = vizitat  # daca nodul a fost deja vizitat

    def generare_succesori(self):
        """ Functia de generare a succesorilor.

        Pentru fiecare bloc aflat in capatul stivei caut toate celelalte stive pe care l-as putea muta, astfel incat
        mutarea sa fie valida. Adaug toate aceste stive in lista succesorilor.
        """
        info = copy.deepcopy(self.nod.info)
        for i in range(Nod.numar_stive):
            if len(info[i]):
                bloc = info[i].pop(len(info[i]) - 1)
                for j in range(Nod.numar_stive):
                    if i != j and mutare_valida(info, bloc, j):
                        info[j].append(bloc)
                        new_nod = Nod(copy.deepcopy(info))
                        self.nod.adauga(new_nod, divizori(bloc))
                        info[j].pop()
                info[i].append(bloc)
        return self.nod.suc

    def testare_scop(self):
        """ Functia de testare a scopului. """
        return all([len(self.nod.info[i]) == Nod.inaltimi[i] for i in range(Nod.numar_stive)])

    def drum(self, arbore):
        """ Reconstituirea drumului de cost minim.

        :param arbore: arborele drumurilor posibile
        """
        drum = []
        if self.parinte is not None:
            drum = arbore[tuple(tuple(info) for info in self.parinte.info)].drum(arbore)
        drum.append(self.nod)
        return drum


def mutare_valida(info, bloc, i):
    """ Verifica daca o mutare este valida.

    :param info: lista stivelor
    :param bloc: blocul care va fi mutat
    :param i: indicele stivei pe care blocul va fi mutat
    """
    stiva = info[i]

    if i > 0:
        stiva_stanga = info[i - 1]
        if len(stiva_stanga) > len(stiva) and stiva_stanga[len(stiva)] == bloc:
            return False

    if i < Nod.numar_stive - 1:
        stiva_dreapta = info[i + 1]
        if len(stiva_dreapta) > len(stiva) and stiva_dreapta[len(stiva)] == bloc:
            return False

    return len(stiva) == 0 or math.gcd(stiva[-1], bloc) == 1


def divizori(n):
    """ Determina numarul de divizori ai numarului natural n.

    :param n: un numar real
    """
    return len([i for i in range(1, n + 1) if n % i == 0])


def sortare_arbore(nod, arbore):
    """ Sorteaza arborele in fuctie de f.

    :param nod: nodul din arbore
    :param arbore: arborele drumurilor
    """
    return arbore[nod].f


def verifica_existenta_solutiei(info):
    """ Validari si optimizari: Gasirea unor conditii din care sa reiasa ca o stare nu are cum sa contina in subarborele
    de succesori o stare finala, deci nu mai merita expandata.

    Verific daca exista vreun bloc care se divide cu toata lumea deci nu poate fi mutat, dar in lista de inaltimi stiva
    pe care se afla blocul trebuie sa aiba o inaltime mai mica decat nivelul blocului si nu exista nicio stiva de
    inaltime 1.

    :param info: lista de stive de verificat
    """
    for i in range(len(info)):
        for j in range(len(info[i])):
            if all([math.gcd(info[i][j], info[k][h]) != 1 for k in range(len(info)) for h in range(len(info[k]))]) and \
                    Nod.inaltimi[i] < j + 1 and not any([Nod.inaltimi[k] == 1 for k in range(Nod.numar_stive)]):
                return False
    return True


def input_valid(info):
    """ Validari si optimizari: Verificarea datelor de intrare.

    Lista cu inaltimile stivelor trebuie sa aiba lungime egala cu numarul de stive, iar suma acestor inaltimi trebuie sa
    fie egala cu numarul de blocuri.

    :param info: lista de stive de verificat
    """
    return len(Nod.inaltimi) == Nod.numar_stive and \
           sum([len(info[i]) - Nod.inaltimi[i] for i in range(len(info))]) == 0


def citeste_date_intrare(nume_fisier):
    """ Citeste datele de intrare, le proceseaza si le salveaza in memorie.

    :param nume_fisier: numele fisierului din care sunt extrase datele de intrare
    """
    fisier_intrare = open(nume_fisier, "r")
    Nod.numar_stive = int(fisier_intrare.readline().split()[0])

    info = []
    for i in range(Nod.numar_stive):
        stiva = list(map(int, fisier_intrare.readline().split()))
        info.append(stiva)
    Nod.inaltimi = list(map(int, fisier_intrare.readline().split()))

    fisier_intrare.close()
    return info


def A_Star(fisier_intrare):
    """ Algoritmul A Star.

    :param fisier_intrare: numele fisierului din care sunt extrase datele de intrare
    """
    input_info = citeste_date_intrare(fisier_intrare)
    if not input_valid(input_info):
        print("Fisier de intrare incorect\n")
        return
    if not verifica_existenta_solutiei(input_info):
        return

    start_node = Nod(input_info)
    arbore = {tuple(tuple(element) for element in start_node.info): NodArbore(start_node, None, 0, 0)}
    noduri_deschise = [start_node]

    while noduri_deschise:
        noduri_deschise.sort(key=lambda x: sortare_arbore(tuple(tuple(element) for element in x.info), arbore))
        nod_curent = noduri_deschise.pop(0)
        info_nod_curent = tuple(tuple(element) for element in nod_curent.info)
        arbore[info_nod_curent].vizitat = True

        if arbore[info_nod_curent].testare_scop():
            return arbore[info_nod_curent].drum(arbore)

        suc = arbore[info_nod_curent].generare_succesori()
        for nod in suc:
            g_curent = arbore[info_nod_curent].g + nod_curent.suc[nod]
            f_curent = g_curent + nod.h
            info_nod = tuple(tuple(element) for element in nod.info)
            if info_nod not in arbore:
                noduri_deschise.append(nod)
                arbore[info_nod] = NodArbore(nod, nod_curent, g_curent, f_curent)
            else:
                if f_curent < arbore[info_nod].f:
                    arbore[info_nod].f = f_curent
                    arbore[info_nod].parinte = nod_curent
                    if arbore[info_nod].vizitat:
                        noduri_deschise.append(nod)


def main():
    """ Functia principala a programului. """
    fisiere_intrare = ["input1.txt", "input2.txt", "input3.txt", "input4.txt"]
    for fisier_intrare in fisiere_intrare:
        for varianta in [1, 2, 3]:
            Nod.varianta = varianta
            start_time = time.perf_counter()
            drum = A_Star(fisier_intrare)
            end_time = time.perf_counter()
            print(f"Timpul de rulare pentru {fisier_intrare} cu euristica {varianta}: {end_time - start_time} secunde.")

            output_file = open("output_varianta" + str(varianta) + "_" + fisier_intrare, "w")

            if not drum:
                output_file.write("Nu exista solutie\n")
            else:
                output_file.write(f"Drumul de cost minim (lungime {len(drum) - 1}): \n")
                for nod in drum:
                    output_file.write(str(nod))

            output_file.close()


if __name__ == "__main__":
    main()
