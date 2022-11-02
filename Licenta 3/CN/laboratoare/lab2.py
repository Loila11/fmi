import numpy as np
import matplotlib.pyplot as plt
import math


# functia de intrare
def f(x):
    return x ** 3 - 7 * x ** 2 + 14 * x - 6


def valori_intermediare(a, b, epsilon):
    # verific conditiile de intrare
    assert a < b, 'Intervalul dat nu este valid'
    assert np.sign(f(a)) * np.sign(f(b)) < 0, 'f(a) si f(b) au acelasi semn'

    # setez datele initiale
    n = math.floor(np.log2((b - a) / epsilon))

    for i in range(1, n):
        # aplic teorema valorilor intermediare
        if f(a) * f((a + b) / 2) < 0:
            b = (a + b) / 2
        else:
            a = (a + b) / 2

    return (a + b) / 2, n


def main():
    # a
    a = 0
    b = 4

    x = np.linspace(a, b, 100)
    y = f(x)

    plt.plot(x, y)
    plt.plot([0, 0], [-7, 3], 'black', linewidth=0.5)
    plt.plot([-0.5, 5], [0, 0], 'black', linewidth=0.5)
    plt.xlabel('x')
    plt.ylabel('y')

    # b
    eps = 10 ** (-5)

    b1, n1 = valori_intermediare(0, 1, eps)
    print('b1: ' + str(b1) + ' ' + str(n1))

    b2, n2 = valori_intermediare(1, 3.2, eps)
    print('b2: ' + str(b2) + ' ' + str(n2))

    b3, n3 = valori_intermediare(3.2, 4, eps)
    print('b3: ' + str(b3) + ' ' + str(n3))

    # c
    x = [b1, b2, b3]
    y = [f(b1), f(b2), f(b3)]

    plt.scatter(x, y, color='yellow')
    plt.show()


if __name__ == '__main__':
    main()
