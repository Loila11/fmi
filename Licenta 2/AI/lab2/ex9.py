# 1
def gen_matrix(n):
    return [[j + 1 for i in range(n)] for j in range(n)]


print(gen_matrix(4))


# 2
def odd_col(m):
    return [[l[i] for i in range(len(l)) if i % 2 == 1] for l in m]


print(odd_col([[1, 2, 3, 4], [5, 6, 7, 8]]))


# 3
def sita(m1, m2):
    return [[m1[i][j] * m2[i][j] for j in range(len(m1[i]))] for i in range(len(m1))]


print(sita([[2, 5, 7, 1], [4, 5, 0, 2], [0, 3, 1, 7]],
           [[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 0, 1]]))


# 4
def gen_matrix(n, elem):
    return [[elem * (i + j == n - 1) for j in range(n)] for i in range(n)]


print(gen_matrix(3, 1))


# 5
def gen_matrix2(l1, l2):
    return [[l1[i] if l1[i] <= l2[j] else l2[i] for j in range(len(l2))] for i in range(len(l1))]


print(gen_matrix2([1, 2], [1, 2, 3]))
