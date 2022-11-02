l = ["co-pa-cel", "pa-pu-cel","a-bac","021-220-20-10","1-pi-tic","go-go-nea","tip-til","123-456","a-co-lo","lo-go-ped","pa-pa-gal","co-co-starc"]

# 1
d = {"vocale": "aeiou", "consoane": "bcdfghjklmnpqrstvxyz", "cifre": "0123456789"}

# 2
d2 = {}
for k in l:
    el = k.split("-")
    for i in el:
        if i not in d2:
            d2[i] = []
        if k not in d2[i]:
            d2[i] += [k]

print(d2)

# 3
cifre = []
for k in d2:
    if k.isdigit():
        cifre.append(k)

for k in cifre:
    if k in d2:
        print(k + ": " + str(d2[k]))
        del d2[k]

# 4
print(len(d2))

# 5
cvc = []
voc = "aeiou"
for k in d2:
    if len(k) == 3 and k[0] not in voc and k[1] in voc and k[2] not in voc:
        cvc.append(k)

print(cvc)
