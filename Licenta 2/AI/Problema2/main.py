# Problema 2

import copy
import sys
import time
import pygame


class Joc:
    DIMENSIUNE = 10
    JMIN = 'O'
    JMAX = 'X'
    ESTIMARE_SCOR = 2
    ALGORITM = 2
    INTERFATA_GRAFICA = True

    def __init__(self, tabla=None, scor_jmin=0, scor_jmax=0):
        """ Informatia fiecarei casute este pastrata intr-o lista de liste.

        :param tabla: tabla de joc
        :param scor_jmin: scorul jucatorului JMIN
        :param scor_jmax: scorul jucatorului JMAX
        """
        self.scor_jmin = scor_jmin
        self.scor_jmax = scor_jmax

        if tabla is not None:
            self.tabla = tabla
        else:
            self.tabla = [[' ' for i in range(Joc.DIMENSIUNE)] for j in range(Joc.DIMENSIUNE)]
            self.tabla[0][0] = self.tabla[9][9] = 'O'
            self.tabla[0][9] = self.tabla[9][0] = 'X'

    def __str__(self):
        sir = ' '
        for i in range(Joc.DIMENSIUNE):
            sir += ' ' + str(i)

        sir += '\n  ' + '*-' * Joc.DIMENSIUNE + '*\n'
        for i in range(Joc.DIMENSIUNE):
            sir += str(i) + ' '
            for j in range(Joc.DIMENSIUNE):
                sir += '|' + self.tabla[i][j]
            sir += '|\n  ' + '*-' * Joc.DIMENSIUNE + '*\n'

        return sir

    def distanta_simbol(self, i, j, d, simbol):
        """ Calculeaza distanta pornind de la linia i si coloana j pe care o pot parcurge in directia d intalnind doar
         simbolul dat.

        :param i: indicele liniei
        :param j: indicele coloanei
        :param d: coeficientii directiei
        :param simbol: simbolul de numarat
        """
        linie = i + d[0]
        coloana = j + d[1]
        distanta = 0

        while 0 <= linie < Joc.DIMENSIUNE and 0 <= coloana < Joc.DIMENSIUNE and self.tabla[linie][coloana] == simbol:
            distanta += 1
            linie += d[0]
            coloana += d[1]

        return distanta

    def directie_valida(self, i, j, d, jucator):
        """ Returneaza 1 daca, dupa o serie continua de spatii goale in directia d se afla o casuta cu simbolul
        jucatorului curent, 0 altfel.

        :param i: indicele liniei
        :param j: indicele coloanei
        :param d: coeficientii directiei
        :param jucator: simbolul jucatorului curent
        """
        distanta = self.distanta_simbol(i, j, d, ' ')
        linie = i + distanta * d[0] + d[0]
        coloana = j + distanta * d[1] + d[1]

        return 1 if 0 <= linie < Joc.DIMENSIUNE and 0 <= coloana < Joc.DIMENSIUNE and \
                    self.tabla[linie][coloana] == jucator else 0

    def valid(self, i, j, jucator):
        """ Determina daca mutarea jucatorului pe linia i si coloana j este valida (este libera si se pot gasi doua
        simboluri de ale lui pe linia, coloana sau diagonalele care cuprind casuta curenta iar intre ele si pozitia
        actuala sunt doar casute libere).

        :param i: indicele liniei
        :param j: indicele coloanei
        :param jucator: simbolul jucatorului curent
        """
        if self.tabla[i][j] != ' ':
            return False

        d = self.directie_valida(i, j, [1, 0], jucator) + self.directie_valida(i, j, [-1, 0], jucator) + \
            self.directie_valida(i, j, [0, 1], jucator) + self.directie_valida(i, j, [0, -1], jucator) + \
            self.directie_valida(i, j, [1, 1], jucator) + self.directie_valida(i, j, [-1, -1], jucator) + \
            self.directie_valida(i, j, [1, -1], jucator) + self.directie_valida(i, j, [-1, 1], jucator)

        return d > 1

    def adauga_simbol(self, i, j, jucator):
        """ Adauga simbolul jucatorului pe tabla de joc.

        :param i: indicele liniei
        :param j: indicele coloanei
        :param jucator: simbolul jucatorului curent
        """
        self.tabla[i][j] = jucator

        if jucator == Joc.JMIN:
            self.scor_jmin += self.calculeaza_scor_mutare(i, j, jucator)
        else:
            self.scor_jmax += self.calculeaza_scor_mutare(i, j, jucator)

    def calculeaza_scor_directie(self, i, j, d, simbol):
        """ Calculeaza scorul pe o singura distanta al unei mutari.

        :param i: indicele liniei
        :param j: indicele coloanei
        :param d: coeficientii directiei
        :param simbol: simbolul jucatorului curent
        """
        return max(0,
                   min(3, self.distanta_simbol(i, j, d, simbol)) +
                   min(3, self.distanta_simbol(i, j, [-d[0], -d[1]], simbol)) - 2)

    def calculeaza_scor_mutare(self, i, j, jucator):
        """ Calculeaza scorul unei mutari.

        :param i: indicele liniei
        :param j: indicele coloanei
        :param jucator: simbolul jucatorului curent
        """
        return self.calculeaza_scor_directie(i, j, [1, 0], jucator) + \
               self.calculeaza_scor_directie(i, j, [0, 1], jucator) + \
               self.calculeaza_scor_directie(i, j, [1, 1], jucator) + \
               self.calculeaza_scor_directie(i, j, [-1, 1], jucator)

    def calculeaza_scor_1(self, jucator):
        """ Estimeaza scorul jucatorului curent.

        Scorul este egal cu scorul maxim posibil minus scorul adversarului.

        :param jucator: jucatorul curent
        """
        return (self.DIMENSIUNE - 3) * (2 * self.DIMENSIUNE - 3) - self.scor_jmax \
            if jucator == self.JMIN else (self.DIMENSIUNE - 3) * (2 * self.DIMENSIUNE - 3) - self.scor_jmin

    def calculeaza_scor_2(self, jucator):
        """ Estimeaza scorul jucatorului curent.

        Scorul este egal cu diferenta minima intre scorul pe care il poate avea jucatorul si cel pe care il va avea
        advesarul pentru aceeasi mutare.

        :param jucator: jucatorul curent
        """
        scor = self.scor_jmin - self.scor_jmax if jucator == self.JMIN else self.scor_jmin - self.scor_jmax
        jucator2 = urmatorul_jucator(jucator)

        for i in range(Joc.DIMENSIUNE):
            for j in range(Joc.DIMENSIUNE):
                scor = max(self.calculeaza_scor_mutare(i, j, jucator) - self.calculeaza_scor_mutare(i, j, jucator2),
                           scor)
        return scor

    def calculeaza_scor(self, jucator):
        """ Estimeaza scorul jucatorului curent in functie de varianta aleasa.

        :param jucator: jucatorul curent
        """
        return self.calculeaza_scor_1(jucator) if Joc.ESTIMARE_SCOR == 1 else self.calculeaza_scor_2(jucator)

    def estimare_scor(self):
        """ Estimeaza scorul jocului. """
        final = self.final()

        if final == Joc.JMAX:
            return 100000
        elif final == Joc.JMIN:
            return -100000
        elif final == "remiza":
            return 0
        return self.calculeaza_scor(Joc.JMAX) - self.calculeaza_scor(Joc.JMIN)

    def succesori(self, jucator):
        """ Genereaza mutarile posibile ale jucatorului actual.

        :param jucator: simbolul jucatorului curent
        """
        succesori = []
        for i in range(Joc.DIMENSIUNE):
            for j in range(Joc.DIMENSIUNE):
                if self.valid(i, j, jucator):
                    tabla = copy.deepcopy(self.tabla)
                    tabla[i][j] = jucator
                    succesori.append(Joc(tabla))
                    tabla[i][j] = ' '
        return succesori

    def final(self):
        """ Verifica daca starea actuala este finala. """
        if self.succesori(Joc.JMIN) and self.succesori(Joc.JMAX):
            return False

        if self.scor_jmin == self.scor_jmax:
            print("Este egalitate!")
        if self.scor_jmin > self.scor_jmax:
            print(f"{self.JMIN} a castigat!")
        else:
            print(f"{self.JMAX} a castigat!")
        return True


