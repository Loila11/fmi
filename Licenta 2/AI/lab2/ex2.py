import string
import itertools


# a
def eq_list(l):
    return len(set(l)) == 1


print(eq_list([3, 2, 2, 1]))
print(eq_list([10, 10]))


# b
def alphabet(sir):
    return set(sir.lower()) >= set(string.ascii_lowercase)


print(alphabet("QwertyuiopaSdfghjklzxcvbnm"))
print(alphabet("QwertyuiopaSdf3ghjklzxcvbnm5"))
print(alphabet("W"))


# c
def comp(sir1, sir2):
    return set(sir1) == set(sir2)


print(comp("abv", "bva"))
print(comp("adb", "adB"))


# d
def subsets(m):
    finm = []
    for i in range(len(m) + 1):
        finm += itertools.combinations(list(m), i)
    return set(finm)


print(subsets({9, 0, 8, 9}))


# e
def cart(m1, m2):
    return {(x, y) for x in m1 for y in m2}


print(cart({1, 3, 4}, {1, 2}))
