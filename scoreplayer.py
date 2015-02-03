#!/usr/bin/python

# Based on ...

import numpy
import pyaudio

STD_SAMPLE_RATE = 44100


class AudioPlayer(object):

    """docstring for AudioPlayer"""

    def __init__(self):
        super(AudioPlayer, self).__init__()

    def gen_sine_wave(frequency, length, rate=STD_SAMPLE_RATE):
        length = int(length * rate)
        factor = frequency * (numpy.pi * 2) / rate
        return numpy.sin(numpy.arange(length) * factor)

    def gen_note_array(frequency, length, rate=STD_SAMPLE_RATE):
        array = 0*AudioPlayer.gen_sine_wave(frequency, length, rate)
        array += 0.4 * AudioPlayer.gen_sine_wave(2*frequency, length, rate)
        array += 0.2 * AudioPlayer.gen_sine_wave(3*frequency, length, rate)
        array += 0.1 * AudioPlayer.gen_sine_wave(4*frequency, length, rate)
        array += 0.5 * AudioPlayer.gen_sine_wave(5*frequency, length, rate)
        array += 0.25 * AudioPlayer.gen_sine_wave(6*frequency, length, rate)
        array += 0.125 * AudioPlayer.gen_sine_wave(7*frequency, length, rate)
        return array

    def play_from_array(array):
        p = pyaudio.PyAudio()
        stream = p.open(format=pyaudio.paFloat32,
                        channels=1, rate=STD_SAMPLE_RATE, output=1)

        stream.write(array.astype(numpy.float32).tostring())
        stream.close()
        p.terminate()

    def gen_array_from_note(note, length):
        return AudioPlayer.gen_note_array(note.frequency, length)

    def gen_array_from_unit(unit):
        note = unit.notes[0]
        duration = float(unit.duration)
        print(str(unit) + '    ' + str(float(unit.duration)))
        array = AudioPlayer.gen_note_array(
            frequency=note.frequency, length=duration)
        for note in unit.notes[1:]:
            array += AudioPlayer.gen_note_array(
                frequency=note.frequency, length=duration)
        return numpy.array(array)

    def gen_array_from_score(score):
        units_arrays = []
        for line in score.lines:
            for bar in line:
                for unit in bar.units:
                    units_arrays.append(AudioPlayer.gen_array_from_unit(unit))

        return numpy.concatenate(units_arrays)

if __name__ == '__main__':
    import sys

    from score import Score

    if len(sys.argv) == 1:
        s = Score.parse('./test_files/jsbach_inventio1.xml')
    else:
        s = Score.parse(sys.argv[1])

    a = AudioPlayer.gen_array_from_score(s)
    AudioPlayer.play_from_array(a)
