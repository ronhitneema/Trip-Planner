import heapq

class Graph:
    def __init__(self, edges):
        self.adj_list = {}
        for node1, node2, weight in edges:
            if node1 not in self.adj_list:
                self.adj_list[node1] = {}
            if node2 not in self.adj_list:
                self.adj_list[node2] = {}
            self.adj_list[node1][node2] = weight
            self.adj_list[node2][node1] = weight

class ShortestPathFinder:
    def __init__(self, graph, start_node):
        self.graph = graph
        self.start_node = start_node
        self.dist = {start_node: 0}

    def find_shortest_path(self):
        """
        Finds shortest path for nodes of given graph
        
        Returns:
        sorted nodes (map locations)
        """
        pq = [(0, self.start_node)]
        visited = set()
        while pq:
            (d, node) = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            for neighbor, weight in self.graph.adj_list[node].items():
                new_dist = self.dist[node] + weight
                if neighbor not in self.dist or new_dist < self.dist[neighbor]:
                    self.dist[neighbor] = new_dist
                    heapq.heappush(pq, (new_dist, neighbor))

        sorted_nodes = sorted(self.dist.items(), key=lambda x: x[1])
        return sorted_nodes

