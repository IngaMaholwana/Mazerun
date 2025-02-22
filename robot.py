# from obstacles import create_random_obstacles,is_path_blocked,obstacles
from obstacles import *


directions = ['forward', 'right', 'back', 'left']
position_x = 0
position_y = 0
directions = ['forward', 'right', 'back', 'left']
current_direction_index = 0


def do_help():
    """
    Provides help information to the user
    :return: (True, help text) to indicate robot can continue after this command was handled
    """
    return True, """I can understand these commands:
OFF  - Shut down robot
HELP - provide information about commands
FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
BACK - move backward by specified number of steps, e.g. 'BACK 10'
RIGHT - turn right by 90 degrees
LEFT - turn left by 90 degrees
SPRINT - sprint forward according to a formula
REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
"""

def get_robot_name():
    """
    Returns the name of the robot user chooses
    :return: The name of the robot as a string
    """
    name = input("What do you want to name your robot? ")
    while len(name) == 0:
        name = input("What do you want to name your robot? ")
    return name

def get_command(robot_name):
    """
    Prompts the user for a command and returns the command as a string
    :param robot_name: The name of the robot
    :return: The command entered by the user
    """
    command = input(f"{robot_name}: What must I do next? ").lower().strip()
    return command

def valid_commands(command):
    """
    Checks if the command is valid
    :param command: The command to validate
    :return: True if command is valid, False otherwise
    """
    okay = ["off", "help", "forward", "back", "right", "left", "sprint", "replay"]
    if command.split(" ")[0] in okay:
        return True
    return False

def handle_command(command, robot_name):
    """
    Handles the command execution
    :param command: The command to execute
    :param robot_name: The name of the robot
    :return: True if the robot should continue, False if it should shut down
    """
    if command.lower() == 'off':
        print(f"{robot_name}: Shutting down..")
        return False
    elif command.lower() == 'help':
        success, help_text = do_help()
        print(help_text)
        return True
    elif valid_commands(command):
        # Here you would implement the actual movement commands
        print(f"{robot_name}: Executing {command}")
        return True
    else:
        print(f"{robot_name}: Sorry, I did not understand '{command}'")
        return True

def split_command_input(command):
    """
    Splits the command input into a list of arguments
    :param command: The command to split
    :return: A list of arguments
    """
    args = command.split(' ') # i wwant the int valiers
    return args


def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    # area limit vars
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100

    return min_x <= new_x <= max_x and min_y <= new_y <= max_y


def show_position(robot_name):
    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')

def obstacles_position():
    """this function is there to display them and name them for the player"""
    create_random_obstacles()
    if len(obstacles) > 0:
        print("There are some obstacles:")
        for obstacle in create_random_obstacles():
            print("- At position " + str(obstacle[0]) + "," + str(obstacle[1]) + " (to " + str(obstacle[0] + 4) + "," + str(obstacle[1] + 4) + ")")


def update_position(steps):
    """
    Update the current x and y positions given the current direction, and specific nr of steps
    :param steps:
    :return: True if the position was updated, else False
    """

    global position_x, position_y
    new_x = position_x
    new_y = position_y

    if directions[current_direction_index] == 'forward':
        new_y = new_y + steps
    elif directions[current_direction_index] == 'right':
        new_x = new_x + steps
    elif directions[current_direction_index] == 'back':
        new_y = new_y - steps
    elif directions[current_direction_index] == 'left':
        new_x = new_x - steps
    if is_position_allowed(new_x, new_y):
        position_x = new_x
        position_y = new_y
        return True 
    return False


