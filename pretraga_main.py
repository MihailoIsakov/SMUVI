#! /usr/bin/env python

__author__ = 'zieghailo'

from time import sleep
import plotter

from sphereofinfluence import distance


def input_graph():
    global graph
    from sphereofinfluence import SoIGraph
    graph = SoIGraph.randomize(0, 100, 100)

    plotter.start_gui(graph)

    # plotter.show()
    plotter.plt.ion()
    plotter.plot_graph(graph)
    plotter.plot_arrows(graph)
    plotter.show()
    # breadth_first_search(graph)
    # depth_first_search(graph)
    dijkstra(graph)

def depth_first_search(graph, slp=1):
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
        sleep(slp)


def breadth_first_search(graph, slp=1):
    visited = set()
    queue = list()

    start = graph.points[0]
    end = graph.points[1]

    queue.append(start)

    while len(queue) > 0:
        next_el = queue.pop(0)
        visited.add(next_el)

        if next_el == end:
            return

        for connection in next_el.connections:
            if connection not in visited and connection not in queue:
                queue.append(connection)
                plotter.plot_connection(next_el, connection)

        plotter.plot_visited(visited)
        sleep(slp)

def dijkstra(graph, slp=1):
    visited = set()
    queue = list()

    start = graph.points[0]
    start.price = 0
    end = graph.points[1]

    queue.append(start)

    while len(queue) > 0:
        next_el = queue.pop(0)
        visited.add(next_el)

        if next_el == end:
            return

        for connection in next_el.connections:
            if connection not in visited:
                old_price = connection.price
                new_price = next_el.price + distance(next_el, connection)
                connection.price = min(old_price, new_price)

                if connection not in queue:
                    queue.append(connection)
                plotter.plot_connection(next_el, connection)

        queue.sort(key=lambda point: point.price)

        plotter.plot_visited(visited)
        sleep(slp)

if __name__ == "__main__":
    input_graph()