class Stare:
    def __init__(self, joc, jucator_curent, adancime, scor=None):
        self.joc = joc                          # joc curent
        self.jucator_curent = jucator_curent    # jucator curent
        self.adancime = adancime                # adancime
        self.scor = scor                        # scor
        self.mutari_posibile = []               # mutari posibile
        self.stare_aleasa = None                # starea urmatoare

    def __str__(self):
        return str(self.joc)

    def generare_succesori(self):
        """ Functia de generare a succesorilor.

        Pentru fiecare mutare posibila, adauga in lista o Stare formata din aceasta, urmatorul jucator si noua adancime.
        """
        jocuri = self.joc.succesori(self.jucator_curent)
        succesori = [Stare(joc, urmatorul_jucator(self.jucator_curent), self.adancime - 1)
                     for joc in jocuri if joc is not None]
        return succesori


class InterfataGrafica:
    DIMENSIUNE_CASUTA = 30
    DIMENSIUNE_ECRAN = (2 * Joc.DIMENSIUNE + 1) * DIMENSIUNE_CASUTA

    LINIE_ORIZONTALA = pygame.transform.scale(pygame.image.load('line.png'), (DIMENSIUNE_CASUTA, DIMENSIUNE_CASUTA))
    LINIE_VERTICALA = pygame.transform.rotate(LINIE_ORIZONTALA, 90)
    INTERSECTIE = pygame.transform.scale(pygame.image.load('intersection.png'), (DIMENSIUNE_CASUTA, DIMENSIUNE_CASUTA))
    CASUTA_GOALA = pygame.transform.scale(pygame.image.load('empty.png'), (DIMENSIUNE_CASUTA, DIMENSIUNE_CASUTA))
    X = pygame.transform.scale(pygame.image.load('x.png'), (DIMENSIUNE_CASUTA, DIMENSIUNE_CASUTA))
    O = pygame.transform.scale(pygame.image.load('o.png'), (DIMENSIUNE_CASUTA, DIMENSIUNE_CASUTA))

    def __init__(self):
        self.ecran = pygame.display.set_mode((self.DIMENSIUNE_ECRAN, self.DIMENSIUNE_ECRAN))


