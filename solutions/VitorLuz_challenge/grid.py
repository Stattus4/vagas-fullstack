class Grid:
    def __init__(self, grid_map: list[list[int]]):
        """
        initialize the 2D matriz

        Args:
            grid_map (list[list[int]]): 
                grip_map receives one list of lists(integer).
                0 represents 'ok to go'
                1 represents 'dont go'
        """
        self.grid_map = grid_map
        self.rows = len(grid_map)
        self.cols = len(grid_map[0]) if grid_map != 0 else 0
    

    def isInGrid(self, cord_x:int, cord_y:int):
        """
        check if the actual position of the rover is inside the grid

        Args:
            cord_x (int): rover x position
            cord_y (int): rover y position
        """
        if (cord_x >= 0 and cord_x < self.rows) and (cord_y >= 0 and cord_y < self.cols):
            return True
    
    def isObstacle(self, cord_x:int, cord_y:int):
        """
        check if the coordinates is ok or not to go

        Args:
            cord_x (int): rover x position
            cord_y (int): rover y position

        """
        if self.grid_map[cord_x][cord_y] == 1 and self.isInGrid(cord_x,cord_y):
            return True