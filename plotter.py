__author__ = 'zieghailo'

import matplotlib.pyplot as plt

# plt.ion()

def show():
    plt.show()
    plt.get_current_fig_manager().full_screen_toggle()

def plot_graph(graph):
    # plt.ion()
    x = [p.x for p in graph.points]
    y = [p.y for p in graph.points]

    plt.plot(x, y, 'b*')
    plt.draw()


def plot_arrows(graph):
    for p in graph.points:
        x = p.x
        y = p.y

        for c in p.connections:
            cx = c.x
            cy = c.y
            # ax.arrow(x, y, cx-x, cy-y)
            plt.plot([x, cx], [y, cy], 'k')
    plt.draw()


def plot_visited(visited):
    x = [p.x for p in visited]
    y = [p.y for p in visited]

    plt.plot(x, y, 'ro', ms=7)
    plt.draw()

def plot_connection(start, end):
    plt.plot([start.x, end.x], [start.y, end.y])

def start_gui(graph):
    fig = plt.figure(1)
    ax = fig.add_subplot(111)
    ax.set_title('click to build line segments')
    line, = ax.plot([0, 100], [0, 100], 'b.')  # empty line
    pointbuilder = PointBuilder(line, ax, graph)
    fig.waitforbuttonpress(0)

    plt.show()


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

        plt.cla()
        self.graph.build_graph()
        plot_arrows(self.graph)

        plot_graph(self.graph)

        # self.points.figure.waitforbuttonpress(0)




if __name__ == "__main__":
    start_gui()