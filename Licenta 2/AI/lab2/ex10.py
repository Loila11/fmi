# 1
def generate_dict(n1, n2):
    return {i:[j for j in range(1, i + 1) if i % j == 0] for i in range(n1, n2 + 1)}


print(generate_dict(3, 9))


# 2
def dict_tup_val(l):
    return {sum(x for x in li): tuple(x for x in li) for li in l}


print(dict_tup_val([[5,9,1],[1,4],[2,3],[5,3,0,7],[1,4,3,0,8]]))


# 3
def dict_tup_key(lt):
    return {t:[x for x in range(min(t), max(t)) if x not in t] for t in lt}


print(dict_tup_key([(3,7,9),(1,2,3,4),(10,3,5,6),(2,2),(6,7,1,2,4)]))
