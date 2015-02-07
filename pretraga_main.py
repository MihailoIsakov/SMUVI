#! /usr/bin/env python

__author__ = 'zieghailo'

import plotter

def input_graph():
    global graph
    from sphereofinfluence import SoIGraph
    graph = SoIGraph.randomize(0, 100, 100)

    plotter.start_gui(graph)



if __name__ == "__main__":
    input_graph()