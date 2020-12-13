"""Day 9 exercise."""
import itertools
from typing import List, Tuple, Union

# Load file
in_file = open("data/day_9_input.txt", "r")
content = in_file.read()
numbers = content.split("\n")
numbers = [ int(x) for x in numbers ]
in_file.close()

def get_all_groups(input_list: List, batch_size: int) -> List[Tuple]:
    """Get all possible pairs in a list."""
    return list(itertools.combinations(input_list, batch_size))

def find_sum_group(group_list: List[Tuple], target: int) -> Tuple:
    """Find the pair in the list that sums to the target."""
    for item in group_list:
        if sum(item) == target:
            return item
			
def find_bad_number(numbers) -> Union[int, bool]:
    """Find bad number in the list."""
    segment = numbers[:25]
    i = 1
    for number in numbers[25:]:
        groups = get_all_groups(segment, 2)
        if not find_sum_group(groups, number): 
            return number
        else:
            segment = numbers[i:25+i]
            i += 1
    return False

def find_contiguous(numbers, target) -> Union[int, bool]:
    for group in range(2, len(numbers)):
        segment = numbers[:group]
        i = 1
        while i < len(numbers)-group:
            if sum(segment) == target:
                return segment
            i += 1
            segment = numbers[i:group+i]

    return False