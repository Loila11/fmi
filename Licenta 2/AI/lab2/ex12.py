def eq(nume_fisier):
    fisier = open(nume_fisier, "r+")
    lines = fisier.readlines()

    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] += '=' + str(eval(lines[i])) + '\n'

    fisier.seek(0)
    for line in lines:
        fisier.write(line)

    fisier.close()


eq("ex12.txt")
