# Problema unui lacat

import copy
import sys
import time


class Node:
    length = 0
    var = 0

    def __init__(self, info):
        self.info = info  # cheia nodului
        self.h = self.estimate_cost()  # estimarea pentru nod
        self.suc = {}  # lista de succesori

        '''
        Configuratie pentru info: o lista de tupluri de forma: (stare_incuietoare, numar), unde i inseamna inchis, 
            d deschis
        Schematic: info = [
                            (i, 1), 
                            (d, 0), 
                            (i, 3)
                            ]
        Configuratie pentru suc: un dictionar in care cheia este un nod succesor iar valoarea este o lista de caractere 
            reprezentand cheia cu care se ajunge la acesta
        '''

    def __repr__(self):
        node = "["
        for index in range(Node.length - 1):
            node += f"inc({self.info[index][0]}, {self.info[index][1]}), "
        node += f"inc({self.info[Node.length - 1][0]}, {self.info[Node.length - 1][1]})]"
        return node

    def __eq__(self, other):
        return self.info == other.info

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def append(self, node, key):
        # adaug o stare succesoare la lista de stari
        # node = starea succesoare
        # key = cheia folosita pentru a ajunge la acea stare
        self.suc[node] = key

    def estimate_cost(self):
        # functia de estimare a costului
        return self.estimate_cost_1() if Node.var == 1 \
            else self.estimate_cost_2() if Node.var == 2 \
            else self.estimate_cost_3()

    def estimate_cost_1(self):
        # prima euristica admisibila posibila
        diff = 0
        for element in self.info:
            diff = max(diff, element[1])
        return diff

    def estimate_cost_2(self):
        # a doua euristica admisibila posibila
        for element in self.info:
            if element[0] == 'i':
                return element[1]
        return 0

    def estimate_cost_3(self):
        # euristica neadmisibila
        diff = 0
        for element in self.info:
            diff += element[1]
        return diff


class TreeNode:
    def __init__(self, node, parent, g, f, seen=False):
        self.node = node  # variabila de tip Node
        self.parent = parent  # variabila de tip Node, parintele nodului curent
        self.g = g  # costul de la radacina pana la nodul curent
        self.f = f  # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.seen = seen  # daca nodul a fost deja vizitat

    def expand(self, keys):
        # functia de generare a succesorilor starii curente
        # keys = lista de chei disponibile
        if self.node.estimate_cost_3() >= 2 * Node.length:
            return []

        for key in keys:
            new_node = use_key(copy.deepcopy(self.node.info), key)
            if self.node.h >= new_node.h:
                self.node.append(new_node, key)
        return self.node.suc.keys()

    def test_fin(self):
        # functia de testare a scopului; verific daca toate incuietorile sunt deschise
        for element in self.node.info:
            if element[0] != 'd':
                return False
        return True

    def path(self, tree):
        # returnez drumul de la starea initiala la starea finala
        # tree = arborele de stari
        path = []
        if self.parent is not None:
            path = tree[tuple(self.parent.info)].path(tree)
        path.append(self.node)
        return path


def use_key(info, key):
    # returnez starea lacatului dupa utilizarea cheii
    # info = informatiile starii curente
    # key = cheia utilizata
    for index in range(Node.length):
        if key[index] == 'i':
            if info[index][0] == 'i':
                info[index] = (info[index][0], info[index][1] + 1)
            else:
                info[index] = ('i', 1)
        elif key[index] == 'd':
            if info[index][0] == 'i':
                info[index] = (info[index][0], info[index][1] - 1)
                if info[index][1] == 0:
                    info[index] = ('d', info[index][1])
    return Node(info)


def tree_sort(elem, tree):
    # functia de sortare a arborelui in functie de f
    # elem = elementul curent
    # tree = arborele de stari
    return tree[elem].f


def generate_first_node():
    # generez starea de start
    info = []
    for i in range(Node.length):
        info.append(('i', 1))
    node = Node(info)
    return node


def read_keys(file_path):
    # citesc lista de chei
    # file_path = adresa fisierului de intrare, daca a fost data ca argument in linia de comanda, None altfel
    if file_path is None:
        file_path = input("Fisierul de intrare (cu codurile cheilor): ")
    file = open(file_path, "r")
    keys = []
    for line in file:
        line = line.split()[0]
        key = []
        pp = False
        for index in range(len(line)):
            key.append(line[index])
            if line[index] == 'd':
                pp = True
        if pp:
            keys.append(key)
    file.close()
    return keys


def search(keys):
    # caut cel mai scurt drum de la starea initiala la cea finala
    # keys = lista de chei disponibile
    start_node = generate_first_node()
    tree = {tuple(start_node.info): TreeNode(start_node, None, 0, 0)}
    open_nodes = [start_node]

    while open_nodes:
        open_nodes.sort(key=lambda x: tree_sort(tuple(x.info), tree))
        current_node = open_nodes.pop(0)
        current_info = tuple(current_node.info)
        tree[current_info].seen = True

        if tree[current_info].test_fin():
            return tree[current_info].path(tree)

        suc = tree[current_info].expand(keys)
        for node in suc:
            current_g = tree[current_info].g + 1
            current_f = current_g + node.h
            node_info = tuple(node.info)
            if node_info not in tree:
                open_nodes.append(node)
                tree[node_info] = TreeNode(node, current_node, current_g, current_f)
            else:
                if current_f < tree[node_info].f:
                    tree[node_info].f = current_f
                    tree[node_info].parent = current_node
                    if tree[node_info].seen:
                        open_nodes.append(node)


