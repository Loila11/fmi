import numpy as np
import sounddevice as sd


def freq(i):
    return 440 / (1.0595 ** i)


octave = {'Do': freq(9),
          'Re': freq(7),
          'Mi': freq(5),
          'Fa': freq(4),
          'Sol': freq(2),
          'La': freq(0),
          'Si': freq(-2),
          'Do2': freq(-3)}


def add_note(note, frequency):
    octave[note] = frequency


# diez
def make_sharp(note):
    return octave[note] / 1.0595


# bemol
def make_flat(note):
    return octave[note] * 1.0595


def sine(amplitude, frequency, time, phase):
    return amplitude * np.sin(2 * np.pi * frequency * time + phase)


sampling_rate = 44100


def get_tone(frequency, time_of_view):
    amplitude = 10000
    phase = 0

    sampling_period = 1. / sampling_rate  # s
    n_samples = time_of_view / sampling_period
    time = np.linspace(0, time_of_view, int(n_samples + 1))

    return sine(amplitude, frequency, time, phase)


def play_song(tone):
    sd.default.samplerate = sampling_rate
    wav_wave = np.array(tone, dtype=np.int16)
    sd.play(wav_wave, blocking=True)
    sd.stop()


def ex1():
    for note in octave:
        play_song(get_tone(octave[note], 1))


def ex2():
    add_note('SiB', make_flat('Si'))
    add_note('Re2', freq(-5))

    sheet_music = read("FrereJacques.txt")

    tone = np.concatenate([get_tone(octave[note], time_of_view) for (note, time_of_view) in sheet_music])
    play_song(tone)


def read(filename):
    sheet_music = []

    file = open(filename, "r")
    sharp_notes = file.readline().strip().split(' ')
    flat_notes = file.readline().strip().split(' ')

    if sharp_notes[0] != '':
        for note in sharp_notes:
            add_note(note + '#', make_sharp(note))

    for note in flat_notes:
        add_note(note + 'B', make_flat(note))

    for line in file:
        notes = [pair.split(',') for pair in line.strip().split(' ')]
        for note in notes:
            if note[0] in sharp_notes:
                note[0] += '#'

            if note[0] in flat_notes:
                note[0] += 'B'

            sheet_music.append((note[0], float(note[1])))

    return sheet_music


def main():
    # ex1()
    ex2()


if __name__ == '__main__':
    main()
