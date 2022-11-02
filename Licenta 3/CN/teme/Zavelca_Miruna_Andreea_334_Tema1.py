import numpy as np
import matplotlib.pyplot as plt
import math


# ---------------------------------------------- FUNCTII COMUNE --------------------------------------------------------


def valori_intermediare(f, a, b, epsilon):
    # verific conditiile de intrare
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'

    # setez datele initiale
    n = math.floor(np.log2((b - a) / epsilon))

    for i in range(1, n):
        # aplic un pas al metodei valorilor intermediare
        if f(a) * f((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2

    return (a + b) / 2


def make_graph(f, g_min, g_max, res_x, res_y):
    """
        Construiesc graficul unei singure functii
    """
    x = np.linspace(g_min, g_max, 100)

    # trasez graficul pentru functia f
    plt.plot(x, f(x))

    # trasez axele graficului
    plt.plot([0, 0], [min(0, g_min), g_max], 'black', linewidth=0.5)
    plt.plot([min(0, g_min), g_max], [0, 0], 'black', linewidth=0.5)

    # denumesc axele graficului
    plt.xlabel('x')
    plt.ylabel('y')

    # adaug punctele de intersectie ale functiei cu axa Ox
    plt.scatter(res_x, res_y, color='green')

    # afisez graficul
    plt.show()


# ----------------------------------------------- EXERCITIUL 1 ---------------------------------------------------------


def f1(x):
    # ecuatia de rezolvat pentru exercitiul 1
    return x * x - 13


def ex1():
    """
        Notez cu x rezultatul cautat. Atunci:
         x = sqrt(13) <=> x ^ 2 = 13 <=> x ^ 2 - 13 = 0
        Ecuatia la care am ajuns se afla in functia f1(x). f1(x) este o functie continua, de clasa C2.
         sqrt(13) > 0, deci x > 0.
        Pe intervalul [0, inf), f1(x) este strict crescatoare, deci are solutie unica.
         3 ^ 2 = 9 < 13 < 16 = 4 ^ 2
        Aleg [3, 4] intervalul in care caut solutia ecuatiei si aplic metoda valorilor intermediare, explicata in curs.
    """
    # setez limitele intervalului pentru care voi rezolva ecuatia
    g_min = 3
    g_max = 4

    # setez precizia solutiei
    eps = 1e-7

    # rezolvarea ecuatiei cu datele setate anterior
    res = valori_intermediare(f1, g_min, g_max, eps)
    print('Exercitiul 1: ' + str(res))


# ----------------------------------------------- EXERCITIUL 2 ---------------------------------------------------------


def f2l(x):
    # functia din stanga '=' la exercitiul 2
    return np.e ** (x - 2)


def f2r(x):
    # functia din dreapta '=' la exercitiul 1
    return np.cos(np.e ** (x - 2)) + 1


def f2(x):
    # ecuatia de rezolvat pentru exercitiul 2
    return f2l(x) - f2r(x)


def make_graph_2(f1_, f2_, g_min, g_max, res):
    """
        Construiesc graficul pentru doua functii si punctul de intersectie al acestora
    """
    x = np.linspace(g_min, g_max, 100)

    # trasez graficul pentru functia din stanga '='
    plt.plot(x, f1_(x))
    # trasez graficul pentru functia din dreapta '='
    plt.plot(x, f2_(x))

    # setez limitele intervalului pe care il voi afisa grafic
    plt.gca().set_ylim(g_min, g_max)
    plt.gca().set_xlim(g_min, g_max)

    # trasez axele graficului
    plt.plot([0, 0], [min(0, g_min), g_max], 'black', linewidth=0.5)
    plt.plot([min(0, g_min), g_max], [0, 0], 'black', linewidth=0.5)

    # denumesc axele graficului
    plt.xlabel('x')
    plt.ylabel('y')

    # adaug punctul de intersectie al celor doua functii
    plt.scatter([res], [f1_(res)], color='green')

    # afisez graficul
    plt.show()


def ex2():
    """
        Am pus functia din stanga egalului in f2s, functia din dreapta in f2d,
         iar ecuatia e ^ (x - 2) - cos (e ^ (x - 2)) - 1 in f2(x). f2(x) este o functie continua, monotona, de clasa C2.
        Se observa ca este monotona de pe grafic. Pentru cazul in care este necesara o demonstratie:
         f2'(x) = e ^ (x - 2) + e ^ (x - 2) * sin(e ^ (x - 2)) = e ^ (x - 2) (1 + sin(e ^ (x - 2))) (*)
         e ^ (x - 2) > 0 oricare x in R (**)
         sin(e ^ (x - 2)) >= -1     => 1 + sin(e ^ (x - 2)) >= 0 oricare x in R (***)
         Din (*), (**) si (***) => f2'(x) >= 0 oricare x in R
         O functie este monotona daca derivata nu isi schimba semnul => f2 este monotona => functia are solutie unica

        Se observa empiric f2(-2) < 0 < f(6)
        Aleg [-2, 6] intervalul in care caut solutia ecuatiei si aplic metoda valorilor intermediare pentru a afla
         punctul in care ecuatia se intersecteaza cu axa Ox. Acesta este punctul de intersectie al celor doua functii.
        Creez graficul celor doua functii, cu punctul lor de intersectie.
    """
    # setez limitele intervalului pentru care voi rezolva ecuatia
    g_min = -2
    g_max = 6

    # setez precizia solutiei
    eps = 1e-3

    # rezolv ecuatia cu datele setate anterior
    res = valori_intermediare(f2, g_min, g_max, eps)
    print('Exercitiul 2: ' + str(res))

    # ilustrez grafic cele doua functii si punctul lor de intersectie
    make_graph_2(f2l, f2r, g_min, g_max, res)


# ----------------------------------------------- EXERCITIUL 3 ---------------------------------------------------------


def f3(x):
    # ecuatia de rezolvat pentru exercitiul 3
    return x ** 3 + 6 * (x ** 2) - x - 30


def df3(x):
    # derivata de ordin I
    return 3 * (x ** 2) + 12 * x - 1


def ddf3(x):
    # derivata de ordin II
    return 6 * x + 12


def pozitie_falsa(f, a, b, eps):
    # verific conditiile de intrare
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df3(a)) * np.sign(df3(b)) > 0, 'f\' se anuleaza pe [a, b]'
    assert np.sign(ddf3(a)) * np.sign(ddf3(b)) > 0, 'f" se anuleaza pe [a, b]'

    # setez datele initiale
    n = 0
    x = (a * f(b) - b * f(a)) / (f(b) - f(a))

    while True:
        # aplic un pas al metodei pozitiei false
        n = n + 1
        x_old = x

        # actualizez a, b si x pentru pasul actual
        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        elif f(a) * f(x) > 0:
            a = x
        x = (a * f(b) - b * f(a)) / (f(b) - f(a))

        # verific conditia de iesire
        if np.abs(x - x_old) / np.abs(x_old) < eps:
            break

    return x, n


def ex3():
    """
        Am definit functia pozitie_falsa conform descrierii din curs.
        Ecuatia data se afla in f3(x).
        Una dintre solutiile problemei este capatul inferior al intervalului. Din acest motiv, nu se poate alege un
            interval care sa respecte datele de intrare pentru metoda pozitiei false (sign(f(a)) * sign(f(b)) = 0).
            Pentru a rezolva aceasta problema, am extins intervalul la [-5.1, 5].
        Am ales empiric cele 3 subintervale: [-5.1, -4.5], [-4, -2.1], [1, 5].
        Am ilustrat functia si solutiile sale folosind functia make_graph.
    """
    # setez intervalul de definitie al functiei
    g_min = -5.1
    g_max = 5

    # setez precizia solutiei
    eps = 1e-5

    # rezolv pentru trei subintervale
    res1, n1 = pozitie_falsa(f3, -5.1, -4.5, eps)
    res2, n2 = pozitie_falsa(f3, -4, -2.1, eps)
    res3, n3 = pozitie_falsa(f3, 1, 5, eps)

    # construiesc vectorii cu solutiile
    res_x = [res1, res2, res3]
    res_y = [f3(res1), f3(res2), f3(res3)]

    # afisez solutiile ecuatiei
    print('Exercitiul 3: ' + str(res_x))

    # creez graficul functiei
    make_graph(f3, g_min, g_max, res_x, res_y)


# ----------------------------------------------- EXERCITIUL 4 ---------------------------------------------------------


def f4(x):
    # ecuatia de rezolvat pentru exercitiul 4
    return x ** 3 + 3 * (x ** 2) - 4 * x - 12


def df4(x):
    # derivata de ordin I
    return 3 * (x ** 2) + 6 * x - 4


def secanta(f, a, b, x0, x1, eps):
    # verific conditiile de intrare
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df4(a)) * np.sign(df4(b)) > 0, 'f\' se anuleaza pe [a, b]'

    # setez datele initiale
    n = 1

    while np.abs(x1 - x0) / np.abs(x0) >= eps:
        # aplic un pas al metodei secantei
        n = n + 1
        x = (x0 * f(x1) - x1 * f(x0)) / (f(x1) - f(x0))

        # verific ca x-ul actual sa se afle in continuare in intervalul dat
        assert a < x < b, 'Introduceti alte valori pentru x0, x1'

        # actualizez ultimele doua valori ale lui x
        x0 = x1
        x1 = x

    return x1, n


