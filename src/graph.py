import googlemaps
from helper import constants

class RouteGraph:
    def __init__(self):
        self.gmaps = googlemaps.Client(key=constants.Constants.GOOGLEAPIKEY.value)

    def form_adjacency_matrix_time(self, row):
        """
        Forms adjacency matrix for the graph with time values
        
        Parameters:
        row : data row with map locations

        Returns:
        adjacency matrix with time values
        """
        adj_mat_time = []
        for i in range(len(row)):
            temp_sub_mat_time = []
            for j in range(len(row)):
                if (i == j):
                    temp_sub_mat_time.append(0)
                else:
                    my_dist = self.gmaps.distance_matrix(row[i], row[j])['rows'][0]['elements'][0]
                    temp_sub_mat_time.append(my_dist['duration']['value'])
            adj_mat_time.append(temp_sub_mat_time)
        return adj_mat_time

    def form_adjacency_matrix_distance(self, row):
        """
        Forms adjacency matrix for the graph with distance values
        
        Parameters:
        row : data row with map locations

        Returns:
        adjacency matrix with distance values
        """
        adj_mat_dist = []
        for i in range(len(row)):
            temp_sub_mat_dist = []
            for j in range(len(row)):
                if (i == j):
                    temp_sub_mat_dist.append(0)
                else:
                    my_dist = self.gmaps.distance_matrix(row[i], row[j])['rows'][0]['elements'][0]
                    temp_sub_mat_dist.append(my_dist['distance']['value'])
            adj_mat_dist.append(temp_sub_mat_dist)
        return adj_mat_dist
