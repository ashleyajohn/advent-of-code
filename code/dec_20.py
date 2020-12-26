r = open('data/day_20_input.txt').read()
input = r.split('\n\n')
input = input[:-1]

def process_tiles(raw):
    lines = raw.splitlines()
    id = int(lines[0][5:-1])
    data = lines[1:]
    return [id,data]

data = [process_tiles(raw) for raw in input]

def get_edges(data):
    edges = [data[0],data[-1][::-1]]
    left = ''
    right = ''
    for line in data:
        left = line[0] + left
        right = right + line[-1]
    edges = edges + [left, right]
    return edges

edge_data = {}
matches = {}

for tile in data:
    id = tile[0]
    matches[id] = 0
    edges = get_edges(tile[1])
    for edge in edges:
        other = None
        if edge in edge_data:
            other = edge_data[edge]
        else:
            reverse = edge[::-1]
            if reverse in edge_data:
                other = edge_data[reverse]
                edge = reverse
        if other is not None:
            matches[other] = matches[other] + 1
            matches[id] = matches[id] + 1
            edge_data[edge] = [other,id]
        else:
            edge_data[edge] = id

acc = 1
corners = []
for id in matches:
    if matches[id] == 2:
        corners.append(id)
        acc = acc * id


def flip(data):
    output = []
    for row in data:
        output.append(row[::-1])
    return output

def rotate(data):
    output = ['']*len(data[0])
    for row in data:
        for i in range(len(row)):
            output[i] = row[i] + output[i]
    return output

def permutate(data,i):
    if i > 3:
        i = i - 4
        data = flip(data)
    while i > 0:
        i = i - 1
        data = rotate(data)
    return data

database = {}
for tile in data:
    database[tile[0]] = tile[1]

def get_neighbor(id,side):
    tile = database[id]
    edges = get_edges(tile)
    edge = edges[side]
    if edge not in edge_data:
        edge = edge[::-1]
    neighbour = edge_data[edge]
    if neighbour == id:
        return None
    elif neighbour[0] == id:
        return neighbour[1]
    else:
        return neighbour[0]

up,down,left,right = 0,1,2,3

seed = corners[0]
for i in range(4):
    database[seed] = permutate(database[seed],1)
    if get_neighbor(seed,up) == get_neighbor(seed,left) == None:
        break

grid = [seed]
seed = get_neighbor(seed,right)
while(seed is not None):
    original_tile = database[seed]
    for i in range(8):
        database[seed] = permutate(original_tile,i)
        if get_neighbor(seed,up) is None and get_neighbor(seed,left) is grid[-1]:
            grid.append(seed)
            seed = get_neighbor(seed,right)
            break

grid = [grid]
while len(grid) == 1 or grid[-1][-1] not in corners:
    grid.append([])
    prev = None
    seed = get_neighbor(grid[-2][0],down)
    col = 0
    while True:
        original_tile = database[seed]
        for i in range(8):
            database[seed] = permutate(original_tile,i)
            if get_neighbor(seed,up) is grid[-2][col] and get_neighbor(seed,left) is prev:
                grid[-1].append(seed)
                prev = seed
                seed = get_neighbor(seed,right)
                break
        col = col + 1
        if seed is None:
            break

def center(tile):
    tile = tile[1:-1]
    for i in range(len(tile)):
        tile[i] = tile[i][1:-1]
    return tile

pic = []
for row in grid:
    scanline = None
    for i in range(len(row)):
        id = row[i]
        tile = database[id]
        tile = center(tile)#Remove to check for edge alignment
        if i == 0:
            scanline = tile
        else:
            for subrow in range(len(scanline)):
                scanline[subrow] = scanline[subrow] + tile[subrow]
    pic = pic + scanline

def dragon_check(pic,row,col,dragon):
    dragonHeight = len(dragon)
    dragonLength = len(dragon[0])
    height = len(pic)
    length = len(pic[0])
    if dragonHeight + row > height or dragonLength + col > length:
        return None
    for y in range(dragonHeight):
        for x in range(dragonLength):
            if dragon[y][x] == '#' and pic[row+y][col+x] == '.':
                return False
    return True

dragon = ['                  # ','#    ##    ##    ###',' #  #  #  #  #  #   ']
dragon_size = 0
for row in dragon:
    dragon_size = dragon_size + row.count('#')

waves = 0
for row in pic:
    waves = waves + row.count('#')

for i in range(8):
    new_pic = permutate(pic,i)
    dragon_count = 0
    row = 0
    col = 0
    while True:
        result = dragon_check(new_pic,row,col,dragon)
        if result is None:
            if col != 0:
                col = 0
                row = row + 1
            else:
                break
        else:
            if result is True:
                dragon_count = dragon_count + 1
            col = col + 1
    if dragon_count > 0:
        break