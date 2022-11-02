import string

# 1
print([x for x in range(1, 10, 2)])


# 2
print([x for x in string.ascii_lowercase])


# 3
def generate_list(n):
    return [(-1)**(i + 1) * i for i in range(1, n)]


print(generate_list(10))


# 4
def odd(l):
    return [x for x in l if x % 2 == 1]


print(odd([3, 4, 2, 5, 6]))


# 5
def odd_p(l):
    return [l[i] for i in range(1, len(l), 2)]


print(odd_p([3, 4, 2, 5, 6]))


# 6
def same_par(l):
    return [l[i] for i in range(len(l)) if i % 2 == l[i] % 2]


print(same_par([2, 4, 1, 7, 5, 1, 8, 10]))


# 7
def tup(l):
    return [(l[i], l[i + 1]) for i in range(len(l) - 1)]


print(tup([1, 2, 3]))


# 8
def n_lists(n):
    return [[i * j for i in range(n)] for j in range(n)]


print(n_lists(5))


# 9
sir = "abcde"
print([sir[i:] + sir[:i] for i in range(len(sir))])


# 10
def lists(n):
    return [[j for i in range(j)] for j in range(n)]


print(lists(4))
