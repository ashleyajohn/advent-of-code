from math import ceil
from typing import List, Tuple

# Load file
in_file = open("data/day_13_input.txt", "r")
content = in_file.read()
input_file = content.split("\n")
in_file.close()

timestamp = int(input_file[0])
buses = input_file[1]
buses = buses.split(',')
buses = [int(b) for b in buses if b != 'x']

bus_offsets = [[int(buses[k]), k] for k in range(len(buses)) if buses[k] != 'x']

def find_soonest_bus(buses: List[int], timestamp: int) -> int:
    """Find the soonest bus to come and the product of that ID and wait time."""
    next_bus = []
    for b in buses:
        next_bus.append(ceil(timestamp / b) * b)
    idx = next_bus.index(min(next_bus))
    soonest = buses[idx] * (next_bus[idx] - timestamp)
    return soonest

def find_offset(offsets: List) -> int:
    """Find timestamp of offset pattern."""
    lcm = 1
    time = 0    
    for i in range(len(offsets)-1):
        bus_id = offsets[i+1][0]
        idx = offsets[i+1][1]
        lcm *= offsets[i][0]
        while (time + idx) % bus_id != 0:
            time += lcm
    return time