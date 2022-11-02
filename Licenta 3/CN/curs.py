import matplotlib.pyplot as plt
import numpy as np
import math
import random


# ------------------------------------------------------- CURS 1 -------------------------------------------------------

def metoda_bisectiei(f, a, b, epsilon):
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'

    # setez datele initiale
    n = math.floor(np.log2((b - a) / epsilon))
    x = (a + b) / 2

    for i in range(1, n):
        # aplic un pas al metodei valorilor intermediare
        if f(x) == 0:
            break
        elif f(a) * f(x) < 0:
            b = x
        else:
            a = x
        x = (a + b) / 2

    return x, n


def metoda_Newton_Raphson(f, df, ddf, a, b, epsilon, x0):
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df(a)) * np.sign(df(b)) > 0, 'Exista c astfel incat f\'(c) = 0'
    assert np.sign(ddf(a)) * np.sign(ddf(b)) > 0, 'Exista c astfel incat f"(c) = 0'
    assert np.sign(f(x0)) * np.sign(ddf(x0)) > 0, 'f(x0) * f"(x0) <= 0'

    # setez datele initiale
    x_old = x0
    n = 0

    while True:
        # aplic metoda
        x_new = x_old - f(x_old) / df(x_old)

        # verific conditia de iesire
        if np.abs(x_new - x_old) / np.abs(x_old) < epsilon:
            break

        # trec la pasul urmator
        x_old = x_new
        n += 1

    return x_new, n


# ------------------------------------------------------- CURS 2 -------------------------------------------------------

def metoda_secantei(f, df, a, b, x0, x1, eps):
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df(a)) * np.sign(df(b)) > 0, 'f\' se anuleaza pe [a, b]'

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


def metoda_pozitiei_false(f, df, ddf, a, b, eps):
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df(a)) * np.sign(df(b)) > 0, 'f\' se anuleaza pe [a, b]'
    assert np.sign(ddf(a)) * np.sign(ddf(b)) > 0, 'f" se anuleaza pe [a, b]'

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


# ------------------------------------------------------- CURS 3 -------------------------------------------------------

