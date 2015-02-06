__author__ = 'zieghailo'

import numpy as np
from scipy.spatial import KDTree

from point import Point

class SoIGraph():

    def __init__(self, points):
        self.points = points
        data = [tuple(p.p) for p in points]
        self.kdtree = KDTree(data)

    @staticmethod
    def randomize(n, maxx, maxy):
        points = [Point(np.random.rand(2) * [maxx, maxy]) for r in range(n)]
        points.append(Point(np.array([0, 0])))
        points.append(Point(np.array([maxx, maxy])))
        return SoIGraph(points)

    def add_point(self, x, y):
        self.points.append(Point(np.array([x, y])))

    def find_closest_distance_index(self, pindex, SCALING=2):
        point = self.points[pindex]

        d = 10
        solution = None

        while solution is None:
            result = self.kdtree.query_ball_point(point.p, d)
            result.remove(pindex)
            if len(result) == 0:
                d *= SCALING
                continue

            closeness = filter(lambda x: distance(point, self.points[x]), result)
            return np.min(closeness)

    def find_closest_distance(self, pindex, SCALING=2):
        pend = self.find_closest_distance_index(pindex, SCALING)
        a = self.points[pindex]
        b = self.points[pend]
        return distance(a, b)


    def build_graph(self):
        radii = np.zeros(len(self.points))
        for i, p in enumerate(self.points):
            radii[i] = self.find_closest_distance(i)

        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                a = self.points[i]
                b = self.points[j]
                dist = distance(a, b)
                if dist < radii[i] + radii[j]:
                    a.connections.append(b)
                    b.connections.append(a)


def distance(a, b):
    return np.sqrt(np.sum((a.p-b.p) ** 2))