def write_sol(keys, file_path):
    # scriu solutia in fisierul de output
    # keys = lista de chei disponibile
    # file_path = adresa fisierului de output
    start_time = time.perf_counter()
    path = search(keys)
    end_time = time.perf_counter()
    print(f"Timpul de rulare pentru varianta {Node.var}: {end_time - start_time} secunde.")

    file = open(file_path, "w")
    if path:
        file.write("Initial: " + str(path[0]) + "\n")

        for index in range(len(path) - 1):
            file.write(f"{index + 1}) Incuietori: {path[index]}.\n"
                       f"Folosim cheia: {path[index].suc[path[index + 1]]} pentru a ajunge la {path[index + 1]}.\n")

        file.write(f"\nIncuietori(stare scop): {path[len(path) - 1]}.\n"
                   f"S-au realizat {len(path) - 1} operatii.\n")
    else:
        file.write("Problema nu are solutie.\n")
    file.close()


def main():
    # apelez programul folosind, pe rand, cele 3 euristici gasite
    try:
        arg = sys.argv[1]
    except IndexError:
        arg = None
    keys = read_keys(arg)
    Node.length = len(keys[0])

    Node.var = 1
    write_sol(keys, "output1.txt")

    Node.var = 2
    write_sol(keys, "output2.txt")

    Node.var = 3
    write_sol(keys, "output3.txt")


if __name__ == "__main__":
    main()

'''
Precizari:

Algoritmul de generare a succesorilor:
    - TreeNode.expand(keys)
    - Pentru o stare a lacatului parcurg lista de chei disponibile si generez starea succesoare folosind cheia curenta. 
    In cazul in care starea este valida (costul estimat este mai mic sau egal cu cel actual) o adaug in lista de 
    succesori.
    - Generarea starii succesoare se face cu ajutorul functiei use_key(info, key), care parcurge incuietorile si zonele 
    cheii si incuie sau descuie o incuietoare atunci cand este cazul.

Euristici pentru estimarea costului:
    - Node.var = 1: Valoarea maxima a unei incuietori din lacat:
        - Admisibila, consistenta
        - Pentru o stare data, compar de cate ori este incuiata fiecare incuietoare pentru a gasi maximul.
        - Intrucat o cheie poate descuia un lacat o singura data, pentru o incuietoare incuiata de i ori vor fi necesare 
        i chei. Pentru un lacat cu mai multe incuietori vor fi necesare minim i_max chei, unde i_max este numarul maxim 
        de chei necesare pentru o incuietoare din serie. Atata timp cat nu avem o cheie care descuie toate incuietorile 
        in acelasi timp, dupa ce am terminat cu i_max va trebui reluat procesul pentru noua stare. Ergo, euristica are 
        mereu valoarea mai mica decat costul real al drumului.
    - Node.var = 2: Valoarea primei incuietori inchise (Echivalent cu a unei incuietori oarecare):
        - Admisibila, neconsistenta
        - Pentru o stare data, caut prima incuietoare inchisa si returnez costul acesteia.
        - Dupa cum am precizat si mai sus, pentru a descuia o incuietoare inchisa de i ori avem nevoie de i chei. 
        Intrucat cheia aleasa este una oarecare, aceasta poate sa aiba costul maxim, caz in care ajungem in situatia 
        explicata anterior, sau un cost mai mic decat cel maxim. Pentru al doilea caz, avand in vedere prima afirmatie 
        din acest paragraf stim cu siguranta ca vor fi necesare mai multe chei decat valoarea estimata doar pentru a 
        descuia incuietoarea cu costul maxim.
    - Node.var = 3: Adun pentru fiecare incuietoare de cate ori este incuiata:
        - Nu indeplineste conditia de admisibilitate deoarece costul estimat va fi mereu mai mare decat cel real.

Fisiere de intrare:
    - Un fisier de input care nu are solutii: chei0.txt
    - Un fisier de input care da o stare initiala care este si finala: - 
        Nu este posibil deoarece starea initiala este precizata din datele problemei. 
        Fisierul de intrare contine doar colectia de chei disponibile.
    - Un fisier de input cu un drum de cost minim de lungime 3-5: chei1.txt
    - Un fisier de input cu un drum de cost minim de lungime mai mare decat 5: chei2.txt

Fisiere de iesire:
    - Pentru prima euristica: output1.txt
    - Pentru a doua euristica: output2.txt
    - Pentru a treia euristica: output3.txt

Optimizari:
    - Node.__repr__(): reprezentarea nodului este eficienta pentru formatul de output cerut
    - TreeNode.expand(keys): functia self.node.estimate_cost_3() calculeaza de cate ori au fost incuiate toate 
        incuietorile din lacat. Daca acest numar depaseste dublul valorii initiale (Node.length) este evident ca starea 
        nu va face parte din solutie. Se poate demonstra ca au fost utilizate minim 2 stari care se anuleaza, deci nu 
        este cel mai scurt drum (asta, desigur, in cazul in care are solutie)
    - read_keys(): adaug o cheie in lista doar daca deschide cel putin o incuietoare
'''
