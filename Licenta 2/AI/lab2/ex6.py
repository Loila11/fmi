def suma():
    fisier = open("ex6.txt", "r")
    l = [line.split() for line in fisier]
    s = 0
    for lin in l:
        if len(lin) != 0 and len(lin) != len(l[0]):
            raise Exception("Liniile nu au aceeasi lungime")
        for el in lin:
            s += int(el)
    print(s)


try:
    suma()
except IOError:
    print("Nu se gaseste fisierul")
except ValueError:
    print("Matricea nu e formata doar din numere")
except Exception as eroare:
    print(eroare)