def do_forward(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    new_x = position_x
    new_y = position_y + steps if directions[current_direction_index] == "forward" else position_y
    new_x = position_x + steps if directions[current_direction_index] == "right" else new_x
    new_y = position_y - steps if directions[current_direction_index] == "back" else new_y
    new_x = position_x - steps if directions[current_direction_index] == "left" else new_x

    if not is_path_blocked(position_x, position_y, new_x, new_y):
        if update_position(steps):
            return True, ' > '+robot_name+' moved forward by '+str(steps)+' steps.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    else:
        return True, f"{robot_name}: Sorry, there is an obstacle in the way."


def do_back(robot_name, steps):
    """
    Moves the robot forward the number of steps
    :param robot_name:
    :param steps:
    :return: (True, forward output text)
    """
    
    new_x = position_x
    new_y = position_y - steps if directions[current_direction_index] == "forward" else position_y
    new_x = position_x - steps if directions[current_direction_index] == "right" else new_x
    new_y = position_y + steps if directions[current_direction_index] == "back" else new_y
    new_x = position_x + steps if directions[current_direction_index] == "left" else new_x

    if not is_path_blocked(position_x, position_y, new_x, new_y):
        if update_position(-steps):
            return True, ' > '+robot_name+' moved back by '+str(steps)+' steps.'
        else:
            return True, ''+robot_name+': Sorry, I cannot go outside my safe zone.'
    else:
        return True, f"{robot_name}: Sorry, there is an obstacle in the way."


def do_right_turn(robot_name):
    """
    Do a 90 degree turn to the right
    :param robot_name:
    :return: (True, right turn output text)
    """
    global current_direction_index

    current_direction_index += 1
    if current_direction_index > 3:
        current_direction_index = 0

    return True, ' > '+robot_name+' turned right.'


def do_left_turn(robot_name):
    """
    Do a 90 degree turn to the left
    :param robot_name:
    :return: (True, left turn output text)
    """
    global current_direction_index

    current_direction_index -= 1
    if current_direction_index < 0:
        current_direction_index = 3

    return True, ' > '+robot_name+' turned left.'


def do_sprint(robot_name, steps):
    """
    Sprints the robot, i.e. let it go forward steps + (steps-1) + (steps-2) + .. + 1 number of steps, in iterations
    :param robot_name:
    :param steps:
    :return: (True, forward output)
    """

    if steps == 1:
        return do_forward(robot_name, 1)
    else:
        (do_next, command_output) = do_forward(robot_name, steps)
        print(command_output)
        return do_sprint(robot_name, steps - 1)
    

def updated_position():
    global position_x, position_y, directions, current_direction_index, obstacles
    position_x = 0
    position_y = 0
    directions = ['forward', 'right', 'back', 'left']
    current_direction_index = 0
    obstacles= []
    return position_x, position_y, directions, current_direction_index, obstacles



def start():
    """
    The main function to start the robot.
    It initializes the robot, handles commands, and displays relevant feedback.
    """
    robot_name = get_robot_name()
    print(f"{robot_name}: Hello kiddo!")

    # Create obstacles and display them to the user
    obstacles_position()

    running = True
    while running:
        command = get_command(robot_name)

        # Split command to handle possible arguments (e.g., FORWARD 10)
        command_parts = command.split()
        primary_command = command_parts[0]

        # Handle commands with arguments
        if primary_command in ["forward", "back", "sprint"] and len(command_parts) > 1:
            try:
                steps = int(command_parts[1])
                if primary_command == "forward":
                    success, output = do_forward(robot_name, steps)
                elif primary_command == "back":
                    success, output = do_back(robot_name, steps)
                elif primary_command == "sprint":
                    success, output = do_sprint(robot_name, steps)
                print(output)
                if success:  # Show the position immediately if the command was successful
                    show_position(robot_name)

            except ValueError:
                print(f"{robot_name}: Please provide a valid number of steps.")
            continue

        # Handle other commands without arguments
        if primary_command == "right":
            success, output = do_right_turn(robot_name)
            print(output)
        elif primary_command == "left":
            success, output = do_left_turn(robot_name)
            print(output)
        elif primary_command == "help":
            success, output = do_help()
            print(output)
        elif primary_command == "off":
            print(f"{robot_name}: Shutting down..")
            running = False
        elif primary_command == "replay":
            print(f"{robot_name}: Replay functionality not implemented yet.")  # Placeholder for REPLAY
        else:
            print(f"{robot_name}: Sorry, I did not understand '{command}'")

        # Show the current position after each command
        if running:
            show_position(robot_name)

if __name__ == "__main__":
    start()
