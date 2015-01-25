#!/usr/bin/python3

import unit


class Bar(object):
    """A Bar is a list of Units"""
    def __init__(self, key, time_signature, units):
        super(Bar, self).__init__()
        self.units = units
        self.key = key
        self.time_signature = time_signature

    def __str__(self):
        out = ''
        out += ' - - - - ' + str(self.time_signature)
        out += ' - - - - ' + str(self.key) + ' - - - -\n'
        for u in self.units:
            out += str(u) + '\n'
        return out

    def random_bar():
        key = 'c major'
        time_signature = '4/4'
        n_units = 8
        units = [unit.Unit.random_unit() for _ in range(n_units)]

        return Bar(key, time_signature, units)
