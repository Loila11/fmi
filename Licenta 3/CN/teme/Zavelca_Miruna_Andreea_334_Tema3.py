# python --version: 3.8.6
import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------- FUNCTII COMUNE --------------------------------------------------------


def find_smallest_N(a, b, et, f, f_aprox):
    """ Determina cel mai mic N astfel incat eroarea maxima de trunchiere sa satisfaca relatia data.

    :param a: limita inferioara de definitie a functiei
    :param b: limita superioara de definitie a functiei
    :param et: limita superioara acceptata a erorii de trunchiere
    :param f: functia pentru care calculez acest N
    :param f_aprox: functia care aproximeaza valorile functiei
    :return: N-ul cerut
    """
    N = 2
    divs = [a, b]
    PN = f_aprox(divs)

    while np.linalg.norm([np.max([np.abs(PN(i) - f(i)) for i in np.arange(a, b, 0.5)])], ord=np.inf) > et:
        N = N + 1
        divs = np.linspace(a, b, N)
        PN = f_aprox(divs)

    return N


def show_function(divs, f, f_aprox):
    plt.title('Functia exacta, nodurile de interpolare si aproximarea numerica obtinuta')
    plt.plot(divs, [f(div) for div in divs])
    plt.scatter(divs, [f_aprox(div) for div in divs])
    plt.show()


def show_error(divs, f, f_aprox):
    plt.title('Eroarea de trunchiere')
    plt.plot(divs, [np.abs(f(div) - f_aprox(div)) for div in divs])
    plt.show()


# ----------------------------------------------- EXERCITIUL 1 ---------------------------------------------------------


def f1(x, y):
    """ Functia data la exercitiul 1.

    :param x: parametrul x
    :param y: parametrul y
    :return: rezultatul functiei pentru x si y date
    """
    return 4.5 * (x ** 2) - 12.0 * x * y - 3 * x + 20.5 * (y ** 2) + 5 * y


def simetrica(a):
    """ Verifica daca matricea patratica A este simetrica.

    :param a: matricea patratica A
    :return: True daca matricea e simetrica, False altfel
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    # Verificarea simetriei
    return np.size([1 for i in range(a.shape[0]) for j in range(i) if a[i, j] != a[j, i]]) == 0


def pozitiv_definita(a):
    """ Verifica daca matricea patratica A este pozitiv definita.

    :param a: matricea patratica A
    :return: True daca matricea e pozitiv definita, False altfel
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    # Verificarea minorilor principali (criteriul lui Sylvester).
    return np.size([1 for i in range(a.shape[0]) if np.linalg.det(a[:i, :i]) == 0]) == 0


def admite_minim_unic(a):
    """ Verifica daca functia admite un punct de minim <=> matricea A este simetrica si pozitiv definita.

    :return: None
    """

    # Verificarea conditiilor de intrare: A matrice patratica, simetrica si pozitiv definita.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert simetrica(a), 'Matricea corespunzatoare functiei nu este simetrica!'
    assert pozitiv_definita(a), 'Matricea corespunzatoare functiei nu este pozitiv definita!'

    return all(a[i][i] > 0 for i in range(a.shape[0]))


def grid_discret(a, b, size=50):
    """ Construieste un grid discret si evaleaza f1 in fiecare punct al gridului.

    :param a: matricea A
    :param b: vectorul b
    :param size: numarul de puncte pe fiecare axa
    :return: grid pe planul determinat de axele x1 si x2 si evaluarea functiei pentru fiecare coordonata
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    x1 = np.linspace(-4, 6, size)  # Axa x1
    x2 = np.linspace(-6, 4, size)  # Axa x2
    X1, X2 = np.meshgrid(x1, x2)  # Creeaza un grid pe planul determinat de axele x1 si x2

    X3 = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.array([X1[i, j], X2[i, j]])  # vectorul ce contine coordonatele unui punct din gridul definit mai sus
            X3[i, j] = .5 * x @ a @ x - x @ b  # Evaluam functia in punctul x

    return X1, X2, X3


def curbe_nivel(a, b, levels=10):
    """ Construieste curbele de nivel ale functiei f1.

    :param a: matricea A
    :param b: vectorul b
    :param levels: numarul de linii de nivel
    :return: None
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    # Construieste gridul asociat functiei
    (X1, X2, X3) = grid_discret(a, b)

    # Ploteaza curbele de nivel ale functiei f
    plt.contour(X1, X2, X3, levels=levels)

    # Etichete pe axe
    plt.xlabel('x1')
    plt.ylabel('x2')

    # Titlu
    plt.title('Curbele de nivel ale functiei f')

    # Afiseaza figura
    plt.show()


