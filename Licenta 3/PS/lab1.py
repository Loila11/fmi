# Zavelca Miruna-Andreea 334

import numpy as np
import matplotlib.pyplot as plt

# ex 1
frequency = 2000


def sampling(frequency):
    return 2 * np.pi / frequency


print('a) ' + str(sampling(frequency)))


def count_bytes(frequency, bits_per_second, time):
    return frequency * bits_per_second * time / 8


print('b) ' + str(count_bytes(frequency, 4, 3600)))

'''
a) 0.0031415926535897933
b) 3600000
'''

# ex 2
'''
f(t) = cos (2 * pi * f * t)
frecventa maxima intre x(t) si y(t) este 100
folosesc frecventa Nyquist pentru a elimina frecventele mai mari
rezultatul va fi 2 * frecventa maxima = 2 * 100 = 200
'''


#ex 3
def cosine(frequency, time, phase=0, amplitude=1):
    return amplitude * np.cos(frequency * time + phase)


time_of_view = 0.03
afs = 2000
fs = 200

n_analog = afs * time_of_view + 1
n_samples = fs * time_of_view + 1

atime = np.linspace(0, time_of_view, int(n_analog))
time = np.linspace(0, time_of_view, int(n_samples))

frequency1 = 520 * np.pi
frequency2 = 280 * np.pi
frequency3 = 120 * np.pi

phase1 = np.pi / 3
phase2 = - np.pi / 3
phase3 = np.pi / 3

x = [cosine(frequency1, t, phase1) for t in atime]
y = [cosine(frequency2, t, phase2) for t in atime]
z = [cosine(frequency3, t, phase3) for t in atime]

x_discret = [cosine(frequency1, t, phase1) for t in time]
y_discret = [cosine(frequency2, t, phase2) for t in time]
z_discret = [cosine(frequency3, t, phase3) for t in time]

fig, axs = plt.subplots(3)
fig.suptitle('Esantionare corecta')
axs[0].plot(atime, x)
axs[0].stem(time, x_discret)
axs[1].plot(atime, y)
axs[1].stem(time, y_discret)
axs[2].plot(atime, z)
axs[2].stem(time, z_discret)

plt.show()

# ex 4
'''
SNR = P semnal / P zgomot
SNR db = 10 log(10) SNR

10 log(10) SNR = P semnal / P zgomot
P zgomot = P semnal / 10 log(10) SNR
P zgomot = 90 / 10 log(10) 80 = 8*10 ^ (-8)
'''
