# 1
def poz(l):
    return [x for x in l if x != int(x) or x <= 0] == []


print(poz([2, 4, 8]))
print(poz([2, 4, 8.3]))
print(poz([2, 4, -2]))


# 2
def s_list(l):
    return [x for x in l if x[0] == x[len(x) - 1]] != []


print(s_list(["abc", "aba"]))
print(s_list(["abc", "ab"]))


# 3
def zero(m):
    return not any([any(l) for l in m])


print(zero([[0, 0], [0, 0]]))
print(zero([[0, 0], [1, 0]]))


# 4
def search(sir, l):
    return [x for x in l if x in sir] != []


print(search("abcdefgh", ["ab", "nm", "o"]))
