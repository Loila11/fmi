from string import ascii_lowercase

l = ["papagal", "pisica","soarece","bolovan","soparla","catel", "pasare", "zzzz"]


def print_matrice(m):
    for lin in m:
        print(lin)
    print()


# 1
def gen_matrice():
    m = []
    m += [list(' ' + ascii_lowercase)]
    for i in range(0, 26):
        m += [list(ascii_lowercase[i] + 26 * '0')]
    return m


matrice = gen_matrice()
print_matrice(matrice)


# 2
def completeaza_matrice(li, m):
    for k in li:
        anterior = []
        for g in k:
            i = m[0].index(g) - 1
            for h in anterior:
                j = ord(h) - ord('a')
                m[i + 1][j + 1] = str(int(m[i + 1][j + 1]) + 1)
            anterior += g
    return m


matrice = completeaza_matrice(l, matrice)
print_matrice(matrice)


# 3
j = 0
while j < len(matrice):
    lin = matrice[j]
    p = 0
    for i in range(1, len(lin)):
        if lin[i] != '0':
            p = 1
            break
    if p == 0:
        matrice.remove(lin)
    else:
        j += 1

j = 0
while j < len(matrice[0]):
    p = 0
    for i in range(1, len(matrice)):
        if matrice[i][j] != '0':
            p = 1
            break
    if p == 0:
        for i in range(0, len(matrice)):
            del matrice[i][j]
    else:
        j += 1

print_matrice(matrice)


# 4
N = 2
for i in range(1, len(matrice)):
    for j in range(i, len(matrice[i])):
        if int(matrice[i][j]) >= N:
            print("(" + matrice[i][0] + ", " + matrice[0][j] + ")")
