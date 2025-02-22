in_y, max_y = -200, 200
min_x, max_x = -100, 100

def draw_baseshape():
    """Create the rows and cells of the maze.
    Returns:
        list: A 2D list containing coordinate tuples for each cell
    """
    max = 201  # rows
    min = 401  # columns
    
    try:
        gridsz = int(input("Enter the grid size: "))
        # Create a 2D list to store the coordinates
        grid = []
        
        for row in range(gridsz):
            row_coords = []
            for col in range(gridsz):
                row_coords.append((row, col))
                print(f"({row}, {col})", end=" ")
            grid.append(row_coords)
            print()  # Move to the next row
            
        return grid
    
    except ValueError:
        print("Please enter a valid integer for grid size")
        return None
    

draw_baseshape()  