def urmatorul_jucator(jucator_curent):
    """ Gaseste urmatorul jucator.

    :param jucator_curent: jucatorul curent
    """
    return Joc.JMAX if jucator_curent == Joc.JMIN else Joc.JMIN


def min_max(stare):
    """ Algoritmul minimax.

    :param stare: starea curenta
    """
    if stare.adancime == 0 or stare.joc.final():
        stare.scor = stare.joc.estimare_scor()
        return stare

    stare.mutari_posibile = stare.generare_succesori()
    scor_mutari = [min_max(x) for x in stare.mutari_posibile]

    stare.stare_aleasa = max(scor_mutari, key=lambda x: x.scor) if stare.jucator_curent == Joc.JMAX \
        else min(scor_mutari, key=lambda x: x.scor)

    stare.scor = stare.stare_aleasa.scor
    return stare


def alpha_beta(alpha, beta, stare):
    """ Algoritmul alpha-beta.

    :param alpha: limita inferioara a scorului
    :param beta: limita superioara a scorului
    :param stare: starea curenta
    """
    if stare.adancime == 0 or stare.joc.final():
        stare.scor = stare.joc.estimare_scor()
        return stare

    if alpha > beta:
        return stare

    stare.mutari_posibile = stare.generare_succesori()
    scor_curent = float('-inf') if stare.jucator_curent == Joc.JMAX else float('inf')

    for move in stare.mutari_posibile:
        stare_noua = alpha_beta(alpha, beta, move)

        if stare.jucator_curent == Joc.JMAX:
            alpha = min(alpha, stare_noua.scor)

            if scor_curent < stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor
        else:
            beta = max(beta, stare_noua.scor)

            if scor_curent > stare_noua.scor:
                stare.stare_aleasa = stare_noua
                scor_curent = stare_noua.scor

        if alpha >= beta:
            break

    stare.scor = stare.stare_aleasa.scor
    return stare


def alege_algoritmul():
    """ Citeste algoritmul pe care jucatorul doreste sa il foloseasca. """
    while True:
        algoritm = input("Ce algoritm vrei sa utilizezi? (raspunde cu 1 sau 2)\n 1.Minimax\n 2.Alpha-beta\n ")

        if algoritm in ['1', '2']:
            break

        print("Raspunsul trebuie sa fie 1 sau 2.")

    Joc.ALGORITM = algoritm


