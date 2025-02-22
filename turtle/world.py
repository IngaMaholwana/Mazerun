#this is going to set up the canvas for the boarders this is  where the game and maze is going to be visialiesd

import turtle 
from obstacles import *

def draw_board():
    """
    Draws the board on the turtle screen based on area limits.
    """
    # Define the area limits
    min_x, max_x = -100, 100
    min_y, max_y = -200, 200

    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("Robot Board")
    screen.bgcolor("white")

    # Create a turtle object to draw
    board_turtle = turtle.Turtle()
    board_turtle.speed(0)
    board_turtle.penup()

    # Move to the starting position (bottom-left corner of the rectangle)
    board_turtle.goto(min_x, min_y)
    board_turtle.pendown()
    board_turtle.pensize(2)
    board_turtle.color("black")

    # Draw the rectangle (board area)
    board_turtle.goto(max_x, min_y)  # Bottom-right
    board_turtle.goto(max_x, max_y)  # Top-right
    board_turtle.goto(min_x, max_y)  # Top-left
    board_turtle.goto(min_x, min_y)  # Back to Bottom-left

    # Finish drawing
    board_turtle.penup()
    board_turtle.hideturtle()

    # Keep the window open until the user closes it
    screen.mainloop()

# # Call the function to draw the board
# draw_board()

turtle_robot = turtle.Turtle()#NDIM IS THE TURTLE 
min_y, max_y = -200, 200
min_x, max_x = -100, 100 # want to set them minims of the turtle moves
directions = ['forward', 'right','back','left']
current_direction_index = 0

def obstacles_position():
    create_random_obstacles()
    if len(obstacles) > 0:
        for obstacle in create_random_obstacles():
            print("- At position " + str(obstacle[0]) + "," + str(obstacle[1]) + " (to " + str(obstacle[0] + 4) + "," + str(obstacle[1] + 4) + ")")
            draw_square(obstacle)

def is_position_allowed(new_x, new_y):
    """
    Checks if the new position will still fall within the max area limit
    :param new_x: the new/proposed x position
    :param new_y: the new/proposed y position
    :return: True if allowed, i.e. it falls in the allowed area, else False
    """
    return min_x <= new_x <= max_x and min_y <= new_y <= max_y

def show_position(robot_name):

    print(' > '+robot_name+' now at position ('+str(position_x)+','+str(position_y)+').')
    pass
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
            turtle_robot.forward(steps)
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
            turtle_robot.back(steps)
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
    turtle_robot.right(90)
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
    turtle_robot.left(90)
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
    obstacles = []
    return position_x, position_y, directions, current_direction_index, obstacles