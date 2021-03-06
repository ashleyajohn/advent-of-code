"""Day 1 exercise."""
import itertools
from typing import List, Tuple

# Load file
in_file = open("data/day_1_input.txt", "r")
content = in_file.read()
input_list = content.split("\n")
in_file.close()

def get_all_groups(input_list: List, batch_size: int) -> List[Tuple]:
    """Get all possible pairs in a list."""
    return list(itertools.combinations(input_list, batch_size))

def find_sum_group(group_list: List[Tuple], target: int) -> Tuple:
    """Find the pair in the list that sums to the target."""
    for item in group_list:
        if sum(item) == target:
            return item
