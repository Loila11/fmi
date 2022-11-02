# 8 puzzle

import copy
import time


class Node:
    size = 3
    empty = '0'
    last_info = []

    def __init__(self, info):
        self.info = info  # cheia nodului
        self.h = self.estimate_cost()  # estimarea pentru nod
        self.suc = []  # lista de succesori
        self.index = self.find_empty_index()  # pozitia spatiului liber

        '''
        Configuratie pentru info: o matrice cu cheile tablitelor. Marchez spatiul liber cu simbolul din Node.empty
        Schematic: info = [
                            [11], [12], [13],
                            [21], [22], [23],
                            [31], [32], [33]
                          ]
        '''

    def __repr__(self):
        node = ""
        for line in self.info:
            for element in line:
                node += f"{element} "
            node += "\n"
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
        for i in range(Node.size):
            for j in range(Node.size):
                diff += self.info[i][j] != self.last_info[i][j]
        return diff

    def find_empty_index(self):
        for i in range(Node.size):
            for j in range(Node.size):
                if self.info[i][j] == Node.empty:
                    return i, j
        return None, None

    def count_inversions(self):
        inv = 0
        for i in range(Node.size ** 2):
            for j in range(i + 1, Node.size ** 2):
                if self.info[int(i / 3)][i % 3] > self.info[int(j / 3)][j % 3]:
                    inv += 1
        return inv


class TreeNode:
    def __init__(self, node, parent, g, f, seen=False):
        self.node = node  # variabila de tip Node
        self.parent = parent  # variabila de tip Node, parintele nodului curent
        self.g = g  # costul de la radacina pana la nodul curent
        self.f = f  # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.seen = seen  # daca nodul a fost deja vizitat

    def expand(self):
        directions = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        for direction in directions:
            new_node = slide_slate(self.node, direction)
            if new_node:
                self.node.append(new_node)
        return self.node.suc

    def test_fin(self):
        return self.node.info == Node.last_info

    def path(self, tree):
        path = []
        if self.parent is not None:
            path = tree[tuple(tuple(element) for element in self.parent.info)].path(tree)
        path.append(self.node)
        return path


def slide_slate(node, direction):
    new_line = node.index[0] + direction[0]
    new_column = node.index[1] + direction[1]

    if 0 <= new_line < Node.size and 0 <= new_column < Node.size:
        new_info = copy.deepcopy(node.info)
        new_info[node.index[0]][node.index[1]] = new_info[new_line][new_column]
        new_info[new_line][new_column] = node.empty
        return Node(new_info)


def tree_sort(elem, tree):
    return tree[elem].f


def read_node(path):
    file = open(path, "r")
    node = []
    for line in file:
        info = []
        line = line.split()
        for element in line:
            info.append(element)
        node.append(info)
    file.close()
    return node


def search():
    start_node = Node(read_node("stare_initiala.txt"))
    tree = {tuple(tuple(element) for element in start_node.info): TreeNode(start_node, None, 0, 0)}
    open_nodes = [start_node]

    if start_node.count_inversions() % 2 == 1:
        return None

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
