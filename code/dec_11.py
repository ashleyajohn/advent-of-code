from collections import Counter
from typing import List, Counter, Tuple
from copy import deepcopy

# Load file
seats = []
with open('data/day_11_input.txt') as fp:
    line = fp.readline()
    while line:
        seats.append(list(line.strip()))
        line = fp.readline()
		
def get_neighbors(grid: List[str], x: int, y: int) -> Counter:
    neighbors = []
    row_length, col_length = len(grid[0]), len(grid)
    
    if x > 0: # if we are not in the top row
        neighbors.append(grid[x-1][y]) # add left
        if y > 0: # if we are not in the first column
            neighbors.append(grid[x-1][y-1]) # add down/left diagonal
        if y < row_length - 1: # if we are not in the last column
            neighbors.append(grid[x-1][y+1]) # add down/right diagonal
    if x < col_length - 1: # if we are not in the last row
        neighbors.append(grid[x+1][y]) # add right 
        if y > 0: # if we are not in the first column
            neighbors.append(grid[x+1][y-1]) # add up/left diagonal
        if y < row_length - 1: # if we are not in the last column
            neighbors.append(grid[x+1][y+1]) # add up/right diagonal
    if y > 0: # if we are not in the first column
        neighbors.append(grid[x][y-1]) # add down
    if y < row_length - 1: # if we are not in the last column
        neighbors.append(grid[x][y+1]) # add up
    return Counter(neighbors)
	
def find_steady_state_pt1(seats: List[str]) -> Tuple[int, bool]:
    new_seats = deepcopy(seats)
    change = False    
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]
            count_occ = get_neighbors(seats, row, col)['#']
            if seat == 'L' and count_occ == 0:
                new_seats[row][col] = '#'
                change = True
            elif seat == '#' and count_occ >= 4:
                new_seats[row][col] = 'L'
                change = True
    return new_seats, change

def count_occupied(seats: List[int]) -> int:
    count = 0
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            if seats[row][col] == '#':
                count += 1
    return count

def get_visible_seats(seats: List[str], x: int, y: int) -> int:
    count = 0
    shifts = [
        (-1, -1), (-1, 0), (-1, 1),
        (0,  -1),          (0,  1),
        (1,  -1), (1,  0), (1, 1)
    ]
    
    for (move_x, move_y) in shifts:
        new_x, new_y = (x+move_x, y+move_y)
        while (0 <= new_x <= (len(seats) - 1)) and (0 <= new_y <= (len(seats[0]) - 1)): # when x not in first or last
            if seats[new_x][new_y] == 'L': # new spot empty
                break
            if seats[new_x][new_y] == '#': # new spot filled
                count += 1
                break
            new_x, new_y = (new_x+move_x, new_y+move_y)
    return count
	
def find_steady_state_pt2(seats: List[str]) -> Tuple[int, bool]:
    new_seats = deepcopy(seats)
    change = False    
    for row in range(len(seats)):
        for col in range(len(seats[row])):
            seat = seats[row][col]
            count_occ = get_visible_seats(seats, row, col)
            if seat == 'L' and count_occ == 0:
                new_seats[row][col] = '#'
                change = True
            elif seat == '#' and count_occ >= 5:
                new_seats[row][col] = 'L'
                change = True
    return new_seats, change


# part 1
step = 0
current_seats = deepcopy(seats)

while step < 100:
    current_seats, change = find_steady_state_pt1(current_seats)
    if change == False:
        print(count_occupied(current_seats))
        break
    step += 1
	
# part 2

step = 0
current_seats = deepcopy(seats)

while step < 100:
    current_seats, change = find_steady_state_pt2(current_seats)
    if change == False:
        print(count_occupied(current_seats))
        break
    step += 1