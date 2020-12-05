"""Day 3 exercise."""
from typing import List, Tuple

# Load file
in_file = open("data/day_3_input.txt", "r")
content = in_file.read()
terrain = content.split("\n")
in_file.close()

HEIGHT = len(terrain)
WIDTH = len(terrain[0])

def traverse(terrain: List, move_x: int, move_y: int) -> int:
    """Traverse the map in increments of x, y."""
    x = 0
    y = 0
    tree_count = 0
    
    while y < HEIGHT:
        if terrain[y][x % WIDTH] == '#':
            tree_count += 1
        x += move_x
        y += move_y
    return tree_count
