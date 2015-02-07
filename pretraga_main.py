#! /usr/bin/env python

__author__ = 'zieghailo'

from time import sleep
import plotter


def input_graph():
    global graph
    from sphereofinfluence import SoIGraph
    graph = SoIGraph.randomize(0, 100, 100)

    plotter.start_gui(graph)

    plotter.show()
    plotter.plt.ion()
    plotter.plot_graph(graph)
    plotter.plot_arrows(graph)
    plotter.show()
    breadth_first_search(graph)


def depth_first_search(graph):
    visited = set()
    queue = list()

    start = graph.points[0]
    end = graph.points[1]

    queue.append(start)

    while len(queue) > 0:
        print("Queue length", len(queue))
        next_el = queue.pop(0)
        visited.add(next_el)

        if next_el == end:
            return

        for connection in next_el.connections:
            if connection not in visited:
                if connection in queue:
                    queue.remove(connection)
                queue.insert(0, connection)
                plotter.plot_connection(next_el, connection)

        plotter.plot_visited(visited)
        sleep(1)

def breadth_first_search(graph):
    visited = set()
    queue = list()

    start = graph.points[0]
    end = graph.points[1]

    queue.append(start)

    while len(queue) > 0:
        print("Queue length", len(queue))
        next_el = queue.pop(0)
        visited.add(next_el)

        if next_el == end:
            return

        for connection in next_el.connections:
            if connection not in visited and connection not in queue:
                queue.append(connection)
                plotter.plot_connection(next_el, connection)

        plotter.plot_visited(visited)
        sleep(1)

if __name__ == "__main__":
    input_graph()