import numpy as np
import random
import matplotlib.pyplot as plt


# ---------------------------------------------------- EXERCITIUL 1 ----------------------------------------------------

def DescLRPentaDiag(A, t):
    n = len(t)
    a = [A[i][i] for i in range(n)]
    b = [A[i][i + 1] for i in range(n - 1)]
    c = [A[i + 1][i] for i in range(n - 1)]
    d = [A[i][i + 2] for i in range(n - 2)]
    e = [A[i + 2][i] for i in range(n - 2)]

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


def ex1():
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
    L, R, sol = DescLRPentaDiag(A, t)
    print("SUBPUNCTUL C")
    print("Matricea L este:")
    print(L)
    print("Matricea R este:")
    print(R)
    print('\n')

    # d
    print("SUBPUNCTUL D")
    print("Solutia sistemului este:")
    print(sol)

    print("Verificare:")
    # print(A @ x)


# ---------------------------------------------------- EXERCITIUL 2 ----------------------------------------------------


def grafic(f, g_min, g_max, res_x, res_y):
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


def newton_raphson(f, df, x0, epsilon, a, b):
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    # assert np.sign(df(a)) * np.sign(df(b)) > 0, 'Exista c astfel incat f\'(c) = 0'

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


def ex2():
    def f(x):
        return x ** 3 + 11 * (x ** 2) + 36 * x + 36

    def df(x):
        return 3 * (x ** 2) + 22 * x + 36

    eps = 10e-3

    # metoda newton_raphson  se aplica pe un interval [a, b] astfel incat f(a) * f(b) < 0
    # din prima derivata gasim punctele de inflexiune x1 = (-11 + 2 * sqrt(3)) / 3 si x2 = (-11 - 2 * sqrt(3)) / 3
    # Asadar, metoda trebuie aplicata pe (-inf, x1), (x1, x2), (x2, inf)
    # x0 este ales aleator in aceste intervale

    x1 = (-11 - 2 * np.sqrt(3)) / 3
    x2 = (-11 + 2 * np.sqrt(3)) / 3

    x_aprox1, N1 = newton_raphson(f, df, -10, eps, -1000, x1)
    x_aprox2, N2 = newton_raphson(f, df, -4, eps, x1, x2)
    x_aprox3, N3 = newton_raphson(f, df, 10, eps, x2, 1000)

    # construiesc vectorii cu solutiile
    res_x = [x_aprox1, x_aprox2, x_aprox3]
    res_y = [f(x_aprox1), f(x_aprox2), f(x_aprox3)]
    grafic(f, -7, 0, res_x, res_y)


# -------------------------------------------------- MAIN --------------------------------------------------------------

def main():
    # EXERCITIUL 1
    # ex1()

    # EXERCITIUL 2
    ex2()


if __name__ == '__main__':
    main()
