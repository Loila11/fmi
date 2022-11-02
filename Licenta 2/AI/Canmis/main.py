# Canibali si misionari

import time


class Node:
    n = 0
    m = 0

    def __init__(self, info):
        self.info = info  # cheia nodului
        self.h = self.estimate_cost()  # estimarea pentru nod
        self.suc = []  # lista de succesori

        '''
        Configuratie pentru info: un dictionar cu pozitiile posibile unde cheia este un string reprezentand locul, iar 
            valoarea este un tuplu de forma: (nr de misionari, nr de canibali). Exceptie barca, pentru care pastrez 
            indice malului pe care se afla in momentul respectiv
        Schematic: info = {
                            'mal1': (mis1, can1), 
                            'mal2': (mis3, can3)
                            'barca': indice_mal
                        }
        '''

    def __repr__(self):
        node = ""
        for place in ('mal1', 'mal2'):
            node += f"{place}: (misionari: {self.info[place][0]}, canibali: {self.info[place][1]})\n"
        node += f"Barca se afla pe malul {self.info['barca']}\n"
        return node

    def __eq__(self, other):
        return self.info == other.info

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def append(self, node):
        if node not in self.suc:
            self.suc.append(node)

    def estimate_cost(self):
        return max(0, 2 * (Node.n - self.info['mal2'][0] + Node.n - self.info['mal2'][1]) / Node.m - 1)


class TreeNode:
    def __init__(self, node, parent, g, f, seen=False):
        self.node = node  # variabila de tip Node
        self.parent = parent  # variabila de tip Node, parintele nodului curent
        self.g = g  # costul de la radacina pana la nodul curent
        self.f = f  # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.seen = seen  # daca nodul a fost deja vizitat

    def expand(self):
        place = 'mal' + str(self.node.info['barca'])
        for i in range(self.node.info[place][0] + 1):
            for j in range(self.node.info[place][1] + 1):
                new_node = move_canmis(self.node.info, place, i, j)
                if new_node:
                    self.node.append(new_node)
        return self.node.suc

    def test_fin(self):
        return self.node.info['mal1'] == (0, 0)

    def path(self, tree):
        path = []
        if self.parent is not None:
            path = tree[frozenset(self.parent.info.items())].path(tree)
        path.append(self.node)
        return path


def move_canmis(info, place, i, j):
    new_place = 'mal' + str(1 + info['barca'] % 2)
    place_mis_nr = info[place][0] - i
    place_can_nr = info[place][1] - j
    new_place_mis_nr = info[new_place][0] + i
    new_place_can_nr = info[new_place][1] + j
    if test_place(place_mis_nr, place_can_nr) and test_place(new_place_mis_nr, new_place_can_nr) \
            and test_place(i, j) and 0 < i + j <= Node.m:
        return Node({place: (place_mis_nr, place_can_nr),
                     new_place: (new_place_mis_nr, new_place_can_nr),
                     'barca': (1 + info['barca'] % 2)})


def test_place(mis_nr, can_nr):
    return mis_nr >= can_nr or mis_nr == 0


def tree_sort(elem, tree):
    return tree[elem].f


def search():
    start_node = Node({'mal1': (Node.n, Node.n), 'barca': 1, 'mal2': (0, 0)})
    tree = {frozenset(start_node.info.items()): TreeNode(start_node, None, 0, 0)}
    open_nodes = [start_node]

    while open_nodes:
        open_nodes.sort(key=lambda x: tree_sort(frozenset(x.info.items()), tree))
        current_node = open_nodes.pop(0)
        current_info = frozenset(current_node.info.items())
        tree[current_info].seen = True

        if tree[current_info].test_fin():
            return tree[current_info].path(tree)

        suc = tree[current_info].expand()
        for node in suc:
            current_g = tree[current_info].g + 1
            current_f = current_g + node.h
            node_info = frozenset(node.info.items())
            if node_info not in tree:
                open_nodes.append(node)
                tree[node_info] = TreeNode(node, current_node, current_g, current_f)
            else:
                if current_f < tree[node_info].f:
                    tree[node_info].f = current_f
                    tree[node_info].parent = current_node
                    if tree[node_info].seen:
                        open_nodes.append(node)


def main():
    Node.n = int(input("Numarul de canibali/misionari = "))
    Node.m = int(input("Numarul de locuri in barca = "))
    start_time = time.perf_counter()
    path = search()
    end_time = time.perf_counter()
    print(f"Timpul de rulare: {end_time - start_time} secunde.")

    file = open("output.txt", "w")
    if path:
        file.write("Drumul de cost minim: \n")
        for node in path:
            file.write(f"{node}\n")
        file.write(f"S-au realizat {len(path) - 1} operatii.\n")
    else:
        file.write("Nu exista solutie\n")
    file.close()


if __name__ == "__main__":
    main()
