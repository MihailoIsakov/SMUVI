__author__ = 'zieghailo'

import numpy as np

class Point():

    def __init__(self, val):
        self.connections = []
        self._p = val
        self.price = 99999999999.0

    @property
    def tuple(self):
        return tuple(self._p)

    @property
    def p(self):
        return self._p

    @property
    def x(self):
        return self._p[0]

    @property
    def y(self):
        return self._p[1]

    def clear_connections(self):
        self.connections = []