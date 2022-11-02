import numpy as np
import matplotlib.pyplot as plt


# functia de intrare
def f(x):
    return np.cos(x) - x


# derivata de ordin I
def df(x):
    return - np.sin(x) - 1


# derivata de ordin II
def ddf(x):
    return - np.cos(x)


def metoda_NR(a, b, epsilon, x0):
    # verific conditiile de intrare
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'
    assert np.sign(df(a)) * np.sign(df(b)) > 0, "Exista c astfel incat f'(c) = 0"
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


def main():
    # a
    a = 0
    b = np.pi / 2

    x = np.linspace(a, b, 100)
    y = f(x)

    plt.plot(x, y)
    plt.plot([0, 0], [-2, 2], 'black', linewidth=0.5)
    plt.plot([-0.5, 2], [0, 0], 'black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')
    # plt.show()

    # b
    # metoda_NR(a, b, epsilon, x0)

    # c
    x0 = 1
    eps = 10 ** (-3)
    x_new, n = metoda_NR(a, b, eps, x0)

    plt.scatter(x_new, f(x_new), color='green')
    plt.show()


if __name__ == '__main__':
    main()
