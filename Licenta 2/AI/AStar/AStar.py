class Node:
    def __init__(self, info, h):
        self.info = info         # cheia nodului
        self.h = int(h)          # estimarea pentru nod
        self.suc = {}            # lista de succesori

        '''
        configuratie pentru info: un caracter/ un sir de caractere
        '''

    def __repr__(self):
        return str(self.info)

    def __eq__(self, other):
        return self.info == other

    def __ne__(self, other):
        return not self.__eq__(other)

    def __hash__(self):
        return id(self)

    def append(self, node, cost):
        self.suc[node] = int(cost)


class TreeNode:
    def __init__(self, node, parent, g, f, seen=False):
        self.node = node        # variabila de tip Node
        self.parent = parent    # variabila de tip Node, parintele nodului curent
        self.g = g              # costul de la radacina pana la nodul curent
        self.f = f              # costul estimat de la radacina pana la final, trecand prin nodul curent
        self.seen = seen        # daca nodul a fost deja vizitat

    def path(self, tree):
        path = []
        if self.parent is not None:
            path = tree[self.parent].path(tree)
        path.append(self.node)
        return path

    def expand(self):
        suc = []
        for node in self.node.suc.keys():
            suc.append(node)
        return suc

    def test_fin(self, fin_node):
        return self.node == fin_node


def find_node(key, graph):
    for node in graph:
        if node == key:
            return node


def tree_sort(elem, tree):
    return tree[elem].f


def read_node(path):
    file = open(path, "r")
    info = file.readline()
    file.close()
    return Node(info, 0)


def read_nodes(graph):
    file = open("noduri.txt", "r")
    for line in file:
        line = line.split()
        graph.append(Node(line[0], line[1]))
    file.close()


def read_edges(graph):
    file = open("muchii.txt", "r")
    for line in file:
        line = line.split()
        node1 = find_node(line[0], graph)
        node2 = find_node(line[1], graph)
        node1.append(node2, line[2])
    file.close()


def search():
    start_node = read_node("stare_initiala.txt")
    fin_node = read_node("stare_finala.txt")
    graph = [start_node, fin_node]
    read_nodes(graph)
    read_edges(graph)
    tree = {start_node: TreeNode(start_node, None, 0, 0)}
    open_nodes = [start_node]

    while open_nodes:
        open_nodes.sort(key=lambda x: tree_sort(x, tree))
        current_node = open_nodes.pop(0)
        tree[current_node].seen = True

        if current_node == fin_node:
            return tree[current_node].path(tree)

        suc = tree[current_node].expand()
        for node in suc:
            current_g = tree[current_node].g + current_node.suc[node]
            current_f = current_g + node.h
            if node not in tree:
                open_nodes.append(node)
                tree[node] = TreeNode(node, current_node, current_g, current_f)
            else:
                if current_f < tree[node].f:
                    tree[node].f = current_f
                    tree[node].parent = current_node
                    if tree[node].seen:
                        open_nodes.append(node)


def main():
    path = search()
    if path:
        print("Drumul de cost minim:", end=' ')
        for node in path:
            print(node, end=' ')
    else:
        print("Nu exista drum intre cele doua noduri")


if __name__ == "__main__":
    main()
