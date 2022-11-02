import numpy as np
import matplotlib.pyplot as plt
import csv
from scipy.signal import butter, cheby1, freqz, filtfilt


def RectangularWindow(N):
    return np.ones(N)


def HanningWindow(N):
    return 0.5 * (1 - np.cos(2 * np.pi * np.array(range(N), dtype="float64") / N))


def HammingWindow(N):
    return 0.54 + 0.46 * np.cos(2 * np.pi * np.array(range(N), dtype="float64") / N)


def BlackmanWindow(N):
    return 0.42 - 0.5 * np.cos(2 * np.pi * np.array(range(N), dtype="float64") / N) + \
           0.08 * np.cos(4 * np.pi * np.array(range(N), dtype="float64") / N)


def FlatTopWindow(N):
    return 0.22 - 0.42 * np.cos(2 * np.pi * np.array(range(N), dtype="float64") / N) + \
           0.28 * np.cos(4 * np.pi * np.array(range(N), dtype="float64") / N) - \
           0.08 * np.cos(6 * np.pi * np.array(range(N), dtype="float64") / N) + \
           0.007 * np.cos(8 * np.pi * np.array(range(N), dtype="float64") / N)


def ex1():
    N = 200
    length = 5
    w = [RectangularWindow(N), HanningWindow(N), HammingWindow(N), BlackmanWindow(N), FlatTopWindow(N)]

    fig, axs = plt.subplots(length)
    for i in range(length):
        axs[i].grid(True)
        axs[i].plot(abs(np.fft.fft(w[i])[:N // 2]))

    plt.show()


def readData():
    with open("trafic.csv", newline='', encoding="UTF-8-sig") as f:
        reader = csv.reader(f)
        data = list(reader)
    return list(map(int, np.squeeze(np.asarray(data))))


def A(x):
    plt.grid(True)
    plt.plot(abs(np.fft.fft(x))[:len(x) // 2])
    plt.show()


def C(Wn, N=5, rp=5):
    b0, a0 = butter(N, Wn, btype="low")
    b1, a1 = cheby1(N, rp, Wn, btype="low")
    return b0, a0, b1, a1


def plotD(axs, b, a):
    w, h = freqz(b, a)
    axs.grid(True)
    axs.plot(w, 20 * np.log10(abs(h)))
    return axs


def D(b0, a0, b1, a1):
    fig, axs = plt.subplots(2)
    axs[0] = plotD(axs[0], b0, a0)
    axs[1] = plotD(axs[1], b1, a1)
    plt.show()


def plotE(axs, b, a, x):
    axs.grid(True)
    axs.plot(x)
    axs.plot(filtfilt(b, a, x))
    return axs


def E(b0, a0, b1, a1, x):
    fig, axs = plt.subplots(2)
    axs[0] = plotE(axs[0], b0, a0, x)
    axs[1] = plotE(axs[1], b1, a1, x)
    plt.show()


def ex2():
    x = readData()

    # a
    A(x)

    # b
    Wn = 0.36

    # c
    b0, a0, b1, a1 = C(Wn)

    # d
    D(b0, a0, b1, a1)

    # e
    # Aleg filtrul Butterworth intrucat doar netezeste amplitudinea, in timp ce Chebyshev pierde amplitudine
    E(b0, a0, b1, a1, x)

    # f
    # Pentru filtrul Chebyshev, cu cat N este mai mare cu atat amplitudinea ia valori mai joase pe grafic
    # Tot pentru filtrul Chebyshev, cu cat rp este mai mare cu atat range-ul valorilor este mai mic
    b0, a0, b1, a1 = C(Wn, N=1)
    E(b0, a0, b1, a1, x)

    b0, a0, b1, a1 = C(Wn, N=10)
    E(b0, a0, b1, a1, x)

    b0, a0, b1, a1 = C(Wn, rp=1)
    E(b0, a0, b1, a1, x)

    b0, a0, b1, a1 = C(Wn, rp=10)
    E(b0, a0, b1, a1, x)


def main():
    ex1()
    ex2()


if __name__ == '__main__':
    main()
