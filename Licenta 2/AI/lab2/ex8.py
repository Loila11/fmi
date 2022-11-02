# 1
def all_let(l):
    return {x for sir in l for x in sir}


print(all_let(["abcd", "bau", "daca", "buf"]))


# 2
def even_col(m):
    return {l[i] for l in m for i in range(len(l)) if i % 2 == 0}


print(even_col([[0, 3], [4, 9], [5, 2]]))
