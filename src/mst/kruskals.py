import sys

class MST:
    parent = []
    edges = {}
    def __init__(self, num_vertices):
        self.parent = [i for i in range(num_vertices)]
        pass

    # finds the parent of a vertex
    def find(self, i):
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    # union of two sets
    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)
        self.parent[xroot] = yroot

    # Kruskal's algorithm
    def kruskalMST(self, adj_matrix):
        mincost = 0  # Cost of min MST
        num_vertices = len(self.parent)
        # Initialize sets of disjoint sets
        for i in range(num_vertices):
            self.parent[i] = i

        # Include minimum weight edges one by one
        edge_count = 0
        while edge_count < num_vertices - 1:
            min = sys.maxsize
            a = -1
            b = -1
            for i in range(num_vertices):
                for j in range(num_vertices):
                    if self.find(i) != self.find(j) and adj_matrix[i][j] < min:
                        min = adj_matrix[i][j]
                        a = i
                        b = j
            self.union(a, b)
            self.edges[edge_count] = (a, b, min)
            edge_count += 1
            mincost += min

    def getEdges(self):
        return self.edges