def metoda_substitutiei_descendente(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda substitutiei descendente.

    :param a: matricea patratica A superior triunghiulara
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    assert all([a[i][j] == 0 for i in range(a.shape[0]) for j in range(i)]), \
        'Matricea introdusa nu este superior triunghiulara!'

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


def metoda_Gauss_fara_pivotare(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda Gauss fara pivotare.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    assert np.linalg.det(a) != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat!'

    # Constructia matricei extinse (A|b)
    a_ext = np.concatenate((a, b[:, None]), axis=1)

    # Setarea datelor initiale
    n = a.shape[0] - 1

    for k in range(n):
        assert a_ext[k:, k].any(), 'Sistem incompatibil sau sistem compatibil nedeterminat'

        # Aflam pozitia pivotului de pe colona k
        p = np.argmin(a_ext[k:, k] == 0)  # Pozitia primului element nenul
        p += k

        # Schimba linia 'k' cu 'p' daca pivotul nu se afla pe diagonala principala
        if k != p:
            a_ext[[p, k], :] = a_ext[[k, p], :]

        # Zero pe coloana sub pozitia pivotului
        for j in range(k + 1, n + 1):
            m = a_ext[j, k] / a_ext[k, k]
            a_ext[j, :] -= m * a_ext[k, :]

    assert a_ext[n, n] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat'

    # Gaseste solutia folosind metoda substitutiei descendente
    x_num = metoda_substitutiei_descendente(a_ext[:, :-1], a_ext[:, -1])

    return x_num


def metoda_Gauss_cu_pivotare_partiala(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda Gauss fara pivotare.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    assert np.linalg.det(a) != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat!'

    # Constructia matricei extinse (A|b)
    a_ext = np.concatenate((a, b[:, None]), axis=1)

    # Setarea datelor initiale
    n = a.shape[0] - 1

    for k in range(n):
        assert a_ext[k:, k].any(), 'Sistem incompatibil sau sistem compatibil nedeterminat'

        # Aflam pozitia pivotului de pe colona k
        p = np.argmax(np.abs(a_ext[k:, k]))  # Pozitia primului element nenul
        p += k

        # Schimba linia 'k' cu 'p' daca pivotul nu se afla pe diagonala principala
        if k != p:
            a_ext[[p, k], :] = a_ext[[k, p], :]

        # Zero pe coloana sub pozitia pivotului
        for j in range(k + 1, n + 1):
            m = a_ext[j, k] / a_ext[k, k]
            a_ext[j, :] -= m * a_ext[k, :]

    assert a_ext[n, n] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat'

    # Gaseste solutia folosind metoda substitutiei descendente
    x_num = metoda_substitutiei_descendente(a_ext[:, :-1], a_ext[:, -1])

    return x_num


def metoda_Gauss_cu_pivotare_totala(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda Gauss cu pivotare totala.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """
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
        assert a_ext[p, m] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat.'

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
    assert a_ext[n, n] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat.'

    # Gasirea solutiei folosind metoda substitutiei descendente.
    y = metoda_substitutiei_descendente(a_ext[:, :-1], a_ext[:, -1])

    # Repozitionarea necunoscutelor
    x = list(range(n + 1))
    for i in range(n + 1):
        x[index[i]] = y[i]

    return np.array(x)


def metoda_substitutiei_ascendente(a, b):
    """ Calculeaza x astfel incat Ax = B folosind metoda substitutiei ascendente.

    :param a: matricea patratica A inferior triunghiulara
    :param b: vectorul solutiei b
    :return: vectorul cautat x
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'
    assert all([a[i][j] == 0 for i in range(a.shape[0]) for j in range(i + 1, a.shape[1])]), \
        'Matricea introdusa nu este inferior triunghiulara!'

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


def inversa_unei_matrice(a):
    """ Calculeaza inversa matricei A folosind metoda Gauss cu pivotare totala.

    :param a: matricea patratica A
    :return: inversa matricei A
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert np.linalg.det(a) != 0, 'Matricea introdusa nu este inversabila!'

    # Initializeaza o matrice pentru stocarea solutiei.
    inversa = np.zeros_like(a)

    # Initializeaza matricea din dreapta egalului ca matricea identitate.
    n = a.shape[0]
    ident = np.eye(n)

    # Afla fiecare coloana din inversa folosind metoda de eliminare Gauss cu pivotare totala.
    for i in range(n):
        inversa[:, i] = metoda_Gauss_cu_pivotare_totala(a, ident[:, i])

    return inversa


# ------------------------------------------------------- CURS 4 -------------------------------------------------------

def rangul_unei_matrice(a, tol):
    """ Calculeaza rangul matricei A folosind metoda Gauss cu pivotare partiala.

    :param a: matricea nenula A
    :param tol:
    :return: inversa matricei A
    """
    assert a.any(), 'Matricea introdusa este nula!'

    # Setarea datelor initiale.
    m = a.shape[0]
    n = a.shape[1]
    h = 0
    k = 0
    rang = 0

    while h < m and k < n:
        p = np.argmax(np.abs(a[h:, k]))
        p += k

        if a[p, k] <= tol:
            k += 1
            continue

        if p != h:
            a[[p, h], :] = a[[h, p], :]

        for j in range(h + 1, m):
            mjk = a[j, k] / a[h, k]
            a[j, :] -= mjk * a[h, :]

        h += 1
        k += 1
        rang += 1

    return rang + 1


def factorizarea_LU_cu_Gauss_cu_pivotare_partiala(a, b):
    """ Calculeaza L inferior triunghiulara si U superior triunghiulara astfel incat L * U = A.

    :param a: matricea patratica A
    :param b: vectorul solutiei b
    :return: matricele L si U cautate, vectorul b renumerotat conform schimbarilor de linii
    """
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
        assert a[p, k] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat.'

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
    assert a[n, n] != 0, 'Sistem incompatibil sau sistem compatibil nedeterminat.'

    # Repozitionarea necunoscutelor.
    b = np.array(b[w])

    # Gasirea solutiei pentru L * y = b
    y = metoda_substitutiei_ascendente(L, b)

    # Gasirea solutiei pentru U * x = y
    x = metoda_substitutiei_descendente(a, y)
    return x


# ------------------------------------------------------- CURS 5 -------------------------------------------------------

def factorizare_Cholesky(a):
    """ Calculeaza L inferior triunghiulara astfel incat L * L^{T} = A folosind factorizarea Cholesky.

    :param a: matricea patratica, simetrica si pozitiv definita A
    :return: matricea L cautata
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert np.size([1 for i in range(a.shape[0]) for j in range(i) if a[i, j] != a[j, i]]) == 0, \
        'Matricea introdusa nu este simetrica!'
    assert np.size([1 for i in range(a.shape[0]) if np.linalg.det(a[:i, :i]) == 0]) == 0, \
        'Matricea introdusa nu este pozitiv definita!'

    # Setarea datelor initiale.
    n = a.shape[0] - 1
    L = np.zeros((n + 1, n + 1))
    alpha = a[0, 0]

    # Verificare suplimentara a sistemului.
    assert alpha > 0, 'Matricea nu este pozitiv definita.'

    # Initializarea primei coloane a matricei L.
    L[0, 0] = np.sqrt(alpha)
    for i in range(1, n + 1):
        L[i, 0] = a[i, 0] / L[0, 0]

    # Determinarea solutiei numerice.
    for k in range(1, n + 1):
        alpha = a[k, k] - sum(L[k, s] ** 2 for s in range(k))

        # Verificare suplimentara a sistemului.
        assert alpha > 0, 'Matricea nu este pozitiv definita.'

        # Initializarea coloanei k a matricei L.
        L[k, k] = np.sqrt(alpha)
        for i in range(k + 1, n + 1):
            L[i, k] = (a[i, k] - sum(L[i, s] * L[k, s] for s in range(k))) / L[k, k]

    return L


# ------------------------------------------------------- CURS 6 -------------------------------------------------------

# TODO:
# Minimizarea functiilor de doua variabile
# Tema3: curbe_nivel, met_gradientilor_conjugati

def metoda_pasului_descendent(a, b, x):
    """ Afla punctul de minim al functiei biliniare definite de matricea A si vectorul b folosind metoda pasului
    descendent.

    :param a: matricea A
    :param b: vectorul b
    :param x: punctul initial [x0, y0]
    :return: punctul de minim al functiei f1
    """
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert a.shape[0] == b.shape[0], 'Matricea introdusa si vectorul b nu se potrivesc!'

    h = b - a @ x
    while np.linalg.norm(h, ord=2) > 1e-10:
        alpha = (np.transpose(h) @ h) / (np.transpose(h) @ a @ h)
        x = x + alpha * h
        h = b - a @ x

    return x


# ------------------------------------------------------- CURS 7 -------------------------------------------------------

def modul(a):
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    return np.sqrt(sum([a[i][j] ** 2 for i in range(a.shape[0]) for j in range(a.shape[0]) if i != j]))


def metoda_Jacobi_de_aproximare_a_valorilor_proprii(a, epsilon):
    assert a.shape[0] == a.shape[1], 'Matricea introdusa nu este patratica!'
    assert np.size([1 for i in range(a.shape[0]) for j in range(i) if a[i, j] != a[j, i]]) == 0, \
        'Matricea introdusa nu este simetrica!'

    n = a.shape[0]
    while modul(a) >= epsilon:
        maxx = a[0, 1]
        p = 0
        q = 1

        for i in range(n):
            for j in range(i + 1, n):
                if np.abs(a[i, j]) > maxx:
                    maxx = np.abs(a[i, j])
                    p = i
                    q = j

        if a[p, p] == a[q, q]:
            theta = np.pi / 4
        else:
            theta = (1 / 2) * np.arctan(2 * a[p, q] / (a[q, q] - a[p, p]))

        c = np.cos(theta)
        s = np.sin(theta)

        for j in range(n):
            if j != p and j != q:
                u = a[p, j] * c - a[q, j] * s
                v = a[p, j] * s + a[q, j] * c
                a[p, j] = a[j, p] = u
                a[q, j] = a[j, q] = v

        u = (c ** 2) * a[p, p] - 2 * c * s * a[p, q] + (s ** 2) * a[q, q]
        v = (s ** 2) * a[p, p] + 2 * c * s * a[p, q] + (c ** 2) * a[q, q]
        a[p, p] = u
        a[q, q] = v
        a[p, q] = a[q, p] = 0

    lam = [a[i][i] for i in range(n)]
    return lam


# ------------------------------------------------------- CURS 8 -------------------------------------------------------

def metoda_directa_de_determinare_a_polinomului_Lagrange(f, X):
    """ Determina functia cu polinomul PN(x) determinat folosind metoda directa.

    :param f: functia f data
    :param X: lista diviziunilor
    :return: polinomul Lagrange
    """
    n = len(X)
    a = np.array([[X[i] ** j for j in range(n)] for i in range(n)])
    y = np.array([f(X[i]) for i in range(n)])
    sol = metoda_Gauss_cu_pivotare_totala(a, y)

    def PN(x):
        return sum([sol[i] * (x ** i) for i in range(n)])

    return PN


def metoda_Lagrange_de_determinare_a_polinomului_Lagrange(f, X):
    """ Determina functia cu polinomul PN(x) determinat folosind metoda Lagrange.

    :param f: functia f data
    :param X: lista diviziunilor
    :return: polinomul Lagrange
    """
    n = len(X)
    y = np.array([f(X[i]) for i in range(n)])

    def L(k, x):
        return np.prod([(x - X[j]) / (X[k] - X[j]) for j in range(n) if j != k])

    def PN(x):
        return sum([L(k, x) * y[k] for k in range(n)])

    return PN


def metoda_Newton_de_determinare_a_polinomului_Lagrange(f, X):
    """ Determina functia cu polinomul PN(x) determinat folosind metoda Newton.

    :param f: functia f data
    :param X: lista diviziunilor
    :return: polinomul Lagrange
    """
    n = len(X)
    a = np.array([[0 if j > i else 1 if i == 0 else np.prod([X[i] - X[k] for k in range(0, j)])
                   for j in range(n)] for i in range(n)])
    y = np.array([f(X[i]) for i in range(n)])
    c = metoda_substitutiei_ascendente(a, y)

    def PN(x):
        return c[0] + np.sum([c[i] * np.prod([x - X[j] for j in range(i)]) for i in range(1, len(c))])

    return PN


def metoda_Newton_cu_diferente_divizate_de_determinare_a_polinomului_Lagrange(f, X):
    """ Determina functia cu polinomul PN(x) determinat folosind metoda Newton cu diferente divizate.

    :param f: functia f data
    :param X: lista diviziunilor
    :return: polinomul Lagrange
    """
    n = len(X)
    q = np.zeros((n, n))

    for i in range(n):
        q[i, 0] = f(X[i])

    for i in range(1, n):
        for j in range(1, i + 1):
            q[i, j] = (q[i, j - 1] - q[i - 1, j - 1]) / (X[i] - X[i - j + 1])

    def PN(x):
        return q[0, 0] + np.sum([q[k, k] * np.prod([x - X[h] for h in range(k - 1)]) for k in range(1, n)])

    return PN


# ------------------------------------------------------- CURS 10 ------------------------------------------------------

def interpolare_cu_functii_spline_liniare(f, X):
    n = len(X)
    Y = np.array([f(X[i]) for i in range(n)])
    a = np.zeros(n)
    b = np.zeros(n)

    for j in range(n):
        a[j] = Y[j]
        b[j] = (Y[j + 1] - Y[j]) / (X[j + 1] - X[j])

    def eval_s(x):
        for i in range(n):
            if X[i] <= x <= X[i + 1]:
                return a[i] + b[i] * (x - X[i])

    return eval_s


# TODO:
def interpolare_cu_functii_spline_patratice(f, X):
    return None


# ------------------------------------------------------- CURS 11 ------------------------------------------------------

def interpolare_cu_functii_spline_cubice(f, df, X):
    n = len(X) - 1
    mat = [[1. if (i == j and (j == 0 or j == n)) or (j == i - 1 and i != n) or (j == i + 1 and i != 0)
            else 4. if i == j else 0. for j in range(n + 1)] for i in range(n + 1)]

    h = X[1] - X[0]
    y = [df(X[0]) if i == 0 else df(X[i]) if i == n
         else 3 / h * (f(X[i + 1]) - f(X[i - 1])) for i in range(n + 1)]

    b = metoda_Gauss_cu_pivotare_totala(np.array(mat), np.array(y))

    a = [f(X[i]) for i in range(n)]
    c = [3 / (h ** 2) * (f(X[i + 1]) - f(X[i])) - (b[i + 1] + 2 * b[i]) / h for i in range(n)]
    d = [-2 / (h ** 3) * (f(X[i + 1]) - f(X[i])) + (1 / (h ** 2) * (b[i + 1] + b[i])) for i in range(n)]

    def eval_s(x):
        return [a[i] + b[i] * (x - X[i]) + c[i] * ((x - X[i]) ** 2) + d[i] * ((x - X[i]) ** 3)
                for i in range(n) if X[i] <= x <= X[i + 1]][0]

    return eval_s


# ------------------------------------------------------- CURS 12 ------------------------------------------------------

def metoda_diferentelor_finite_progresive(f, X):
    h = X[1] - X[0]

    def eval_s(i):
        return (f(X[i] + h) - f(X[i])) / h

    return eval_s


def metoda_diferentelor_finite_regresive(f, X):
    h = X[1] - X[0]

    def eval_s(i):
        return (f(X[i]) - f(X[i] - h)) / h

    return eval_s


def metoda_diferentelor_finite_centrale(f, X):
    h = X[1] - X[0]

    def eval_s(i):
        return (f(X[i] + h) - f(X[i] - h)) / (2 * h)

    return eval_s


def metoda_diferentelor_finite_centrale_pentru_ddf(f, X):
    h = X[1] - X[0]

    def eval_s(i):
        return (f(X[i] + h) - 2 * f(X[i]) + f(X[i] - h)) / (h ** 2)

    return eval_s


# TODO:
# def metoda_de_extrapolare(f, x, h, n):
#     def phi(n, h):
#         return (2 ** (n - 1) * phi(n - 1, h / 2) - phi(n - 1, h)) / (2 ** (n - 1) - 1)
#
#     for i in range(n):
#         q[i, 0] = phi(x, h / (2 ** i - 1))
#
#     for i in range(1, n):
#         for j in range(1, i + 1):
#             q[i, j] = q[i, j - 1] + (q[i, j - 1] - q[i - 1, j - 1]) / (2 ** (j - 1) - 1)
#
#     return q[n, n]


# ------------------------------------------------------- CURS 13 ------------------------------------------------------

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


# ------------------------------------------------------- CURS 14 ------------------------------------------------------


def regresie_liniara():
    return None


def regresie_polinomiala():
    return None


def regresie_exponentiala():
    return None


def DescLRPentaDiag(A, t):
    n = len(t)
    a = [A[i][i] for i in range(n)]
    b = [A[i][i + 1] for i in range(n - 1)]
    c = [A[i + 1][i] for i in range(n - 1)]
    d = [A[i][i + 2] for i in range(n - 2)]
    e = [A[i + 2][i] for i in range(n - 2)]

    print()
    print(a)
    print(b)
    print(c)
    print(d)
    print(e)
    print()

    l = np.zeros(n - 1)
    m = np.zeros(n - 2)
    r = np.zeros(n)
    s = np.zeros(n - 1)
    v = np.zeros(n - 2)

    y = np.zeros(n)
    x = np.zeros(n)

    # PASUL 1
    r[0] = a[0]
    s[0] = b[0]
    l[0] = c[0] / r[0]
    r[1] = a[1] - l[0] * s[0]

    v = [d[i] for i in range(n - 2)]
    m = [e[i] / r[i] for i in range(n - 2)]

    for i in range(n - 2):
        s[i + 1] = b[i + 1] - l[i] * v[i]
    for i in range(n - 2):
        l[i + 1] = (c[i + 1] - m[i] * s[i]) / r[i + 1]

    for i in range(n - 2):
        r[i + 2] = a[i + 2] - l[i + 1] * s[i + 1] - m[i] * v[i]

    # PASUL 2
    y[0] = t[0]
    y[1] = t[1] - l[0] * y[0]
    for i in range(2, n):
        y[i] = t[i] - l[i - 1] * y[i - 1] - m[i - 2] * y[i - 2]

    # PASUL 3
    x[n - 1] = y[n - 1] / r[n - 1]
    x[n - 2] = (y[n - 2] - s[n - 2] * x[n - 1]) / r[n - 2]
    for i in range(n - 3, -1, -1):
        x[i] = (y[i] - s[i] * x[i + 1] - v[i] * x[i + 2]) / r[i]

    # CREEZ MATRICEA L
    L = np.zeros((n, n))
    for i in range(n):
        L[i][i] = 1
    for i in range(n - 1):
        L[i + 1][i] = l[i]
    for i in range(n - 2):
        L[i + 2][i] = m[i]

    # CREEZ MATRICEA R
    R = np.zeros((n, n))
    for i in range(n):
        R[i][i] = r[i]
    for i in range(n - 1):
        R[i][i + 1] = s[i]
    for i in range(n - 2):
        R[i][i + 2] = v[i]

    return L, R, x

# -------------------------------------------------------- TEST --------------------------------------------------------


def main():
    # b
    n = 10
    a = [random.uniform(0, 1) for i in range(n)]
    b = [random.uniform(0, 1) for i in range(n)]
    c = [random.uniform(0, 1) for i in range(n)]
    d = [random.uniform(0, 1) for i in range(n)]
    e = [random.uniform(0, 1) for i in range(n)]
    t = [random.uniform(0, 1) for i in range(n)]

    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = a[i]
    for i in range(n - 1):
        A[i][i + 1] = b[i]
        A[i + 1][i] = c[i]
    for i in range(n - 2):
        A[i][i + 2] = d[i]
        A[i + 2][i] = e[i]

    print("SUBPUNCTUL B")
    print("Matricea A este:")
    print(A)
    print("Matricea t este:")
    print(t)
    print('\n')

    # c
    L, R, x = DescLRPentaDiag(A, t)
    print("SUBPUNCTUL C")
    print("Matricea L este:")
    print(L)
    print("Matricea R este:")
    print(R)
    print('\n')

    # d
    print("SUBPUNCTUL D")
    print("Solutia sistemului este:")
    print(x)

    print("Verificare:")
    # print(A @ x)
