print("Comenzi:\n1) scrie_continut\n2) scrie_cuvinte [ord|asc|desc]\n3) scrie_linii lin1-lin2\n4) iesire")
fisier = open("input.txt", "r")
log = open("log.txt", "a")

comanda = input()
log.write(comanda + '\n')
while comanda != "iesire":
    comanda = comanda.split()
    if comanda[0] == "scrie_continut":
        rez = open("rezultat_1.txt", "w+")
        continut = fisier.read()

        rez.write(continut)
        rez.close()
    elif comanda[0] == "scrie_cuvinte":
        rez = open("rezultat_2.txt", "w+")
        continut = fisier.read().lower().split()

        if comanda[1] == 'asc':
            continut.sort()
        elif comanda[1] == 'desc':
            continut.sort(reverse=True)

        for cuvant in continut:
            rez.write(cuvant + '\n')
        rez.close()
    else:
        rez = open("rezultat_3.txt", "w+")
        continut = fisier.readlines()

        lin = comanda[1].split('-')
        for i in range(len(continut)):
            if int(lin[0]) <= i <= int(lin[1]):
                rez.write(str(i) + ')' + continut[i])
        rez.close()

    fisier.seek(0)
    comanda = input()
    log.write(comanda + '\n')

log.write("###########################\n")
fisier.close()
log.close()
