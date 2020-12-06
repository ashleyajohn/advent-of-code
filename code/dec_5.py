"""Day 5 exercise."""
from typing import Tuple

# Load file
in_file = open("day_5_input.txt", "r")
content = in_file.read()
seats = content.split("\n")
in_file.close()

def decode_seat(binary_name: str) -> Tuple[int, int]:
    """Decode binary format of seat into (row, col)."""
    rows = binary_name[0:7]
    cols = binary_name[7:10]
    row = int(rows.replace("F", "0").replace("B", "1"), 2)
    col = int(cols.replace("L", "0").replace("R", "1"), 2)
    return (row, col)

def calc_seat_id(location: Tuple) -> int:
    """Calculate the seat id."""
    return location[0] * 8 + location[1]
	
seat_ids = []

for item in seats:
    seat_ids.append(calc_seat_id(decode_seat(item)))

# get all possible seat ids, find missing
set(range(min(seat_ids), max(seat_ids))).difference(seat_ids)
