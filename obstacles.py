import random
obstacles = []

def create_random_obstacles():
    obstacles.clear()
    for _ in range(random.randint(0, 10)):
        x = random.randint(-100, 100)
        y = random.randint(-200, 200)
        obstacles.append((x, y))
    return obstacles

def is_position_blocked(x, y):
    for obstacle in obstacles:
        if obstacle[0] <= x <= obstacle[0] + 4 and obstacle[1] <= y <= obstacle[1] + 4:
            return True
    return False

def is_path_blocked(x1, y1, x2, y2):
    if y1 == y2:
        for x in range(min(x1, x2), max(x1, x2) + 1):
            if is_position_blocked(x, y1):
                return True
    else: 
        for y in range(min(y1, y2), max(y1, y2) + 1):
            if is_position_blocked(x1, y):
                return True
    return False

def get_obstacles():
    return obstacles
