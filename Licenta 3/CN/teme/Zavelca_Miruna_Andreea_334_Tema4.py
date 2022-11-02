# python --version: 3.8.6
import numpy as np
import matplotlib.pyplot as plt


# ----------------------------------------------- EXERCITIUL 1 ---------------------------------------------------------


def f1(x):
    """ Functia data la exercitiul 1.

    :param x: parametrul x
    :return: rezultatul functiei in punctul x
    """
    return np.cos(0.3 * x)


def f1dd(x):
    """ Derivata de ordin 2 a functiei f1.

    :param x: parametrul x
    :return: rezultatul derivatei in punctul x
    """
    return -0.09 * np.cos(0.3 * x)


def met_diferentelor_finite(divs):
    """ Pentru un set de diviziuni dat, determina a doua derivata a functiei folosind metoda diferentelor finite.

    :param divs: diviziunile intervalului
    :return: functie care determina a doua derivata in a i-a diviziune
    """
    h = divs[1] - divs[0]

    def eval_s(i):
        return (f1(divs[i + 2]) - 2 * f1(divs[i + 1]) + f1(divs[i])) / (h ** 2)

    return eval_s


def gaseste_N_minim(a, b, et, f, f_aprox):
    """ Determina cel mai mic N astfel incat eroarea maxima de trunchiere sa satisfaca relatia data.

    :param a: limita inferioara de definitie a functiei
    :param b: limita superioara de definitie a functiei
    :param et: limita superioara acceptata a erorii de trunchiere
    :param f: functia pentru care calculez acest N
    :param f_aprox: functia care aproximeaza valorile functiei
    :return: N-ul cerut
    """
    N = 4
    divs = np.linspace(a, b, N)
    y_aprox = f_aprox(divs)

    while np.linalg.norm([np.max([np.abs(y_aprox(i) - f(divs[i + 1])) for i in range(N - 2)])], ord=np.inf) > et:
        N = N + 1
        divs = np.linspace(a, b, N)
        y_aprox = f_aprox(divs)

    return N


def grafic_functie(divs, f, f_aprox):
    """ Reprezentarea grafica a functiei f si a aproximarii acesteia.

    :param divs: diviziunile intervalului
    :param f: functia reala
    :param f_aprox: aproximarea functiei
    :return: None
    """
    plt.title('Derivata a doua a functiei si aproximarea numerica obtinuta')
    plt.plot(divs, [f(div) for div in divs])
    plt.scatter(divs[1:-1], [f_aprox(i) for i in range(len(divs) - 2)])
    plt.show()


def grafic_eroare(divs, f, f_aprox):
    """ Reprezentarea grafica a erorii de trunchiere.

    :param divs: diviziunile intervalului
    :param f: functia reala
    :param f_aprox: aproximarea functiei
    :return: None
    """
    plt.title('Eroarea de trunchiere')
    plt.plot(divs[1:-1], [np.abs(f(divs[i + 1]) - f_aprox(i)) for i in range(len(divs) - 2)])
    plt.show()


def ex1():
    """ Sa se aproximeze a doua derivata a functiei folosind metoda diferentelor finite.
        1. Sa se reprezinte grafic derivata a doua exacta a functiei si aproximarea numerica obtinuta. Numarul de puncte
         al discretizarii intervalului, N, se va alege cel mai mic posibil astfel incat eroarea maxima de trunchiere sa
         satisfaca relatia ||e_{t}||_{inf} <= 1e-5.
        2. Sa se reprezinte intr-o figura noua eroare de trunchiere.

    :return: None
    """
    a = -np.pi / 2
    b = np.pi
    et = 1e-5

    N = gaseste_N_minim(a, b, et, f1dd, met_diferentelor_finite)
    divs = np.linspace(a, b, N)
    f_aprox = met_diferentelor_finite(divs)

    # 1
    grafic_functie(divs, f1dd, f_aprox)

    # 2
    grafic_eroare(divs, f1dd, f_aprox)


# ----------------------------------------------- EXERCITIUL 2 ---------------------------------------------------------


def f2(x, sigma=1.0):
    """ Functia data la exercitiul 2.

    :param x: parametrul x
    :param sigma: parametrul sigma
    :return: rezultatul functiei in punctul x
    """
    assert -10 <= x <= 10, 'Parametrul dat nu se afla in domeniul de definitie'
    return np.e ** (- x ** 2 / (2 * (sigma ** 2))) / sigma * np.sqrt(2 * np.pi)


def formula_dreptunghiului(f, a, b):
    """ Formula de cuadratura a dreptunghiului.

    :param f: functia de integrat
    :param a: primul nod al cuadraturii
    :param b: ultimul nod al cuadraturii
    :return: aproximarea integralei pe intervalul [a, b]
    """
    h = (b - a) / 2
    return f((a + b) / 2) * 2 * h


def formula_trapezului(f, a, b):
    """ Formula de cuadratura a trapezului.

    :param f: functia de integrat
    :param a: primul nod al cuadraturii
    :param b: ultimul nod al cuadraturii
    :return: aproximarea integralei pe intervalul [a, b]
    """
    h = (b - a) / 2
    return (f(a) + f(b)) * h


def formula_Simpson(f, a, b):
    """ Formula de cuadratura Simpson.

    :param f: functia de integrat
    :param a: primul nod al cuadraturii
    :param b: ultimul nod al cuadraturii
    :return: aproximarea integralei pe intervalul [a, b]
    """
    h = (b - a) / 2
    return f(a) * h / 3 + f(a + h) * 4 * h / 3 + f(b) * h / 3


def integrare(f, x, metoda):
    """ Calculeaza valoarea aproximativa a integralei conform formulei de cuadratura primite ca parametru.

    :param f: functia de integrat
    :param x: o diviziune a intervalului
    :param metoda: metoda de cuadratura utilizata
    :return: integrala functiei
    """
    assert metoda in ['dreptunghi', 'trapez', 'Simpson'], 'Metoda nu se afla in lista de valori acceptate'

    formula = formula_dreptunghiului if metoda == 'dreptunghi' else formula_trapezului if metoda == 'trapez' \
        else formula_Simpson

    return sum([formula(f, x[i], x[i + 1]) for i in range(len(x) - 1)])


def ex2():
    """ Creati functia integrare care calculeaza valoarea aproximativa a integralei I(f) = Int[a -> b] f(x) dx conform
    formulelor de cuadratura sumate a dreptunghiului, trapezului si Simpson si are ca date de intrare:
        * functia de integrat f
        * vectorul x, o diviziune a intervalului [a, b]
        * sirul de caractere metoda in {'dreptunghi', 'trapez', 'Simpson'}
    iar ca date de iesire:
        * aproximarea numerica a integralei I(f).

    Sa se aproximeze valoarea integralei I(f) = Int[a -> b] f(x) dx pentru functia data, folosind cele 3 metode
    mentionate mai sus.

    :return: None
    """
    a = -10
    b = 10

    N = 1000
    x = np.linspace(a, b, N)

    print("Aproximarea integralei conform formulei de cuadratura sumate a dreptunghiului:\n"
          f"{integrare(f2, x, 'dreptunghi')}\n"
          "Aproximarea integralei conform formulei de cuadratura sumate a trapezului:\n"
          f"{integrare(f2, x, 'trapez')}\n"
          "Aproximarea integralei conform formulei de cuadratura sumate Simpson:\n"
          f"{integrare(f2, x, 'Simpson')}")


# -------------------------------------------------- MAIN --------------------------------------------------------------


def main():
    ex1()
    ex2()


if __name__ == '__main__':
    main()
