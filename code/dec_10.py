from collections import Counter
from typing import List

# Load file
in_file = open("data/day_10_input.txt", "r")
content = in_file.read()
jolts = content.split("\n")
jolts = [ int(x) for x in jolts ]
in_file.close()

jolts = sorted(jolts) 

# add max 
jolts.append(jolts[-1] + 3)

# add outlet
jolts.append(0)

jolts = sorted(jolts)

def get_jolt_diffs(jolts: List[int]) -> dict:
    """Get list of joltage differences."""
    diffs = [jolts[i]-jolts[i-1] for i in range(1,len(jolts))]
    print (diffs)
    counts = dict(Counter(diffs))
    return counts
	
def get_possible_paths(jolts: List[int]) -> int:
    record = {0: 1}
    jolts.pop(0)
    for i in jolts:
        record[i] = record.get(i-3,0) + record.get(i-2,0) + record.get(i-1,0)
    return memo[arr[-1]]