def alege_simbol():
    """ Citeste simbolul cu care jucatorul doreste sa joace. """
    while True:
        Joc.JMIN = input("Vrei sa joci cu X sau cu O? (X incepe jocul)\n ").upper()

        if Joc.JMIN in ['X', 'O']:
            break

        print("Raspunsul trebuie sa fie X sau O.")

    Joc.JMAX = 'O' if Joc.JMIN == 'X' else 'X'


def alege_dificultatea():
    """ Citeste nivelul de dificultate al jocului preferat de jucator. """
    while True:
        dificultate = input("Alege dificultatea jocului (raspunde cu 1, 2 sau 3):\n "
                            "1.Usor\n 2.Avansat\n 3.Greu\n")

        if dificultate in ['1', '2', '3']:
            break

        print("Raspunsul trebuie sa fie 1, 2 sau 3.")

    return int(dificultate)


def alege_utilizarea_interfetei():
    """ Citeste preferinta jucatorului referitor la utilizarea interfetei grafice. """
    while True:
        tip_joc = input("Vrei sa folosesti interfata grafica? (raspunde cu 'da' sau 'nu')\n")

        if tip_joc in ['da', 'nu']:
            break

        print("Raspunsul trebuie sa fie 'da' sau 'nu'.")

    Joc.INTERFATA_GRAFICA = tip_joc == 'da'


def randul_jucatorului_interfata(stare, casute):
    """ Arata mutarile jucatorului pe interfata grafica.

    :param stare: starea actuala
    :param casute: seria de casute care contin informatia grafica
    """
    mutare_valida = False

    while not mutare_valida:
        for eveniment in pygame.event.get():
            if eveniment.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if eveniment.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()

                for linie in range(2 * Joc.DIMENSIUNE + 1):
                    for coloana in range(2 * Joc.DIMENSIUNE + 1):
                        if casute[linie][coloana].collidepoint(position):
                            mutare_valida = stare.joc.valid(linie // 2, coloana // 2, Joc.JMIN)
                            if mutare_valida:
                                stare.joc.adauga_simbol(linie // 2, coloana // 2, Joc.JMIN)


def randul_jucatorului(stare):
    """ Realizeaza mutarea jucatorului.

    :param stare: starea actuala
    """
    mutare_valida = False
    
    while not mutare_valida:
        try:
            linie = input("linia = ")
            if linie == "exit":
                return None
            linie = int(linie)

            coloana = input("coloana = ")
            if coloana == "exit":
                return None
            coloana = int(coloana)

            if linie in range(Joc.DIMENSIUNE) and coloana in range(Joc.DIMENSIUNE) and \
                    stare.joc.valid(linie, coloana, Joc.JMIN):
                stare.joc.adauga_simbol(linie, coloana, Joc.JMIN)
                mutare_valida = True
            else:
                print("Linie sau coloana invalida.")

        except ValueError:
            print("Linia si coloana introduse trebuie sa fie numere naturale.")

    return stare


def randul_calculatorului(stare):
    """ Realizeaza mutarea calculatorului.

    :param stare: starea actuala
    """
    if Joc.ALGORITM == '1':
        stare.joc = min_max(stare).stare_aleasa.joc
    else:
        stare.joc = alpha_beta(-5000, 5000, stare).stare_aleasa.joc
    return stare


def afiseaza_tabla_de_joc(tabla, interfata):
    """ Afiseaza tabla de joc pe interfata grafica.

    :param tabla: tabla curenta de joc
    :param interfata: constantele specifice interfetei grafice
    """
    casute = []
    interfata.ecran.fill((255, 255, 255))

    for linie in range(2 * Joc.DIMENSIUNE + 1):
        serie_casute = []

        for coloana in range(2 * Joc.DIMENSIUNE + 1):
            zona = pygame.Rect(coloana * (interfata.DIMENSIUNE_CASUTA + 1), linie * (interfata.DIMENSIUNE_CASUTA + 1),
                               interfata.DIMENSIUNE_CASUTA, interfata.DIMENSIUNE_CASUTA)
            serie_casute.append(zona)
            pygame.draw.rect(interfata.ecran, (255, 255, 255), zona)
            
            if linie % 2 == 0 and coloana % 2 == 0:
                interfata.ecran.blit(interfata.INTERSECTIE, 
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))
            elif linie % 2 == 0:
                interfata.ecran.blit(interfata.LINIE_ORIZONTALA,
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))
            elif coloana % 2 == 0:
                interfata.ecran.blit(interfata.LINIE_VERTICALA,
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))
            elif linie % 2 == coloana % 2 == 1 and tabla[linie // 2][coloana // 2] == 'X':
                interfata.ecran.blit(interfata.X, 
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))
            elif linie % 2 == coloana % 2 == 1 and tabla[linie // 2][coloana // 2] == 'O':
                interfata.ecran.blit(interfata.O, 
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))
            else:
                interfata.ecran.blit(interfata.CASUTA_GOALA, 
                                     (coloana * interfata.DIMENSIUNE_CASUTA, linie * interfata.DIMENSIUNE_CASUTA))

        casute.append(serie_casute)

    pygame.display.flip()
    return casute


