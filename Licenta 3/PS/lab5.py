import numpy as np
import matplotlib.pyplot as plt
import csv

""" ex 1:

    fs = 44.1 kHz = 44100 Hz
    d = distanta intre binuri = 1 Hz

    fs / N = d
        => N = fs / d
        => N = 44100 / 1
        => N = 44100 sampleuri
"""


def RectangularWindow(N):
    return [1 for _ in range(N)]


def HanningWindow(N):
    return [0.5 * (1 - np.cos(2 * np.pi * n / N)) for n in range(N)]


def HammingWindow(N):
    return [0.54 + 0.46 * np.cos(2 * np.pi * n / N) for n in range(N)]


def BlackmanWindow(N):
    return [0.42 - 0.5 * np.cos(2 * np.pi * n / N) + 0.08 * np.cos(4 * np.pi * n / N) for n in range(N)]


def FlatTopWindow(N):
    return [0.22 - 0.42 * np.cos(2 * np.pi * n / N) + 0.28 * np.cos(4 * np.pi * n / N) -
            0.08 * np.cos(6 * np.pi * n / N) + 0.007 * np.cos(8 * np.pi * n / N) for n in range(N)]


def cosine(frequency, time, phase=0, amplitude=1):
    return amplitude * np.cos(frequency * np.pi * time + phase)


def applyWindow(x, w, N):
    return [x[n] * w[n] if n < N else 0 for n in range(len(x))]


def makePlots(x, N):
    wR = RectangularWindow(N)
    wH = HanningWindow(N)
    wHm = HammingWindow(N)
    wB = BlackmanWindow(N)
    wFT = FlatTopWindow(N)
    w = [wR, wH, wHm, wB, wFT]

    length = np.shape(w)[0]

    fig, axs = plt.subplots(length)
    for i in range(length):
        axs[i].grid(True)
        axs[i].plot(applyWindow(x, w[i], N))

    plt.show()


def makeRectangularPlots(x1, x2, N):
    wR = RectangularWindow(N)

    fig, axs = plt.subplots(2)

    axs[0].grid(True)
    axs[0].plot(applyWindow(x1, wR, N)[:N//2])

    axs[1].grid(True)
    axs[1].plot(applyWindow(x2, wR, N)[:N//2])

    plt.show()


def ex2():
    # a
    frequency = 100
    N = 200

    time_of_view = 1
    n_samples = N * time_of_view + 1
    time = np.linspace(0, time_of_view, int(n_samples))
    x = [cosine(frequency, t) for t in time]

    makePlots(x, N)

    # b
    f1 = 1000
    f2 = 1100
    fs = 8000
    N = 1000

    time_of_view = 0.01
    n_samples = fs * time_of_view + 1
    time = np.linspace(0, time_of_view, int(n_samples))
    x1 = [cosine(f1, t) for t in time]
    x2 = [cosine(f2, t) for t in time]

    fft_x1 = np.real(np.fft.fft(x1))
    fft_x2 = np.real(np.fft.fft(x2))

    makeRectangularPlots(fft_x1, fft_x2, N)

    # c (Bonus)
    # Toate functiile sunt afisate grafic la punctul a


def ex3():
    # a
    with open("trafic.csv", newline='', encoding="UTF-8-sig") as f:
        reader = csv.reader(f)
        data = list(reader)
    x = list(map(int, np.squeeze(np.asarray(data))))[:72]

    # b
    print(np.convolve(x, np.ones(5), 'valid') / 5)
    print(np.convolve(x, np.ones(9), 'valid') / 9)
    print(np.convolve(x, np.ones(13), 'valid') / 13)
    print(np.convolve(x, np.ones(17), 'valid') / 17)


def main():
    ex2()
    ex3()


if __name__ == '__main__':
    main()