def met_pasului_descendent(a, b, x):
    """ Afla punctul de minim al functiei biliniare definite de matricea A si vectorul b folosind metoda pasului
    descendent.

    :param a: matricea A
    :param b: vectorul b
    :param x: punctul initial [x0, y0]
    :return: punctul de minim al functiei f1
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    h = b - a @ x
    while np.linalg.norm(h, ord=2) > 1e-10:
        alpha = (np.transpose(h) @ h) / (np.transpose(h) @ a @ h)
        x = x + alpha * h
        h = b - a @ x

    return x


def met_gradientilor_conjugati(a, b, x):
    """ Afla punctul de minim al functiei biliniare definite de matricea A si vectorul b folosind metoda gradientilor
    conjugati.

    :param a: matricea A
    :param b: vectorul b
    :param x: punctul initial [x0, y0]
    :return: punctul de minim al functiei f1
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    d = h = b - a @ x
    while np.linalg.norm(h, ord=2) > 1e-10:
        alpha = (np.transpose(h) @ h) / (np.transpose(d) @ a @ d)
        x = x + alpha * d
        h1 = h - alpha * a @ d
        beta = (np.transpose(h1) @ h1) / (np.transpose(h) @ h)
        h = h1
        d = h + beta * d

    return x


def ex1():
    """ Sa se verifice daca forma biliniara admite un punct de minim unic si in caz afirmativ sa se determine acesta
    folosind:
        1. Metoda pasului descendent
        2. Metoda gradientilor conjugati
    TODO: Sa se reprezinte pe graficul curbelor de nivel aproximarea obtinuta la fiecare iteratie pentru cele doua metode.


    f(x, y) = 1/2 * a11 * (x ** 2) + a12 * x * y + 1/2 * a22 * (y ** 2) - b1 * x - b2 * y

    =>  1/2 * a11 = 4.5
        a12 = - 12.0
        1/2 * a22 = 20.5
        - b1 = - 3.0
        - b2 = 5.0

    =>  A = [  9 -12]
            [-12  41]
        b = [3]
            [-5]

    :return: None
    """
    a = np.array([[9, -12], [-12, 41]])
    b = np.array([[3], [-5]])

    try:
        admite_minim_unic(a)
    except AssertionError as e:
        print(e)
        print('Forma biliniara nu admite un punct de minim unic.')
    else:
        print('Forma biliniara admite un punct de minim unic.')

        x1 = met_pasului_descendent(a, b, np.array([[0], [0]]))
        x2 = met_gradientilor_conjugati(a, b, np.array([[0], [0]]))
        print(x1)
        print(x2)

        curbe_nivel(a, b)


# ----------------------------------------------- EXERCITIUL 2 ---------------------------------------------------------


def f2(x):
    """ Functia data la exercitiul 2.

    :param x: parametrul x
    :return: rezultatul functiei in punctul x
    """
    return -6 * np.sin(-5 * x) - np.cos(2 * x) + 18.93 * x


def substitutie_ascendenta(a, b):
    """ Calculeaza x astfel incat Ax = b folosind metoda substitutiei ascendente.

    :param a: matricea patratica A inferior triunghiulara
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """

    # Verificarea conditiilor de intrare: A matrice patratica si compatibila cu vectorul b.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    # Initializarea vectorului solutiei numerice.
    n = b.shape[0]
    x = np.zeros(shape=n)

    # Prima componenta a solutiei.
    x[0] = b[0] / a[0, 0]

    # Determinarea solutiei numerice.
    for k in range(1, n):
        s = np.dot(a[k, :k], x[:k])
        x[k] = (b[k] - s) / a[k, k]

    return x


def met_Newton_pol_Lagrange(divs):
    """ Determina functia cu polinomul PN(x) determinat folosind metoda Newton.

    :param divs: lista diviziunilor
    :return: functia ceruta
    """
    n = len(divs)
    a = np.array([[0 if j > i else 1 if i == 0 else np.prod([divs[i] - divs[k] for k in range(0, j)])
                   for j in range(n)] for i in range(n)])
    y = np.array([f2(divs[i]) for i in range(n)])
    c = substitutie_ascendenta(a, y)

    def PN(x):
        return c[0] + np.sum([c[i] * np.prod([x - divs[j] for j in range(i)]) for i in range(1, len(c))])

    return PN


def ex2():
    """ Sa se aproximeze functia cu polinomul Lagrange PN(x) determinat folosind metoda Newton.
        1. Sa se reprezinte grafic functia exacta, nodurile de interpolare alese si aproximarea numerica obtinuta. Se
        va alege cel mai mic N astfel incat eroarea maxima de trunchiere sa satisfaca relatia ||e_{t}||_{inf} <= 1e-5.
        2. Sa se reprezinte intr-o figura noua eroare de trunchiere.

    :return: None
    """
    a = -np.pi
    b = np.pi
    et = 1e-5

    N = find_smallest_N(a, b, et, f2, met_Newton_pol_Lagrange)
    divs = np.linspace(a, b, N)
    PN = met_Newton_pol_Lagrange(divs)

    # 1
    show_function(divs, f2, PN)

    # 2
    show_error(divs, f2, PN)


# ----------------------------------------------- EXERCITIUL 3 ---------------------------------------------------------


def f3(x):
    """ Functia data la exercitiul 3.

    :param x: parametrul x
    :return: rezultatul functiei in punctul x
    """
    return -3 * np.sin(-2 * x) - 7 * np.cos(5 * x) - 0.5 * x


def f3_der(x):
    """ Derivata functiei f3.

    :param x: parametrul x
    :return: rezultatul derivatei in punctul x
    """
    return 6 * np.cos(-2 * x) + 35 * np.sin(5 * x) - 0.5