def seteaza_optiunile_jocului():
    """ Prezinta meniul cu optiunile jocului si ii permite jucatorului sa isi aleaga preferintele. """
    print("Scrie numarul corespunzator unei optiuni pentru a schimba setarile predefinite sau pentru a incepe jocul.\n" 
          "Meniu:\n"
          "1. Alege algoritmul utilizat de calculator (minimax sau alpha-beta).\n"
          "2. Alege cu ce simbol vrei sa joci\n"
          "3. Alege nivelul de dificultate al jocului\n"
          "4. Alege daca vrei sa joci cu sau fara interfata grafica\n"
          "5. Incepe jocul\n"
          "Pentru a opri jocul inainte de final introdu 'exit' in timpul turei tale\n")

    adancime = 2
    while True:
        optiune = input()

        if optiune == '1':
            alege_algoritmul()
        elif optiune == '2':
            alege_simbol()
        elif optiune == '3':
            adancime = alege_dificultatea()
        elif optiune == '4':
            alege_utilizarea_interfetei()
        elif optiune == '5':
            return Stare(Joc(), 'X', adancime)
        else:
            print("Valoarea introdusa trebuie sa fie un numar intre 1 si 5.")

        print("Alege alta optiune din meniu. Tasteaza 5 pentru a incepe jocul.")


def main():
    """ Functia principala a programului. """
    if len(sys.argv) > 1:
        stare = Stare(Joc(), 'X', 2)
    else:
        stare = seteaza_optiunile_jocului()

    if Joc.INTERFATA_GRAFICA:
        pygame.init()
        pygame.display.set_caption('Problema 2')
        interfata = InterfataGrafica()
        casute = afiseaza_tabla_de_joc(stare.joc.tabla, interfata)
    else:
        print(f"\nTabla initiala de joc:\n {stare.joc}")
    
    mutarile_jucatorului = 0
    mutarile_calculatorului = 0
    timp_inceput_joc = int(round(time.time() * 1000))
    final = False

    while not final:
        timp_inceput_runda = int(round(time.time() * 1000))

        if stare.jucator_curent == Joc.JMIN:
            print("Randul jucatorului:")
            mutarile_jucatorului += 1

            if Joc.INTERFATA_GRAFICA:
                randul_jucatorului_interfata(stare, casute)
            else:
                check_exit = randul_jucatorului(stare)

                if check_exit is None:
                    break
        else:
            print("Randul calculatorului:")
            mutarile_calculatorului += 1
            randul_calculatorului(stare)

        if Joc.INTERFATA_GRAFICA:
            casute = afiseaza_tabla_de_joc(stare.joc.tabla, interfata)
        else:
            print(f"\nTabla dupa mutare:\n {stare}")

        timp_sfarsit_runda = int(round(time.time() * 1000))
        print(f"Timp de gandire: {timp_sfarsit_runda - timp_inceput_runda} milisecunde.\n")

        final = stare.joc.final()
        stare.jucator_curent = urmatorul_jucator(stare.jucator_curent)

    if Joc.INTERFATA_GRAFICA:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()

    timp_sfarsit_joc = int(round(time.time() * 1000))
    print(f"\nTimpul total de joc: {timp_sfarsit_joc - timp_inceput_joc} milisecunde.\n\n"
          f"Ai facut {mutarile_jucatorului} mutari.\n"
          f"Calculatorul a facut {mutarile_calculatorului} mutari.\n\n"
          f"Scorul jucatorului: {stare.joc.scor_jmin}\n"
          f"Scorul calculatorului: {stare.joc.scor_jmax}")


if __name__ == "__main__":
    main()