def ex4():
    """
        Am definit functia secanta conform descrierii din curs.
        Ecuatia data se afla in f4(x).
        Una dintre solutiile problemei este capatul inferior al intervalului. Din acest motiv, nu se poate alege un
            interval care sa respecte datele de intrare pentru metoda secantei (sign(f(a)) * sign(f(b)) = 0).
            Pentru a rezolva aceasta problema, am extins intervalul la [-3.1, 3].
        Am ales empiric cele 3 subintervale: [-3.1, -2.6], [-2.5, -1], [1, 3] si x0, x1 capetele intervalelor.
        Am ilustrat functia si solutiile sale folosind functia make_graph.
    """
    # setez intervalul de definitie al functiei
    g_min = -3.1
    g_max = 3

    # setez precizia solutiei
    eps = 1e-5

    # rezolv pentru trei subintervale
    res1, n1 = secanta(f4, -3.1, -2.6, -3.1, -2.6, eps)
    res2, n2 = secanta(f4, -2.5, -1, -2.5, -1, eps)
    res3, n3 = secanta(f4, 1, 3, 1, 3, eps)

    # construiesc vectorii solutiilor
    res_x = [res1, res2, res3]
    res_y = [f4(res1), f4(res2), f4(res3)]

    # afisez solutiile ecuatiei
    print('Exercitiul 4: ' + str(res_x))

    # creez graficul functiei
    make_graph(f4, g_min, g_max, res_x, res_y)


# -------------------------------------------------- MAIN --------------------------------------------------------------


def main():
    ex1()
    ex2()
    ex3()
    ex4()


if __name__ == '__main__':
    main()
