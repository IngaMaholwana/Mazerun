min_y, max_y = -200, 200
min_x, max_x = -100, 100

def draw_baseshape_square(cell_size=4):  # Added cell_size parameter
    """Create the rows and cells of the maze.
    Returns:
        list: A 2D list containing coordinate tuples for each cell
    """
    try:
        gridsz = int(input("Enter the grid size: "))
        grid = []
        
        for row in range(gridsz):
            row_coords = []
            for col in range(gridsz):
                # Calculate actual coordinates with cell size
                x = min_x + (col * cell_size)
                y = max_y - (row * cell_size)
                cell = {
                    'position': (x, y),
                    'size': cell_size,
                    'blocked': False  # Add blocked state
                }
                row_coords.append(cell)
            grid.append(row_coords)
            
        return grid
    
    except ValueError:
        print("Please enter a valid integer for grid size")
        return None

def is_position_blocked(x, y, grid):
    """Check if a position is blocked by any cell in the grid
    Args:
        x: x-coordinate to check
        y: y-coordinate to check
        grid: the maze grid
    Returns:
        bool: True if position is blocked, False otherwise
    """
    for row in grid:
        for cell in row:
            cell_x, cell_y = cell['position']
            size = cell['size']
            
            # Check if position is within cell boundaries
            if (cell['blocked'] and 
                cell_x <= x <= cell_x + size and 
                cell_y - size <= y <= cell_y):
                return True
    return False

def is_path_blocked(x1, y1, x2, y2, grid):
    """Check if there's any blocked cell in the path
    Args:
        x1, y1: Starting coordinates
        x2, y2: Ending coordinates
        grid: the maze grid
    Returns:
        bool: True if path is blocked, False otherwise
    """
    if y1 == y2:  # Horizontal movement
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if is_position_blocked(x, y1, grid):
                return True
    else:  # Vertical movement
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if is_position_blocked(x1, y, grid):
                return True
    return False



# Example usage:
def main():
    # Create the grid
    maze_grid = draw_baseshape_square()
    if not maze_grid:
        return
    
    # Example: Mark some cells as blocked
    if len(maze_grid) > 0 and len(maze_grid[0]) > 0:
        # Block some cells for testing
        maze_grid[0][0]['blocked'] = True
        
        # Test position blocking
        x, y = -100, 200  # Example coordinates
        is_blocked = is_position_blocked(x, y, maze_grid)
        print(f"Position ({x}, {y}) is blocked: {is_blocked}")
        
        # Test path blocking
        start_x, start_y = -100, 200
        end_x, end_y = -96, 200
        path_blocked = is_path_blocked(start_x, start_y, end_x, end_y, maze_grid)
        print(f"Path from ({start_x}, {start_y}) to ({end_x}, {end_y}) is blocked: {path_blocked}")

if __name__ == "__main__":
    main()

