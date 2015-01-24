#!/usr/bin/python3

import note


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
        self.notes = sorted(notes, key=note.Note.key_pitch)
        self.duration = duration

    def __str__(self):
        out = '%6s' % str(self.duration) + " | "
        for n in self.notes:
            out += '%-8s' % str(n)
        return out