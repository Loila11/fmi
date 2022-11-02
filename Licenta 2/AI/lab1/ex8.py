l = ["margareta", "crizantema","lalea"," zorea , violeta, orhidee","trandafir","gerbera , iasomie","iris","crin "]


# 1
def add():
    s = input()
    if s in l:
        l.remove(s)
    l.append(s)


add()
print(l)


# 2
for i in range(0, len(l)):
    el = l[0].split()
    l.remove(l[0])
    for j in el:
        if j != ",":
            l.append(j.strip(","))
print(l)


# 3
def make_list(c, li):
    li_ch = []
    for i in li:
        if c in i:
            li_ch.append(i)
    return li_ch


l_ch = make_list("l", l)
print(l_ch)


# 4
l.sort()
print(l)

l.sort(reverse=True)
print(l)
