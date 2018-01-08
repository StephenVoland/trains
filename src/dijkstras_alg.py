class DijkstrasAlg:
    """Implements Dijkstra's algorithm and stores the shortest paths from all nodes to all reachable nodes."""

    """
    'shortest_dists' is a dictionary storing the shortest distances between any two cities.
    In the example below, the shortest distance from A to B is 5.0, from E to D is 15.0, etc.
    Note that a city is not at distance 0 from itself; at least one edge must be traversed to create a route.
    Destinations that can't be reached will not appear; for example from A to A.

    {'A': {'B': 5.0, 'C': 9.0, 'D': 1.0, 'E': 3.0},
     'B': {'B': 9.0, 'C': 4.0, 'D': 12.0, 'E': 6.0},
     'C': {'B': 5.0, 'C': 9.0, 'D': 8.0, 'E': 2.0},
     'D': {'B': 5.0, 'C': 8.0, 'D': 16.0, 'E': 2.0},
     'E': {'B': 3.0, 'C': 7.0, 'D': 15.0, 'E': 9.0}}
    """


    def __init__(self, graph_dict):
        """Find and store all shortest routes for this graph."""
        self.shortest_dists = {}

        # Run Dijkstra's algorithm with each node as the start node.
        for start_node in graph_dict.keys():
            self.shortest_dists[start_node] = self._compute_shotest_paths(graph_dict, start_node)


    def _compute_shotest_paths(self, graph_dict, start_node):
        """Use Dijkstra's algorithm to compute all shortest paths."""
        completed_nodes = {}
        visited_nodes = {start_node: 0}

        while visited_nodes:
            min_value_key = min(visited_nodes, key=visited_nodes.get)
            cost_to_min_node = visited_nodes.pop(min_value_key)

            for k, v in graph_dict[min_value_key].items():
                if k not in completed_nodes:
                    comparison_min = cost_to_min_node + v
                    if k not in visited_nodes:
                        visited_nodes[k] = comparison_min
                    else:
                        visited_nodes[k] = min(comparison_min, visited_nodes[k])

            # Don't mark start node completed at a distance of 0
            if min_value_key != start_node or cost_to_min_node > 0:
                completed_nodes[min_value_key] = cost_to_min_node
        return completed_nodes


    def get_distance(self, start_node, end_node):
        if end_node in self.shortest_dists.get(start_node, {}):
            return self.shortest_dists[start_node][end_node]
        return "NO SUCH ROUTE"

