from turtle import Turtle, Screen
# from maze import draw_baseshape_square
import random

def create_maze(grid_size=10, cell_size=40):
    """Create maze using randomized Prim's algorithm"""
    # Initialize grid with all walls
    min_y, max_y = -200, 200
    min_x, max_x = -100, 100
    grid = []
    for row in range(grid_size):
        grid_row = []
        for col in range(grid_size):
            cell = {
                'position': (min_x + (col * cell_size), max_y - (row * cell_size)),
                'size': cell_size,
                'visited': False,
                'walls': {'N': True, 'S': True, 'E': True, 'W': True}
            }
            grid_row.append(cell)
        grid.append(grid_row)
    
    # Start with random cell
    start_row = random.randint(0, grid_size-1)
    start_col = random.randint(0, grid_size-1)
    grid[start_row][start_col]['visited'] = True
    
    # Add walls of starting cell to wall list
    walls = []
    add_walls_to_list(grid, walls, start_row, start_col)
    
    # Process walls until none remain
    while walls:
        # Pick random wall
        wall = random.choice(walls)
        row, col, direction = wall
        
        # Check cells on both sides of wall
        next_row, next_col = get_next_cell(row, col, direction)
        
        # If one cell is unvisited, make passage
        if is_valid_cell(next_row, next_col, grid_size):
            if not grid[row][col]['visited'] and grid[next_row][next_col]['visited']:
                make_passage(grid, row, col, next_row, next_col, direction)
                grid[row][col]['visited'] = True
                add_walls_to_list(grid, walls, row, col)
            elif grid[row][col]['visited'] and not grid[next_row][next_col]['visited']:
                make_passage(grid, row, col, next_row, next_col, direction)
                grid[next_row][next_col]['visited'] = True
                add_walls_to_list(grid, walls, next_row, next_col)
        
        # Remove processed wall
        walls.remove(wall)
    
    return grid

def add_walls_to_list(grid, walls, row, col):
    """Add all walls of cell to wall list"""
    if row > 0:
        walls.append((row, col, 'N'))
    if row < len(grid)-1:
        walls.append((row, col, 'S'))
    if col > 0:
        walls.append((row, col, 'W'))
    if col < len(grid)-1:
        walls.append((row, col, 'E'))

def get_next_cell(row, col, direction):
    """Get coordinates of cell on other side of wall"""
    if direction == 'N':
        return row-1, col
    elif direction == 'S':
        return row+1, col
    elif direction == 'E':
        return row, col+1
    else:  # W
        return row, col-1

def is_valid_cell(row, col, grid_size):
    """Check if cell coordinates are within grid"""
    return 0 <= row < grid_size and 0 <= col < grid_size

def make_passage(grid, row1, col1, row2, col2, direction):
    """Remove wall between two cells"""
    # Remove wall from first cell
    grid[row1][col1]['walls'][direction] = False
    
    # Remove wall from second cell
    opposite = {'N': 'S', 'S': 'N', 'E': 'W', 'W': 'E'}
    grid[row2][col2]['walls'][opposite[direction]] = False

def draw_maze():
    """Draw the maze using turtle"""
    screen = Screen()
    screen.title("Maze Generated with Prim's Algorithm")
    screen.setup(600, 600)
    
    tmaze = Turtle()
    tmaze.speed('fastest')
    tmaze.hideturtle()
    tmaze.pensize(2)
    
    # Generate and draw maze
    grid = create_maze()
    draw_grid(tmaze, grid)
    
    screen.mainloop()

def draw_grid(tmaze, grid):
    """Draw the complete maze"""
    for row in range(len(grid)):
        for col in range(len(grid)):
            draw_cell(tmaze, grid[row][col], grid[row][col]['walls'])

def draw_cell(tmaze, cell, walls):
    """Draw a single cell with its walls"""
    x, y = cell['position']
    size = cell['size']
    
    tmaze.penup()
    tmaze.goto(x, y)
    
    # Draw walls
    for direction in ['N', 'E', 'S', 'W']:
        tmaze.pendown() if walls[direction] else tmaze.penup()
        tmaze.forward(size)
        tmaze.right(90)

if __name__ == "__main__":
    
    draw_maze()
