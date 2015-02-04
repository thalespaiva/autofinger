#!/usr/bin/python3

from numpy import mean

from note import Note


class Unit(object):

    """
    A Unit is a list of notes that the player should perform at the same time.
    (<- with one hand)
    Duration must be a Fraction (fractions.Fraction) and it's relatively to the
    bar containing the Unit.
    Note that, by perform we don't mean attack! The notes should be either
    attacked or hold.
    The notes list should be sorted by pitch.
    This is the minimum unit for which one can generate a fingering with
    autofinger.
    """

    def __init__(self, notes, duration):
        super(Unit, self).__init__()
        self.notes = sorted(notes, key=Note.key_pitch)
        self.duration = duration
        self.center = self.calculate_center()

    def __str__(self):
        out = '%6s' % str(self.duration) + " | "
        for n in self.notes:
            out += '%-8s' % str(n)
        return out

    def random_unit():
        from random import randrange
        from fractions import Fraction

        n_notes = randrange(1, 6, 1)
        notes = [Note.random_note() for _ in range(n_notes)]

        return Unit(notes, Fraction(1, 2))

    def calculate_center(self):
        pitches = [note.pitch for note in self.notes if note.not_pause()]

        if len(pitches) == 0:
            return None

        return mean(pitches)
