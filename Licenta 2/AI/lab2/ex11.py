fisier = open("ex11.txt", "r")

l = []
for linie in fisier:
    loc = int(linie[:linie.find(":")])
    while loc >= len(l):
        l.append("gol")
    l[loc] = linie[(linie.find(":") + 1):].strip("\n")

print(l)
