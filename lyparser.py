#!/usr/python

import ly.music
import ly.document
import ly.pitch.rel2abs


class LyParser:

    def parse(filename):
        input_file = open(filename, 'r')
        document = ly.document.Document(input_file.read())
        cursor = ly.document.Cursor(document)
        ly.pitch.rel2abs.rel2abs(cursor)
        parsed = ly.music.document(cursor.document)
        input_file.close()

        return parsed


if __name__ == "__main__":

    parsed = LyParser.parse('tests/auxfiles/ly/inventio1.ly')

    for i in parsed[2][0]:
        if "Note" in str(i):
            print(i.dump() + '\t\t' + str(i.octave_token))
