import unittest
from grid import Grid
from rover import Rover
from rover_controller import RoverController

class TestGrid(unittest.TestCase):
    def test_is_in_grid(self):
        grid_map = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        grid = Grid(grid_map)
        self.assertTrue(grid.isInGrid(0, 0))
        self.assertFalse(grid.isInGrid(3, 3))

    def test_is_obstacle(self):
        grid_map = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        grid = Grid(grid_map)
        self.assertTrue(grid.isObstacle(1, 1))
        self.assertFalse(grid.isObstacle(2, 1))

class TestRover(unittest.TestCase):
    def setUp(self):
        grid_map = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        self.grid = Grid(grid_map)
        self.rover = Rover(self.grid, initial_x=1, initial_y=1, orientation='N')

    def test_turn_left(self):
        self.rover.turn_left()
        self.assertEqual(self.rover.orientation, 'W')
        
        self.rover.turn_left()
        self.assertEqual(self.rover.orientation, 'S')

        self.rover.turn_left()
        self.assertEqual(self.rover.orientation, 'E')
        
        self.rover.turn_left()
        self.assertEqual(self.rover.orientation, 'N')

    def test_turn_right(self):
        self.rover.turn_right()
        self.assertEqual(self.rover.orientation, 'E')

        self.rover.turn_right()
        self.assertEqual(self.rover.orientation, 'S')

        self.rover.turn_right()
        self.assertEqual(self.rover.orientation, 'W')

        self.rover.turn_right()
        self.assertEqual(self.rover.orientation, 'N')

    def test_move_forward(self):
        self.rover.orientation = 'S'
        self.rover.move_forward()
        self.assertEqual((self.rover.x, self.rover.y), (2, 1))

    def test_move_backward(self):
        self.rover.orientation = 'S'
        self.rover.move_backward()
        self.assertEqual((self.rover.x, self.rover.y), (0, 1))

    def test_collect_data(self):
        data = self.rover.collect_data()
        expected_data = {"position": (1, 1), "orientation": "N"}
        self.assertEqual(data, expected_data)
        self.assertIn(expected_data, self.rover.data_collected)

class TestRoverController(unittest.TestCase):
    def setUp(self):
        grid_map = [
            [0, 0, 0],
            [0, 1, 0],
            [0, 0, 0]
        ]
        self.grid = Grid(grid_map)
        self.rover = Rover(self.grid, initial_x=2, initial_y=2, orientation='N')
        self.controller = RoverController(self.rover)

    def test_execute_commands(self):
        commands = "F,F,R,F,L,L,F,L,F,R,f,l,F,F,L,F,l,F,R,S"
        result = self.controller.execute_commands(commands)
        
        expected_position = (2, 1)
        expected_orientation = 'E'
        expected_data_collected = [
            {"position": (2, 1), "orientation": 'E'}
        ]

        self.assertEqual(result["final_position"], expected_position)
        self.assertEqual(result["final_orientation"], expected_orientation)
        self.assertEqual(result["data_collected"], expected_data_collected)

if __name__ == '__main__':
    unittest.main()
