__author__ = 'zieghailo'

import matplotlib.pyplot as plt

plt.ion()

def plot_graph(graph):
    plt.figure(1)

    x = [p.x for p in graph.points]
    y = [p.y for p in graph.points]

    plt.plot(x, y, 'r*')
    plt.show()


def plot_arrows(graph):
    plt.figure(1)
    ax = plt.axes()
    for p in graph.points:
        x = p.x
        y = p.y

        for c in p.connections:
            cx = c.x
            cy = c.y
            ax.arrow(x, y, cx-x, cy-y)

    plt.show()



