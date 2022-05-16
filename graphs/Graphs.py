import matplotlib.pyplot as plt
import math

"""
Class graph:
-- init
    -- first argument is an integer which means how many vertices should have a graph.
    -- second argument is a function from n^2 -> {0,1} x R which tells if there is a directed edge between two vertices
        which weight is the second element of the pair it returns
-- draw_graph_on_circle
    makes a drawing of the graph on a circle
"""


class Graph:
    def __init__(self, n, E):
        self.n = n
        self.E = E

    def __simple_edge__(self, x, y):
        if self.E(x, y) == (1, 1) and self.E(y, x) == (1, 1):
            return 1
        return 0

    def draw_graph_on_circle(self):
        x, y = [], []
        angle = 2*math.pi/self.n
        for i in range(self.n):
            x.append(math.cos(angle*i))
            y.append(math.sin(angle*i))
        for i in range(self.n):
            for j in range(self.n):
                if self.__simple_edge__(i, j):
                    plt.plot([x[i], x[j]], [y[i], y[j]], "b-")
        plt.scatter(x, y)
        plt.title("Visualization of the graph on a circle")
        plt.show()

# Testing


def identity(x, y):
    return 1, 1


def odd(x, y):
    if (x+y) % 2:
        return 1, 1
    return 0, 0


full_graph = Graph(7, identity)
full_graph.draw_graph_on_circle()

odd_edges_graph = Graph(7, odd)
odd_edges_graph.draw_graph_on_circle()



