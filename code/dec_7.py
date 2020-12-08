"""Day 7 exercise."""
from typing import Dict, List

# Load file
in_file = open("data/day_7_input.txt", "r")
content = in_file.read()
bags = content.split("\n")
in_file.close()

expanded_bags = {}

for line in bags:
    line = line.replace("bags", "").replace("bag", "").strip(".")
    line = line.split("contain")
    expanded_bags[line[0].strip()] = line[1].strip().split(',')


def find_bag(bags: List, target: str) -> List:
    """Find all bags that hold a certain type of bag."""
    accepting_bags = []
    for item in bags:
        idx = item.find(' bags contain')
        if target in item[idx:]:
            accepting_bags.append(item[:idx])
            accepting_bags.extend(find_bag(bags, item[:idx]))
    return accepting_bags

def sum_all_bags(bags: Dict) -> int:
    """Sum all bags that hold a certain type of bag."""
    total = 1
    if "no other" in expanded_bags[bags]:
        return 1
    for item in expanded_bags[bags]:
        each = item.split()
        total += int(each[0]) * sum_all_bags(" ".join(each[1:]))
    return total