def substitutie_descendenta(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda substitutiei descendente.

    :param a: matricea patratica A superior triunghiulara
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """

    # Verificarea conditiilor de intrare: A matrice patratica si compatibila cu vectorul b.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    # Initializarea vectorului solutiei numerice.
    n = b.shape[0] - 1
    x = np.zeros(shape=n+1)

    # Ultima componenta a solutiei.
    x[n] = b[n] / a[n, n]

    # Determinarea solutiei numerice.
    for k in range(n - 1, -1, -1):
        s = np.dot(a[k, k + 1:], x[k + 1:])
        x[k] = (b[k] - s) / a[k, k]

    return x


def gauss_pivotare_totala(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda Gauss cu pivotare totala.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """

    # Verificarea conditiilor de intrare: A matrice patratica si compatibila cu vectorul b, sistem compatibil.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    assert np.linalg.det(a) != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat!'

    # Constructia matricei extinse (A|b).
    a_ext = np.concatenate((a, b[:, None]), axis=1)

    # Setarea datelor initiale.
    n = a.shape[0] - 1
    index = np.array(range(n + 1))

    # Determinarea solutiei numerice.
    for k in range(n):

        # Determinarea pozitiei pivotului.
        poz = np.argmax(np.abs(a_ext[k:, k:n]))
        p = k + int(poz / (n - k))
        m = k + poz - ((p - k) * (n - k))

        # Verificare suplimentara a sistemului.
        if a_ext[p, m] == 0:
            raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')

        # Pozitionarea pivotului pe prima linie.
        if p != k:
            a_ext[[p, k], :] = a_ext[[k, p], :]

        # Pozitionarea pivotului pe prima coloana.
        if m != k:
            a_ext[:, [m, k]] = a_ext[:, [k, m]]
            index[[m, k]] = index[[k, m]]

        # Eliminarea valorilor de pe fiecare linie de sub pivot, aceeasi coloana.
        for j in range(k + 1, n + 1):
            mjk = a_ext[j, k] / a_ext[k, k]
            a_ext[j, :] -= mjk * a_ext[k, :]

    # Verificare suplimentara a sistemului.
    if a_ext[n, n] == 0:
        raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')

    # Gasirea solutiei folosind metoda substitutiei descendente.
    y = substitutie_descendenta(a_ext[:, :-1], a_ext[:, -1])

    # Repozitionarea necunoscutelor
    x = list(range(n + 1))
    for i in range(n + 1):
        x[index[i]] = y[i]

    return np.array(x)


def f_spline_cubice(divs):
    """ Pentru un set de diviziuni dat, determina functia spline cubica

    :param divs: set de diviziuni
    :return: functie care evalueaza polinomul intr-un punct x
    """
    n = len(divs) - 1
    mat = [[1. if (i == j and (j == 0 or j == n)) or (j == i - 1 and i != n) or (j == i + 1 and i != 0)
            else 4. if i == j else 0. for j in range(n + 1)] for i in range(n + 1)]

    h = divs[1] - divs[0]
    y = [f3_der(divs[0]) if i == 0 else f3_der(divs[i]) if i == n
         else 3 / h * (f3(divs[i + 1]) - f3(divs[i - 1])) for i in range(n + 1)]

    b = gauss_pivotare_totala(np.array(mat), np.array(y))

    a = [f3(divs[i]) for i in range(n)]
    c = [3 / (h ** 2) * (f3(divs[i + 1]) - f3(divs[i])) - (b[i + 1] + 2 * b[i]) / h for i in range(n)]
    d = [-2 / (h ** 3) * (f3(divs[i + 1]) - f3(divs[i])) + (1 / (h ** 2) * (b[i + 1] + b[i])) for i in range(n)]

    def eval_s(x):
        return [a[i] + b[i] * (x - divs[i]) + c[i] * ((x - divs[i]) ** 2) + d[i] * ((x - divs[i]) ** 3)
                for i in range(n) if divs[i] <= x <= divs[i + 1]][0]

    return eval_s


def ex3():
    """ Sa se aproximeze functia folosind interpolarea cu functii spline cubice.
        1. Sa se reprezinte grafic functia exacta, nodurile de interpolare alese si aproximarea numerica obtinuta.
        Numarul de subintervale in care se va imparti domeniul, N, se va alege cel mai mic posibil astfel incat eroarea
        maxima de trunchiere sa satisfaca relatia ||e_{t}||_{inf} <= 1e-5.
        2. Sa se reprezinte intr-o figura noua eroarea de trunchiere.

    :return: None
    """
    a = -np.pi
    b = np.pi
    et = 1e-5

    N = find_smallest_N(a, b, et, f3, f_spline_cubice)
    divs = np.linspace(a, b, N)
    fsc = f_spline_cubice(divs)

    # 1
    show_function(divs, f3, fsc)

    # 2
    show_error(divs, f3, fsc)


# -------------------------------------------------- MAIN --------------------------------------------------------------


def main():
    # ex1()
    ex2()
    # ex3()


if __name__ == '__main__':
    main()
