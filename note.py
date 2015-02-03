import re


class Note(object):

    """
    pitch is one integer, where:
        0 <-> Pause
        1 <-> C1
        2 <-> C#1
        3 <-> D1
    """

    base_notes_list = ['c', 'c#', 'd', 'd#', 'e',
                       'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
    base_notes = dict([('c', 1), ('c#', 2), ('d', 3), ('d#', 4),
                       ('e', 5), ('f', 6), ('f#', 7), ('g', 8),
                       ('g#', 9), ('a', 10), ('a#', 11), ('b', 12)])

    number_of_base_notes = len(base_notes)
    base_black_keys = [2, 4, 7, 9, 11]

    C0frequency = 16.35159783128741

    def __init__(self, note, hold=False):
        super(Note, self).__init__()
        if (isinstance(note, str)):
            self.base_note, self.octave, self.pitch = Note.get_pitch(note)
            self.note = note
            self.hold = hold
        else:
            raise TypeError

    def __str__(self):
        if self.hold:
            return '(h)' + self.note
        else:
            return '(p)' + self.note

    def is_a_black_key(self):
        return (self.pitch % Note.number_of_base_notes) in Note.base_black_keys

    def not_pause(self):
        return (self.pitch != 0)

    def distance(this_note, that_note):
        return abs(this_note.pitch - that_note.pitch)

    def get_pitch(str_note):
        try:
            if str_note == '-':
                return 0

            str_note = str_note.lower()

            note_regex = r'([a-gA-G])(#{1,2}|b{1,2})?(\d+)'
            match = re.match(note_regex, str_note)

            str_pitch = match.group(1).lower()
            modiffs = match.group(2)
            octave = int(match.group(3))

            pitch = 0
            pitch += (octave - 1) * Note.number_of_base_notes
            pitch += Note.base_notes[str_pitch]
            if modiffs:
                pitch += modiffs.count('#')
                pitch -= modiffs.count('b')

            index = (pitch - 1) % 12
            base_note = Note.base_notes_list[index]

            return (base_note, octave, pitch)

        except Exception as e:
            raise e

    def key_pitch(note):
        return note.pitch

    def random_note():
        from random import choice

        pitch = choice(list(Note.base_notes.keys()))
        octave = str(choice(range(1, 9)))

        return Note(pitch + octave)

    def init_notes(list_of_str_notes):
        notes = []
        for str_note in list_of_str_notes:
            notes.append(Note(str_note))

        return notes

    def get_frequency(self):
        n = Note.number_of_base_notes
        note = Note.base_notes[self.base_note] - 1
        base_frequency = Note.C0frequency * 2.0**(note / n)
        frequency = base_frequency * 2.0**self.octave

        return frequency
