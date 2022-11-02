sir = input()

# 1
print(len(sir))


# 2
def isnotalnum(s):
    l = []
    for i in s:
        if not i.isalnum() and i != '-' and i not in l:
            l += i
    return l


l_ch = isnotalnum(sir)
print(l_ch)


# 3
l_cuv = sir.split()
for i in range(0, len(l_cuv)):
    for j in l_ch:
        l_cuv[i] = l_cuv[i].strip(j)
    l_cuv[i] = l_cuv[i].lower()
print(l_cuv)


# 4
l_masc = []
for i in l_cuv:
    if i.endswith("ul"):
        l_masc.append(i)
print(l_masc)


# 5
l_crat = []
for i in l_cuv:
    if i.find("-") > 0:
        l_crat.append(i)
print(l_crat)
