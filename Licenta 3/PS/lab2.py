# Zavelca Miruna-Andreea 334

import numpy as np
import matplotlib.pyplot as plt

# ex 1
'''
    frecventa: 40Hz - 200Hz
    frecventa maxima este 200
    folosesc frecventa Nyquist pentru a elimina frecventele mai mari
    rezultatul va fi 2 * frecventa maxima = 2 * 200 = 400
'''

# ex 2
'''
    B = 10Hz
    fc = 90Hz
    
    (2fc - B) / m >= fs >= (2fc + B) / (m + 1)
     <=> (2 * 90 - 10) / m >= fs >= (2 * 90 + 10) / (m + 1)
     <=> 170 / m >= fs >= 190 / (m + 1)
    
    fs >= 2 * B <=> fs >= 2 * 10 <=> fs >= 20
    
    Pentru a gasi frecventa de esantionare optima am desenat
    
    a) m = 1
    170 >= fs >= 190 / 2
     <=> 170 >= fs >= 95
    fs = 95
     
    b) m = 2
    170 / 2 >= fs >= 190 / 3
     <=> 85 >= fs >= 63.3
    fs = 63.3
     
    c) m = 4
    170 / 4 >= fs >= 190 / 5
     <=> 42.5 >= fs >= 38
    fs = 42.5
'''


# ex 3
def cosine(frequency, time, phase=0, amplitude=1):
    return amplitude * np.cos(frequency * time + phase)


def main():
    time_of_view = 1
    fs = 1000
    frequency = 10 * np.pi

    n_samples = fs * time_of_view + 1

    time = np.linspace(0, time_of_view, int(n_samples))
    fft_time = np.linspace(0, fs, fs)

    x = [cosine(frequency, t) for t in time]
    fft_x = cosine(frequency, fft_time)

    fig, axs = plt.subplots(2)

    axs[0].grid(True)
    axs[0].plot(time, x)

    fft = np.fft.fft(fft_x)

    axs[1].grid(True)
    axs[1].plot(fft_time[:500], fft[:500])

    plt.show()


if __name__ == '__main__':
    main()
