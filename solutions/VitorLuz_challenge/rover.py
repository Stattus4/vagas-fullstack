from grid import Grid

class Rover:
    def __init__(self, grid:Grid, initial_x:int, initial_y:int, orientation:str):
        """
        initialize the rover with the initial position and orientation
        """
        self.grid = grid
        self.x = initial_x
        self.y = initial_y
        self.orientation = orientation
        self.data_collected = []
    
    def turn_left(self):
        """
        knowing that the rover turns 90º, 
        based on the compass rose and starting from the North, 
        if the rover turns left, you can go West and then South, East and again stop at North.
        
        So, if you take the real rover directions and add +1, you go to the next direction of the list, 
        but if you are in the end of the directions list, 
        you have to go back to the first position, that's why '% 4' is needed.

        4 % 4 = 0 start of the list

        """
        directions = ['N', 'W', 'S', 'E'] 
        idx = directions.index(self.orientation)
        self.orientation = directions[(idx + 1) % 4]
    
    def turn_right(self):
        """
        same idea of turn_left, but here the list of directions has been changed
        """
        directions = ['N', 'E', 'S', 'W']
        idx = directions.index(self.orientation)
        self.orientation = directions[(idx + 1) % 4]
    
    def increment_directional(self):
        """
        imagine a chessboard. If rover's self.orientation is North or South, 
        it moves along Y axis. On the other hand, if its self.orientation is East or West,
        it moves along X axis.

        Returns:
            tuple: the incremental change in position based on the rover's orientation.
        """
        if self.orientation == "N":
            return (-1, 0)
        if self.orientation == "S":
            return (1,0)
        if self.orientation == "E":
            return (0,1)
        if self.orientation == "W":
            return (0,-1)

    def move_forward(self):
        """
        Moves the rover one unit forward in the current direction.

        This method calculates the new position of the rover based on the current direction and
        updates the rover's position if the new position is within the grid bounds
        and there are no obstacles.

        The movement logic is based on the directional increment provided by the
        'increment_directional' method.
        """
        dx, dy = self.increment_directional()
        new_x = self.x + dx
        new_y = self.y + dy

        if self.grid.isInGrid(new_x, new_y) and not self.grid.isObstacle(new_x, new_y):
            self.x = new_x
            self.y = new_y
    
    def move_backward(self):
        """
        Same as 'move_forward' but here the rover moves one unit backward in the current
        direction.
        """
        dx, dy = self.increment_directional()
        new_x = self.x - dx
        new_y = self.y - dy

        if self.grid.isInGrid(new_x, new_y) and not self.grid.isObstacle(new_x, new_y):
            self.x = new_x
            self.y = new_y
    
    def collect_data(self):
        """
        Collects and records the current data from the rover.

        This method creates a dictionary containing the current position and orientation 
        of the rover, and adds this dictionary to the list of collected data.

        Returns:
            dict: dictionary with the collected information.
        """
        data = {"position": (self.x, self.y), "orientation": self.orientation}
        self.data_collected.append(data)
        return data