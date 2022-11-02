# Blocuri

import copy
import time


class Node:
    length = 0
    last_info = []

    def __init__(self, info):
        self.info = info  # cheia nodului
        self.h = self.estimate_cost()  # estimarea pentru nod
        self.suc = []  # lista de succesori

        '''
        Configuratie pentru info: o lista de stive, unde inceputul unei stive reprezinta cel mai de jos cub, iar 
            finalul, cel mai de sus, singurul care poate fi mutat
        Exemplu schematic: info = [
                                    [cub1], 
                                    [cub2, cub3, cub4], 
                                    [], 
                                    [cub5]
                                ]
        '''

    def __repr__(self):
        node = ""
        for stack in self.info:
            for element in stack:
                node += f"{element} "
            node += "\n"
        node += "---------------"
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
        diff = 0
        for i in range(Node.length):
            diff += abs(len(self.info[i]) - len(Node.last_info[i]))
            length = min(len(self.info[i]), len(Node.last_info[i]))
            for j in range(length):
                diff += (self.info[i][j] != Node.last_info[i][j])
        return diff


class TreeNode:
    def __init__(self, node, parent, g, f, seen=False):
        self.node = node  # variabila de tip Node
        self.parent = parent  # variabila de tip Node, parintele nodului curent
        self.g = g  # costul de la radacina pana la nodul curent
        self.f = f  # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.seen = seen  # daca nodul a fost deja vizitat

    def expand(self):
        info = copy.deepcopy(self.node.info)
        for i in range(Node.length):
            if not len(info[i]):
                continue

            block = info[i].pop(len(info[i]) - 1)
            for j in range(Node.length):
                if i == j:
                    continue

                info[j].append(block)
                new_node = Node(copy.deepcopy(info))
                self.node.append(new_node)
                info[j].remove(block)

            info[i].append(block)
        return self.node.suc

    def test_fin(self):
        return self.node.info == Node.last_info

    def path(self, tree):
        path = []
        if self.parent is not None:
            path = tree[tuple(tuple(element) for element in self.parent.info)].path(tree)
        path.append(self.node)
        return path


def tree_sort(elem, tree):
    return tree[elem].f


def read_node(path):
    file = open(path, "r")
    Node.length = int(file.readline().split()[0])
    info = []
    for i in range(Node.length):
        line = file.readline().split()
        info.append(line)
    file.close()
    return info


def search():
    start_node = Node(read_node("stare_initiala.txt"))
    tree = {tuple(tuple(element) for element in start_node.info): TreeNode(start_node, None, 0, 0)}
    open_nodes = [start_node]

    while open_nodes:
        open_nodes.sort(key=lambda x: tree_sort(tuple(tuple(element) for element in x.info), tree))
        current_node = open_nodes.pop(0)
        current_info = tuple(tuple(element) for element in current_node.info)
        tree[current_info].seen = True

        if tree[current_info].test_fin():
            return tree[current_info].path(tree)

        suc = tree[current_info].expand()
        for node in suc:
            current_g = tree[current_info].g + 1
            current_f = current_g + node.h
            node_info = tuple(tuple(element) for element in node.info)
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
    Node.last_info = read_node("stare_finala.txt")
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

'''
Fisierele de intrare/iesire sunt de forma:
    Numarul de stive disponibile
    Stiva1 de jos in sus
    Stiva2 de jos in sus
    ...
    StivaN de jos in sus
'''
