def add_shell(space: dict) -> dict:
    """Add shell."""
    X, Y, Z, W = zip(*space.keys())
    x1, x2 = min(X), max(X)
    y1, y2 = min(Y), max(Y)
    z1, z2 = min(Z), max(Z)
    w1, w2 = min(W), max(W)
    for j in range(x1 - 1, x2 + 2):
        for i in range(y1 - 1, y2 + 2):
            for k in range(z1 - 1, z2 + 2):
                for l in range(w1 - 1, w2 + 2):
                    coord = (j, i, k, l)
                    if coord not in space:
                        space[coord] = "."


def get_neighbors_3d(x: int, y: int, z: int, w: int) -> bool:
    """Get 3d neighbors."""
    return [
        (j, i, k, l)
        for j in range(x-1, x+2)
        for i in range(y-1, y+2)
        for k in range(z-1, z+2)
        for l in range(w-1, w+2)
        if j != x or i != y or k != z or l != w
    ]

def get_neighbors_4d(x: int, y: int, z: int) -> bool:
    """Get 4d neighbors."""
    return [
        (j, i, k)
        for j in range(x-1, x+2)
        for i in range(y-1, y+2)
        for k in range(z-1, z+2)
        if j != x or i != y or k != z
    ]


def next_state(space: dict, dim: int) -> dict:
    """Create next space"""
    new_space = dict()
    add_shell(space)
    for coord, value in space.items():
        active_neighbors = 0
        if dim == 3:
            for n_coords in get_neighbors_3d(*coord):
                if space.get(n_coords, ".") == "#":
                    active_neighbors += 1
        elif dim == 4:
            for n_coords in get_neighbors_4d(*coord):
                if space.get(n_coords, ".") == "#":
                    active_neighbors += 1
        if (value == "#" and 2 <= active_neighbors <= 3
            or value == "." and active_neighbors == 3):
            new_value = "#"
        else:
            new_value = "."
        new_space[coord] = new_value
    return new_space