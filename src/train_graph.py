import sys
from .dijkstras_alg import DijkstrasAlg
from enum import Enum


class TrainGraph:
    """
    Takes a string representing a directed graph of city-to-city connections and their distances of
    the format "AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7" and allows querying of 
    - shortest routes,
    - the distance of specific routes,
    - the number of routes from one city to another with a max number of stops,
    - the number of routes from one city to another with an exact number of stops,
    - the number of routes from one city to another with less than a specified distance.

    Formatting of the graph string and the submitted routes is assumed to be valid.
    All distances are required to be greater than 0 so that the algorithms used have valid answers.
    """

    TripType = Enum('TripType', 'exact_stops max_stops')


    def __init__(self, graph):
        self.graph = self._convert_graph_to_dict(graph)
        self.dijkstras_alg = DijkstrasAlg(self.graph)


    def _convert_graph_to_dict(self, graph):
        """Convert the 'graph' string to a dictionary."""
        graph_dict = {}
        connection_list = [x.strip() for x in graph.split(',')]
        for connection in connection_list:
            start_city = connection[0]
            next_city = connection[1]
            distance = float(connection[2:])

            if start_city not in graph_dict:
                graph_dict[start_city] = {}

            graph_dict[start_city][next_city] = distance
        return graph_dict


    def get_shortest_distance(self, start_node, end_node):
        return self.dijkstras_alg.get_distance(start_node, end_node)


    def get_distance(self, route):
        """Calculate distance for a specific route, where 'route' is a string of format "A-B-D" """
        if route == "":
            return "NO SUCH ROUTE"

        route_cities = route.split('-')
        current_city = route_cities[0]
        total_distance = 0
        # Iterate through cities on the route and sum their distances.
        for i in range(1, len(route_cities)):
            next_city = route_cities[i]
            if current_city in self.graph and next_city in self.graph[current_city]:
                total_distance += self.graph[current_city][next_city]
            else:
                return "NO SUCH ROUTE"
            current_city = next_city

        return total_distance


    def get_number_trips(self, start_city, end_city, num_stops, trip_type):
        """
        Get the number of possible trips from start_city to end_city.
        If trip_type is TripType.max_stops, all trips with stops <= num_stops are counted.
        Otherwise only trips with exactly num_stops are counted.
        """
        sum_routes = 0
        if num_stops == 0:
            return 0

        # iterate through all connections from start_city
        for next_city in self.graph[start_city]:
            if next_city == end_city and (trip_type == self.TripType.max_stops or num_stops == 1):
                sum_routes += 1

            sum_routes += self.get_number_trips(next_city, end_city, num_stops - 1, trip_type)

        return sum_routes


    def get_number_trips_to_distance(self, start_city, end_city, max_distance):
        """Get the number of possible trips from start_city to end_city of less than max_distance."""
        sum_routes = 0
        # iterate through all connections from start_city
        for next_city, distance_to_next in self.graph[start_city].items():
            if next_city == end_city and distance_to_next < max_distance:
                sum_routes += 1
            if distance_to_next < max_distance:
                sum_routes += self.get_number_trips_to_distance(next_city, end_city, max_distance - distance_to_next)
        return sum_routes


