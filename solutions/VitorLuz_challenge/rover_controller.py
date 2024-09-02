from rover import Rover

class RoverController:
    def __init__(self, rover:Rover):
        """
        initialize a controller with rover instance

        """
        self.rover = rover
    
    def execute_commands(self, commands:str):
        """
        executes a series of commands on the rover.

        Args:
            commands (str): a string indicating which commands 
            should be executed by the rover. 
            
            Note that I use the upper and split methods to avoid 
            possible errors when typing the commands

        """
        commands_upper = commands.upper()
        commands_list = commands_upper.split(',')

        for command in commands_list:
            command = command.strip()
            if command == 'F':
                self.rover.move_forward()
            elif command == 'B':
                self.rover.move_backward()
            elif command == 'L':
                self.rover.turn_left()
            elif command == 'R':
                self.rover.turn_right()
            elif command == 'S':
                self.rover.collect_data()
            elif command == '':
                continue               
            else:
                raise ValueError(f"Invalid command: {command}")
        
        return{
            "final_position" : (self.rover.x, self.rover.y),
            "final_orientation" : (self.rover.orientation),
            "data_collected" : (self.rover.data_collected)
        }