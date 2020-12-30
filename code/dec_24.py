with open("data/day_24_input.txt") as file:
    challenge_positions = parse_input(file.read())

DIRECTIONS = {
    "e": 1+0j,
    "se": 0+1j,
    "sw": -1+1j,
    "w": -1+0j,
    "nw": 0-1j,
    "ne": 1-1j
}


def parse_input(input_txt):
    positions = []
    for line in input_txt.splitlines():
        position = 0
        line = list(reversed(line))
        while line:
            direction = line.pop()
            if direction not in "ew":
                direction += line.pop()
            position += DIRECTIONS[direction]
        positions.append(position)
    return positions


def part_1(positions):
    hexmap = set()
    for position in positions:
        hexmap.symmetric_difference_update({position})
    return len(hexmap), hexmap


def check_neighbors(position, old_state, new_state,
                    candidates=None):
    neighbor_positions = {position + direction for direction in DIRECTIONS.values()}
    n_neighbors = len(neighbor_positions & old_state)
    active = position in old_state
    if active and n_neighbors in {1, 2} or not active and n_neighbors == 2:
        new_state.add(position)
    if candidates is not None:
        candidates.update(neighbor_positions)


def part_2(hexmap):
    # hexmap stores only the black tiles as a set.
    for _ in range(100):
        new_hexmap = set()
        candidates = set()
        for position in hexmap:
            check_neighbors(position, hexmap, new_hexmap, candidates)
        # Check the neighbors of the active cells:
        for position in candidates:
            check_neighbors(position, hexmap, new_hexmap)
        hexmap = new_hexmap
    return len(hexmap)
