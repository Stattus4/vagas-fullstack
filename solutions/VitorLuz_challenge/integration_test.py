import unittest
from grid import Grid
from rover import Rover
from rover_controller import RoverController

class TestRoverIntegration(unittest.TestCase):
    def test_rover_navigation_and_data_collection(self):
        grid_map = [
            [0, 0, 0, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0],
            [1, 0, 1, 0, 1],
            [0, 0, 0, 1, 0]
        ]
        grid = Grid(grid_map)
        rover = Rover(grid, initial_x=2, initial_y=2, orientation='N')
        controller = RoverController(rover)

        commands = "F, R, F, L, F, S, B, L, F, S"
        result = controller.execute_commands(commands)

        expected_final_position = (1, 2)
        expected_final_orientation = 'W'
        expected_data_collected = [
            {"position": (0, 2), "orientation": 'N'},
            {"position": (1, 2), "orientation": 'W'}
        ]

        self.assertEqual(result["final_position"], expected_final_position)
        self.assertEqual(result["final_orientation"], expected_final_orientation)
        self.assertEqual(result["data_collected"], expected_data_collected)

if __name__ == '__main__':
    unittest.main()
