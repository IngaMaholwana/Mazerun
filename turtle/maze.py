in_y, max_y = -200, 200
min_x, max_x = -100, 100

def draw_baseshape_square():
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
                row_coords.append((row, col))
            grid.append(row_coords)
            
        return grid
    
    except ValueError:
        print("Please enter a valid integer for grid size")
        return None

