import re


class Note(object):
    """
    pitch is one integer, where:
        1 <-> A1
        2 <-> A#1
        3 <-> B1
    """

    base_black_keys = [2, 5, 7, 10, 12]
    base_notes = dict([('a', 1), ('a#', 2), ('b', 3), ('c', 4), ('c#', 5),
                       ('d', 6), ('d#', 7), ('e', 8), ('f', 9), ('f#', 10),
                       ('g', 11), ('g#', 12)])
    number_of_base_notes = len(base_notes)

    def __init__(self, note, hold=False):
        super(Note, self).__init__()
        if (isinstance(note, str)):
            self.pitch = Note.get_pitch(note)
            self.note = note
            self.hold = hold
        else:
            raise TypeError

    def __str__(self):
        if self.hold:
            return '(p) self.note'
        else:
            return '(h) self.note'

    def is_a_black_key(self):
        return (self.pitch % Note.number_of_base_notes) in Note.base_black_keys

    def distance(this_note, that_note):
        return abs(this_note.pitch - that_note.pitch)

    def get_pitch(str_note):
        try:
            str_note = str_note.lower()

            note_regex = r'([a-gA-G])(#{1,2}|b{1,2})?(\d+)'
            match = re.match(note_regex, str_note)

            str_pitch = match.group(1).lower()
            modiffs = match.group(2)
            position = int(match.group(3))

            pitch = 0
            pitch += (position - 1)*Note.number_of_base_notes
            pitch += Note.base_notes[str_pitch]
            if modiffs:
                pitch += modiffs.count('#')
                pitch -= modiffs.count('b')

            return pitch

        except Exception as e:
            raise e

    def key_pitch(note):
        return note.pitch
