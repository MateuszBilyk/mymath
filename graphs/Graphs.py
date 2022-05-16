"""
Class graph:
-- init
    -- first argument is an integer which means how many vertices should have a graph.
    -- second argument is a function from n^2 -> {0,1} x R which tells if there is a directed edge between two vertices
        which weight is the second element of the pair it returns
"""


class Graph:
    def __init__(self,n,E):
        self.n=n
        self.E=E
