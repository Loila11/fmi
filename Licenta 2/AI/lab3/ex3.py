import random
import time


class Elev:
    index = 0

    def __init__(self, nume=None):
        self.sanatate = 90
        self.inteligenta = 20
        self.oboseala = 0
        self.dispozitie = 100

        self.nume = nume
        if nume is None:
            self.__class__.index += 1
            self.nume = 'Necunoscut_' + str(self.__class__.index)

        self.ore_activitate = {}
        self.bolnav = False
        self.absolvent = False
        self.activitate_curenta = None
        self.timp_executat_activ = 1

    def __repr__(self):
        return self.nume + ': ' + self.activitate_curenta.nume + ' ' + \
               str(self.timp_executat_activ) + '/' + \
               str(self.activitate_curenta.durata) + ' ' + \
               ' (sanatate ' + str(self.sanatate) + \
               ', inteligenta ' + str(self.inteligenta) + \
               ', oboseala ' + str(self.oboseala) + \
               ', buna dispozitie ' + str(self.dispozitie) + ')'

    def __getitem__(self, key):
        return self.__dict__[key]

    def __setitem__(self, key, value):
        self.__dict__[key] = value

    def actualizeaza_proprietate(self, proprietate, factor):
        self[proprietate] = max(0, min(100, self[proprietate] + factor / self.activitate_curenta.durata))
        self[proprietate] = round(self[proprietate], 2)

    def desfasoara_activitate(self):
        self.actualizeaza_proprietate('sanatate', self.activitate_curenta.factor_sanatate)
        self.actualizeaza_proprietate('inteligenta', self.activitate_curenta.factor_inteligenta)
        self.actualizeaza_proprietate('oboseala', self.activitate_curenta.factor_oboseala)
        self.actualizeaza_proprietate('dispozitie', self.activitate_curenta.factor_dispozitie)

        if self.oboseala == 100:
            if self.activitate_curenta.factor_sanatate > 0:
                self.actualizeaza_proprietate('sanatate', -(self.activitate_curenta.factor_sanatate / 2))
            if self.activitate_curenta.factor_inteligenta > 0:
                self.actualizeaza_proprietate('inteligenta', -(self.activitate_curenta.factor_inteligenta / 2))
            if self.activitate_curenta.factor_dispozitie > 0:
                self.actualizeaza_proprietate('dispozitie', -(self.activitate_curenta.factor_dispozitie / 2))

        if self.sanatate == 0 or self.dispozitie == 0:
            self.bolnav = True

        if self.inteligenta == 100:
            self.absolvent = True

    def trece_ora(self, ora):
        if self.activitate_curenta is None:
            return False

        self.ore_activitate[self.activitate_curenta.nume] += 1
        if (ora > 22 or ora <= 6) and self.activitate_curenta.nume != 'dormit':
            self.sanatate -= 1
        self.timp_executat_activ += 1
        return self.timp_executat_activ <= self.activitate_curenta.durata

    def testeaza_final(self):
        return self.bolnav or self.absolvent

    def afiseaza_raport(self):
        for activitate in self.ore_activitate:
            print(activitate + ' ' + str(self.ore_activitate[activitate]), end=' ')
        print('\n------------------------')


class Activitate:
    def __init__(self, nume, factor_sanatate, factor_inteligenta, factor_oboseala, factor_dispozitie, durata):
        self.nume = nume
        self.factor_sanatate = factor_sanatate
        self.factor_inteligenta = factor_inteligenta
        self.factor_oboseala = factor_oboseala
        self.factor_dispozitie = factor_dispozitie
        self.durata = durata

    def __repr__(self):
        return {'nume': self.nume,
                'factor sanatate': self.factor_sanatate,
                'factor inteligenta': self.factor_inteligenta,
                'factor oboseala': self.factor_oboseala,
                'factor dispozitie': self.factor_dispozitie,
                'durata': self.durata}


def ora_reala(ora):
    return (ora - 1) % 24 + 1


def trece_ora(act, elevi, ora):
    for elev in elevi:
        if not elev.trece_ora(ora):
            elev.activitate_curenta = act[random.randrange(len(act))]
            elev.timp_executat_activ = 1
            if elev.activitate_curenta.nume not in elev.ore_activitate:
                elev.ore_activitate[elev.activitate_curenta.nume] = 0
            elev.ore_activitate[elev.activitate_curenta.nume] += 1
        elev.desfasoara_activitate()
        if elev.testeaza_final():
            if elev.absolvent:
                print('Felicitari! ' + elev.nume + ' a absolvit!')
            else:
                print(elev.nume + ' s-a imbolnavit si a ajuns la spital')
            elev.afiseaza_raport()
            elevi.remove(elev)


def porneste_simulare(act, elevi, ora_start, ora_fin):
    for idx in range(ora_start, ora_fin):
        ora = ora_reala(idx)
        print('Ora ' + str(ora) + ':00')
        trece_ora(act, elevi, ora)
        for elev in elevi:
            print(elev)
        print('------------------------')
        time.sleep(1)

    comanda = input('comanda = ')
    if comanda == 'gata':
        return
    elif comanda == 'continua':
        ora = ora_fin
        while elevi:
            trece_ora(act, elevi, ora)
            ora = ora_reala(ora + 1)
        return
    elif comanda.isnumeric():
        porneste_simulare(act, elevi, ora_fin, ora_fin + int(comanda))
    else:
        print('Comanda nu este valida')
        porneste_simulare(act, elevi, ora_fin, ora_fin)


def citeste_activitati():
    act = []
    fisier_act = open('ex3.txt', 'r')
    lin = fisier_act.readline()
    while lin:
        arr = []
        for i in lin.split():
            if i.lstrip('-').isnumeric():
                arr.append(int(i))
            else:
                arr.append(i)
        if arr[1].__class__ is int:
            act.append(Activitate(*arr))
        lin = fisier_act.readline()
    return act


def citeste_elevi():
    return [Elev('Matei'), Elev('Ioana'), Elev(), Elev()]


if __name__ == '__main__':
    porneste_simulare(citeste_activitati(), citeste_elevi(), 9, 10)
