#!/usr/bin/python3

from numpy import mean, var

from unit import Unit


class Bar(object):
    """A Bar is a list of Units"""
    def __init__(self, key, time_signature, units):
        super(Bar, self).__init__()
        self.units = units
        self.key = key
        self.time_signature = time_signature
        centers = [unit.center for unit in self.units]
        self.units_centers = [c for c in centers if c is not None]
        self.center = mean(self.units_centers)
        self.var = var(self.units_centers)

    def __str__(self):
        out = ''
        out += ' -- ts: ' + str(self.time_signature)
        out += ' -- key: ' + str(self.key)
        out += ' -- center: ' + str(self.center)
        out += ' -- var: ' + str(self.var) + '--\n'
        for u in self.units:
            out += str(u) + '\n'
        return out

    def random_bar():
        key = 'c major'
        time_signature = '4/4'
        n_units = 8
        units = [Unit.random_unit() for _ in range(n_units)]

        return Bar(key, time_signature, units)
