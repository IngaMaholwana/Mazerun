# def do_help():
#     """
#     Provides help information to the user
#     :return: (True, help text) to indicate robot can continue after this command was handled
#     """
#     return True, """I can understand these commands:
# OFF  - Shut down robot
# HELP - provide information about commands
# FORWARD - move forward by specified number of steps, e.g. 'FORWARD 10'
# BACK - move backward by specified number of steps, e.g. 'BACK 10'
# RIGHT - turn right by 90 degrees
# LEFT - turn left by 90 degrees
# SPRINT - sprint forward according to a formula
# REPLAY - replays all movement commands from history [FORWARD, BACK, RIGHT, LEFT, SPRINT]
# """ 

# def get_robot_name():
#     """
#     Returns the name of the robot user chooses
#     it cant be
#     :return: The name of the robot as a string
#     """
#     name = input("What do you want to name your robot? ")
#     while len(name) == 0:
#         name = input("What do you want to name your robot? ")
#     return name

# def get_command(robot_name):
#     """
#     Prompts the user for a command and returns the command as a string
#     :param robot_name: The name of the robot
#     :return: The command entered by the user
#     """
#     command = input(f"{robot_name}: What must I do next? ").lower().strip()
#     return command

# def valid_commands(command):
#     """this is where i will check the currently alloweed"""
#     okay = ["off", "help", "forward", "back", "right", "left", "sprint", "replay"]  #dont mind this replay and sprint nonses foer now
#     if command.split(" ")[0] in okay:
#         return True

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

def start():
    """
    The main function to start the robot
    """
    robot_name = get_robot_name()
    print(f"{robot_name}: Hello kiddo!")
    
    running = True
    while running:
        command = get_command(robot_name)
        running = handle_command(command, robot_name)

if __name__ == "__main__":
    start()
