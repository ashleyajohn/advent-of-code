from math import sin, cos, radians

# Load file
in_file = open("data/day_12_input.txt", "r")
content = in_file.read()
moves = content.split("\n")
in_file.close()

ORIENTATION_MAP = {'N': (0, 1), 'S': (0, -1), 'W': (-1, 0), 'E': (1, 0)}

# Part 1 
x = 0
y = 0 
orientation = 90

for move in moves:
    action, distance = move[0], int(move[1:])
    if action in ORIENTATION_MAP:
            x_dir, y_dir = ORIENTATION_MAP[action]
            x += distance * x_dir
            y += distance * y_dir
    if action in ['L', 'R']: 
        orientation += (distance if action == 'R' else 360 - distance)
        orientation % 360
    elif action == 'F':
        theta = radians(orientation)
        y += int(cos(theta) * distance)
        x += int(sin(theta) * distance)
print(f'Part 1: {abs(x) + abs(y)}')


# Part 2
x, y = 0, 0
x_way, y_way = 10, 1

for move in moves:
    action, distance = move[0], int(move[1:])
    if action in ORIENTATION_MAP:
        x_dir, y_dir = ORIENTATION_MAP[action]
        x_way += distance * x_dir
        y_way += distance * y_dir
    elif action in {'L', 'R'}:
        rotation = (distance if action == 'R' else 360 - distance)
        if rotation == 90 or rotation == 270:
            tmp = y_way
            y_way = x_way * (-1 if rotation == 90 else 1)
            x_way = tmp * (1 if rotation == 90 else -1)
        elif rotation == 180:
            x_way *= -1
            y_way *= -1
    elif action == 'F':
        x += distance * x_way
        y += distance * y_way

print(f'Part 2: {abs(x) + abs(y)}')