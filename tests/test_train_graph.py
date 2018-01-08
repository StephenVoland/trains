import unittest
from src.train_graph import TrainGraph

class TrainGraphTest(unittest.TestCase):
    def setUp(self):
        self.train_graph = TrainGraph("AB5, BC4, CD8, DC8, DE6, AD5, CE2, EB3, AE7")


    # Testing train_graph.get_distance
    def test_empty_route_should_return_no_such_route(self):
        self.assertEqual(self.train_graph.get_distance(""), "NO SUCH ROUTE")

    def test_nonexistant_single_step_route_should_return_no_such_route(self):
        self.assertEqual(self.train_graph.get_distance("A-C"), "NO SUCH ROUTE")

    def test_existing_single_step_route_should_return_distance(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-B"), 5)

    def test_nonexistant_multiple_step_route_should_return_no_such_route(self):
        self.assertEqual(self.train_graph.get_distance("A-B-D"), "NO SUCH ROUTE")

    def test_existing_multiple_step_route_should_return_distance(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-B-C"), 9)


    # Testing train_graph.get_number_trips
    def test_number_trips_max_stops_with_missing_connection_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips("A", "A", 3, TrainGraph.TripType.max_stops), 0)

    def test_number_trips_max_stops_with_valid_routes_should_return_number(self):
        self.assertEqual(self.train_graph.get_number_trips("E", "D", 5, TrainGraph.TripType.max_stops), 2)

    def test_number_trips_max_stops_with_too_small_stops_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips("E", "D", 2, TrainGraph.TripType.max_stops), 0)

    def test_number_trips_exact_stops_with_missing_connection_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips("A", "A", 3, TrainGraph.TripType.exact_stops), 0)

    def test_number_trips_exact_stops_with_valid_routes_should_return_number(self):
        self.assertEqual(self.train_graph.get_number_trips("A", "C", 2, TrainGraph.TripType.exact_stops), 2)

    def test_number_trips_exact_stops_with_no_matches_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips("E", "D", 4, TrainGraph.TripType.exact_stops), 0)


    # Testing train_graph.get_shortest_distance
    def test_route_to_self_should_not_automatically_return_zero_distance(self):
        self.assertEqual(self.train_graph.get_shortest_distance("D", "D"), 16)

    def test_shortest_dist_to_unreachable_destination_should_return_no_such_route(self):
        self.assertEqual(self.train_graph.get_shortest_distance("C", "A"), "NO SUCH ROUTE")

    def test_direct_connection_shortest_should_return_direct_distance(self):
        self.assertEqual(self.train_graph.get_shortest_distance("A", "B"), 5)

    def test_indirect_connection_shortest_should_return_indirect_distance(self):
        self.assertEqual(self.train_graph.get_shortest_distance("A", "E"), 7)

    def test_two_routes_tie_should_return_correct_distance(self):
        self.assertEqual(self.train_graph.get_shortest_distance("A", "C"), 9)

    # Testing train_graph.get_number_trips_to_distance
    def test_num_routes_of_less_than_zero_distance_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips_to_distance("E", "B", 0), 0)

    def test_num_routes_to_unreachable_city_should_return_zero(self):
        self.assertEqual(self.train_graph.get_number_trips_to_distance("E", "A", 100), 0)

    def test_num_routes_of_complex_path_should_return_five(self):
        self.assertEqual(self.train_graph.get_number_trips_to_distance("A", "C", 19), 5)


    # Default tests
    def test_1(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-B-C"), 9)

    def test_2(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-D"), 5)

    def test_3(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-D-C"), 13)

    def test_4(self):
        self.assertAlmostEqual(self.train_graph.get_distance("A-E-B-C-D"), 22)

    def test_5(self):
        self.assertEqual(self.train_graph.get_distance("A-E-D"), "NO SUCH ROUTE")

    def test_6(self):
        self.assertEqual(self.train_graph.get_number_trips("C", "C", 3, TrainGraph.TripType.max_stops), 2)

    def test_7(self):
        self.assertEqual(self.train_graph.get_number_trips("A", "C", 4, TrainGraph.TripType.exact_stops), 3)

    def test_8(self):
        self.assertEqual(self.train_graph.get_shortest_distance("A", "C"), 9)

    def test_9(self):
        self.assertEqual(self.train_graph.get_shortest_distance("B", "B"), 9)

    def test_10(self):
        self.assertEqual(self.train_graph.get_number_trips_to_distance("C", "C", 30), 7)

