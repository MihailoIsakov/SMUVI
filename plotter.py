__author__ = 'zieghailo'

import matplotlib.pyplot as plt

plt.ion()

def plot_graph(graph):
    plt.figure(1)

    x = [p.x for p in graph.points]
    y = [p.y for p in graph.points]

    plt.plot(x, y, 'r*')
    plt.show()


def plot_arrows(graph, ax):
    # ax = plt.axes()
    for p in graph.points:
        x = p.x
        y = p.y

        for c in p.connections:
            cx = c.x
            cy = c.y
            ax.arrow(x, y, cx-x, cy-y)

    # plt.show()


def start_gui():
    global graph
    from sphereofinfluence import SoIGraph
    graph = SoIGraph.randomize(0, 0, 0)

    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.set_title('click to build line segments')
    line, = ax.plot([0, 100], [0, 100], 'b.')  # empty line
    pointbuilder = PointBuilder(line, ax, graph)
    fig.waitforbuttonpress(0)


class PointBuilder:
    def __init__(self, points, ax, graph):
        self.points = points
        self.ax = ax
        self.graph = graph
        self.cid = points.figure.canvas.mpl_connect('button_press_event', self)

    def __call__(self, event):
        print 'click', event
        if event.inaxes!=self.points.axes: return
        self.graph.add_point(event.xdata, event.ydata)
        x = [p.x for p in self.graph.points]
        y = [p.y for p in self.graph.points]

        self.graph.build_graph()
        plot_arrows(graph, self.ax)

        self.points.set_data(x, y)
        self.points.figure.canvas.draw()

        self.points.figure.waitforbuttonpress(0)




if __name__ == "__main__":
    start_gui()