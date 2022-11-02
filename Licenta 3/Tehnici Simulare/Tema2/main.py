import numpy
import matplotlib.pyplot as plt


# -------------------------------------------------- EXTRA -------------------------------------------------------------
N = 100
M = 10000


def bern(p):
    """ Folosita in calculul binomialei """
    # P1
    q = 1 - p
    u = numpy.random.uniform(0, 1)

    # P2
    return 0 if u <= q else 1


def histograma(x):
    plt.hist(x, bins=100)
    plt.show()


# ----------------------------------------------- EXPONENTIALA ---------------------------------------------------------
def RespExp(lambd=3):
    # P1:
    n = 0

    while True:
        # P2:
        u0, u1 = numpy.random.uniform(0, 1, 2)

        # P3:
        uStar = u0
        k = 1

        # P4:
        while u0 >= u1:
            # P5:
            k = k + 1
            u0 = u1

            # P6:
            u1 = numpy.random.uniform(0, 1)

        # P7:
        if k % 2 == 1:
            x = n + uStar
            break

        n = n + 1

    return x / lambd


def exponentiala():
    """ Sa se genereze variabila exponentiala Exp(3) folosind cea de-a 3a teorema de respingere (curs 5) """
    lambd = 3
    x = [RespExp(lambd) for i in range(M)]

    print(f'Variabila exponentiala:\n'
          f'Media reala: {1/lambd}\n'
          f'Media calculata: {str(numpy.mean(x))}\n'
          f'Dispersia de selectie reala: {1/(lambd ** 2)}\n'
          f'Dispersia de selectie calculata: {str(numpy.var(x))}\n')

    histograma(x)


# ------------------------------------------------ BINOMIALA 1 ---------------------------------------------------------
def binom1(n, p):
    # P1, P2, P3:
    x = sum(bern(p) for i in range(n))

    return x


def binomiala1():
    """ Sa se genereze variabila binomiala prin doua metode (curs 7) - metoda 1 """
    p = 0.5
    q = 1 - p
    x = [binom1(N, p) for i in range(M)]

    print(f'Variabila binomiala - metoda 1:\n'
          f'Media reala: {N * p}\n'
          f'Media calculata: {str(numpy.mean(x))}\n'
          f'Dispersia de selectie reala: {N * p * q}\n'
          f'Dispersia de selectie calculata: {str(numpy.var(x))}\n')

    histograma(x)


# ------------------------------------------------ BINOMIALA 2 ---------------------------------------------------------
def binom2(n, p):
    # P1:
    w = numpy.random.normal(0, 1)
    q = 1 - p

    # P2:
    x = round(n * p + w * numpy.sqrt(n * p * q))

    return x


def binomiala2():
    """ Sa se genereze variabila binomiala prin doua metode (curs 7) - metoda 2 """
    p = 0.5
    q = 1 - p
    x = [binom2(N, p) for i in range(M)]

    print(f'Variabila binomiala - metoda 2:\n'
          f'Media reala: {N * p}\n'
          f'Media calculata: {str(numpy.mean(x))}\n'
          f'Dispersia de selectie reala: {N * p * q}\n'
          f'Dispersia de selectie calculata: {str(numpy.var(x))}\n')

    histograma(x)


# -------------------------------------------------- MAIN --------------------------------------------------------------
def main():
    exponentiala()
    binomiala1()
    binomiala2()


if __name__ == '__main__':
    main()
