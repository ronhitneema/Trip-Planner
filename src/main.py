import os
import argparse

from graph import RouteGraph
from helper import constants
from mst.kruskals import MST
from path import optimum_path
from helper import data_reader
from maps import map_generator


class MinimumSpanningTree:
    """
    A class that computes the minimum spanning tree for a given adjacency matrix.
    """

    def __init__(self, adj_matrix):
        self.mst_obj = MST(len(adj_matrix))
        self.mst_obj.kruskalMST(adj_matrix)

    def get_edges(self):
        return self.mst_obj.getEdges()


class RouteAdjMatrix:
    """
    A class that analyzes the route graph and computes minimum spanning trees for distances and times.
    """

    def __init__(self):
        self.route_adj_matrix = self.read_route_adj_matrix()

    @staticmethod
    def read_route_adj_matrix():
        """
        Reads the route graph from the Excel file and returns a RouteGraph object.
        """
        route_graph = RouteGraph()
        return route_graph

    def compute_minimum_spanning_tree_distance(self, row):
        """
        Computes the minimum spanning tree for distances and returns a MinimumSpanningTree object.
        """
        adj_matrix = self.route_adj_matrix.form_adjacency_matrix_distance(row)
        mst_distance = MinimumSpanningTree(adj_matrix)
        return mst_distance

    def compute_minimum_spanning_tree_time(self, row):
        """
        Computes the minimum spanning tree for times and returns a MinimumSpanningTree object.
        """
        adj_matrix = self.route_adj_matrix.form_adjacency_matrix_time(row)
        mst_time = MinimumSpanningTree(adj_matrix)
        return mst_time


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("argument", help="Enter either 'time' or 'distance'")
    args = parser.parse_args()

    # Analyze the route graph
    adj_matrix = RouteAdjMatrix()
    cwd = os.getcwd()
    parent_dir = os.path.dirname(cwd)
    file_path = parent_dir + constants.Constants.XLSPATH.value
    data_obj = data_reader.ExcelReader(file_path)
    data = data_obj.read_sheet()

    if args.argument.lower() == "distance":
        print("Computing optimal path based on distance")

        for row in data:
            row_data = [x for x in row if x == x]
            # Compute the minimum spanning tree for distances
            mst_distance = adj_matrix.compute_minimum_spanning_tree_distance(row_data)
            distance_edges = mst_distance.get_edges()
            for index in distance_edges:
                print(
                    f'Edge {index}:({distance_edges[index][0]}, {distance_edges[index][1]}) '
                    f'cost:{distance_edges[index][2]}')
            optimum_graph = optimum_path.Graph(list(distance_edges.values()))
            short_path_finder = optimum_path.ShortestPathFinder(optimum_graph, 0)
            shortest_path = short_path_finder.find_shortest_path()
            maps_gen = map_generator.MapGenerator(row_data, shortest_path)
            maps_gen.generate_map()

    elif args.argument.lower() == "time":
        # Compute the minimum spanning tree for times
        for row in data:
            row_data = [x for x in row if x == x]
            mst_time = adj_matrix.compute_minimum_spanning_tree_time(row_data)
            time_edges = mst_time.get_edges()
            for index in time_edges:
                print(f'Edge {index}:({time_edges[index][0]}, {time_edges[index][1]}) cost:{time_edges[index][2]}')
            optimum_graph = optimum_path.Graph(list(time_edges.values()))
            short_path_finder = optimum_path.ShortestPathFinder(optimum_graph, 0)
            shortest_path = short_path_finder.find_shortest_path()
            maps_gen = map_generator.MapGenerator(row_data, shortest_path)
            maps_gen.generate_map()
    else:
        print("Invalid input. Please enter either 'time' or 'distance'.")



if __name__ == "__main__":
    main()
