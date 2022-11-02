# python --version: 3.8.6
import numpy as np


# ---------------------------------------------- FUNCTII COMUNE --------------------------------------------------------


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


def substitutie_ascendenta(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda substitutiei ascendente.

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


# ----------------------------------------------- EXERCITIUL 1 ---------------------------------------------------------


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


def ex1():
    """ Sa se verifice daca sistemul admite solutie unica si in caz afirmativ sa se determine solutia folosind metoda
    Gauss cu pivotare totala.

    :return: None
    """
    print('\nExercitiul 1:')

    a = np.array([
        [0.,  -2.,  3.,  1.],
        [4.,   0.,  1.,  2.],
        [-5.,  0.,  7.,  8.],
        [-3., -9., -5., -8.]
    ])

    b = np.array([9., 15., 48., -68.])

    # Verificarea si rezolvarea sistemului.
    try:
        x = gauss_pivotare_totala(a, b)
    except AssertionError as e:
        print(e)
        print('Sistemul nu admite solutie unica.')
    else:
        print('Sistemul admite solutie unica:')
        print(x)

        print('\nA * x:')
        print(np.matmul(a, x))


# ----------------------------------------------- EXERCITIUL 2 ---------------------------------------------------------


def calculeaza_inversa(a):
    """ Calculeaza inversa matricei A folosind metoda Gauss pentru determinarea inversei.

    :param a: matricea patratica A
    :return: inversa matricei A
    """

    # Verificarea conditiilor de intrare: A matrice patratica si inversabila.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert np.linalg.det(a) != 0, 'Matricea introdusa nu este inversabila!'

    # Initializeaza o matrice pentru stocarea solutiei.
    inversa = np.zeros_like(a)

    # Initializeaza matricea din dreapta egalului ca matricea identitate.
    n = a.shape[0]
    ident = np.eye(n)

    # Afla fiecare coloana din inversa folosind metoda de eliminare Gauss cu pivotare totala.
    for i in range(n):
        inversa[:, i] = gauss_pivotare_totala(a, ident[:, i])

    return inversa


def ex2():
    """ Verificati daca matricea B este inversabila si in caz afirmativ aplicati metoda Gauss pentru determinarea
    inversei.

    :return: None
    """
    print('\nExercitiul 2:')

    b = np.array([
        [0., -9.,  -8.,  9.],
        [8.,  2.,  -6.,  8.],
        [3., -3., -10., -7.],
        [9., -2., -10.,  7.]
    ])

    # Verificarea si rezolvarea problemei.
    try:
        x = calculeaza_inversa(b)
    except AssertionError as e:
        print(e)
    else:
        print('Matricea este inversabila. Inversa ei este:')
        print(x)


# ----------------------------------------------- EXERCITIUL 3 ---------------------------------------------------------


def fact_LU_GPP(a, b):
    """ Calculeaza L inferior triunghiulara si U superior triunghiulara astfel incat L * U = A.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: matricele L si U cautate, vectorul b renumerotat conform schimbarilor de linii
    """

    # Verificarea conditiilor de intrare: A matrice patratica, sistem cu solutie unica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert np.linalg.det(a) != 0, 'Sistemul nu admite solutie unica!'

    # Setarea datelor initiale.
    n = a.shape[0] - 1
    L = np.eye(n + 1)
    w = np.array(range(n + 1))

    # Determinarea solutiei numerice.
    for k in range(n):

        # Determinarea pozitiei pivotului.
        p = k + np.argmax(np.abs(a[k:, k]))

        # Verificare suplimentara a sistemului.
        if a[p, k] == 0:
            raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')

        # Pozitionarea pivotului pe prima linie.
        if p != k:
            a[[p, k], :] = a[[k, p], :]
            w[[p, k]] = w[[k, p]]

            # Interschimbarea subliniilor din L.
            if k > 0:
                L[[k, p], :k] = L[[p, k], :k]

        # Eliminarea valorilor de pe fiecare linie de sub pivot, aceeasi coloana.
        for j in range(k + 1, n + 1):
            L[j, k] = a[j, k] / a[k, k]
            a[j, :] -= L[j, k] * a[k, :]

    # Verificare suplimentara a sistemului.
    if a[n, n] == 0:
        raise AssertionError('Sistem incompatibil sau sistem compatibil nedeterminat.')

    # Repozitionarea necunoscutelor.
    b = np.array(b[w])

    # Gasirea solutiei pentru L * y = b
    y = substitutie_ascendenta(L, b)

    # Gasirea solutiei pentru U * x = y
    x = substitutie_descendenta(a, y)
    return x


def ex3():
    """ Sa se verifice daca sistemul admite solutie unica si in caz afirmativ sa se determine solutia folosind
    factorizarea LU cu pivotare partiala.

    :return: None
    """
    print('\nExercitiul 3:')

    a = np.array([
        [0., -10., -3., -10.],
        [7., 7., -9., 3.],
        [-2., -3., -8., 1.],
        [-1., -8., -5., -2.]
    ])

    b = np.array([-161., 38., -76., -104.])

    # Verificarea si rezolvarea problemei.
    try:
        x = fact_LU_GPP(a, b)
    except AssertionError as e:
        print(e)
    else:
        print('Sistemul admite solutie unica:')
        print(x)

        print('\nA * x:')
        print(np.matmul(a, fact_LU_GPP(a, b)))


# ----------------------------------------------- EXERCITIUL 4 ---------------------------------------------------------


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
    :return: True daca matricea e simetrica, False altfel
    """

    # Verificarea conditiilor de intrare: A matrice patratica.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'

    # Verificarea minorilor principali (criteriul lui Sylvester).
    return np.size([1 for i in range(a.shape[0]) if np.linalg.det(a[:i, :i]) == 0]) == 0


def factorizare_Cholesky(a):
    """ Calculeaza L inferior triunghiulara astfel incat L * L^{T} = A folosind factorizarea Cholesky.

    :param a: matricea patratica, simetrica si pozitiv definita A
    :return: matricea L cautata
    """

    # Verificarea conditiilor de intrare: A matrice patratica, simetrica si pozitiv definita.
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert simetrica(a), 'Matricea introdusa nu este simetrica!'
    assert pozitiv_definita(a), 'Matricea introdusa nu este pozitiv definita!'

    # Setarea datelor initiale.
    n = a.shape[0] - 1
    L = np.zeros((n + 1, n + 1))
    alpha = a[0, 0]

    # Verificare suplimentara a sistemului.
    if alpha <= 0:
        raise AssertionError('Matricea nu este pozitiv definita.')

    # Initializarea primei coloane a matricei L.
    L[0, 0] = np.sqrt(alpha)
    for i in range(1, n + 1):
        L[i, 0] = a[i, 0] / L[0, 0]

    # Determinarea solutiei numerice.
    for k in range(1, n + 1):
        alpha = a[k, k] - sum(L[k, s] ** 2 for s in range(k))

        # Verificare suplimentara a sistemului.
        if alpha <= 0:
            raise AssertionError('Matricea nu este pozitiv definita.')

        # Initializarea coloanei k a matricei L.
        L[k, k] = np.sqrt(alpha)
        for i in range(k + 1, n + 1):
            L[i, k] = (a[i, k] - sum(L[i, s] * L[k, s] for s in range(k))) / L[k, k]

    return L


def ex4():
    """ Sa se verifice daca matricea C admite factorizare Cholesky si in caz afirmativ sa se determine aceasta.

    :return: None
    """
    print('\nExercitiul 4:')

    c = np.array([
        [25., -35.,  25., -40.],
        [-35., 74., -10.,  81.],
        [25., -10.,  86.,  33.],
        [-40., 81.,  33., 234.]
    ])

    # Verificarea si rezolvarea problemei.
    try:
        x = factorizare_Cholesky(c)
    except AssertionError as e:
        print(e)
        print('Matricea nu admite factorizare Cholesky.')
    else:
        print('Matricea admite factorizare Cholesky.')
        if np.size([1 for i in range(c.shape[0]) if c[i, i] <= 0]) == 0:
            print('Descompunerea sistemului este unica.')

        print('Matricea L este:')
        print(x)

        print('\nL * L transpus:')
        print(np.matmul(x, np.transpose(x)))


# -------------------------------------------------- MAIN --------------------------------------------------------------


def main():
    ex1()
    ex2()
    ex3()
    ex4()


if __name__ == '__main__':
    main()
