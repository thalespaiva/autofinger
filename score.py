import xml.etree.ElementTree as ElementTree
from fractions import Fraction

from note import Note
from unit import Unit
from bar import Bar


class Score(object):

    def __init__(self, lines, title='', author=''):
        super(Score, self).__init__()
        self.lines = lines
        self.title = title
        self.author = author

    def __str__(self):
        out = ''
        for line in self.lines:
            for bar in line:
                out += str(bar)
        return out

    def get_units(self):
        units = []

        for line in self.lines:
            for bar in line:
                for unit in bar.units:
                    units.append(unit)
        return units

    def parse(file_path):
        tree = ElementTree.parse(file_path)
        score = tree.getroot()

        lines = []
        for line in score.findall('line'):
            bars = []
            for bar in line.findall('bar'):
                units = []
                time_signature = bar.get('time_signature')
                for unit in bar.findall('unit'):
                    notes = []
                    for note in unit.findall('note'):
                        pitch = note.get('pitch')
                        hold_str = note.get('hold')
                        hold = {'True': True, 'False': False}[hold_str]
                        print(pitch)
                        notes.append(Note(pitch, hold))
                    beats = unit.get('beats')
                    units.append(Unit(notes, Fraction(beats)))
                key = bar.get('key')
                bars.append(Bar(key, time_signature, units))
            lines.append(bars)

        title = score.get('title')
        author = score.get('author')

        return Score(lines, title, author)

    def play(self):
        pass
