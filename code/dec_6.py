"""Day 6 exercise."""
from collections import Counter
from typing import List

# Load file
in_file = open("data/day_6_input.txt", "r")
content = in_file.read()
groups = content.split("\n\n")
in_file.close()

def count_any_yes(groups: List) -> int:
    """Count questions that have any 'yes' answers."""
    yes = []
    for group in groups:
        questions = group.split("\n")
        answers = set()
        for question in questions:
            answers.update(question)
        yes.append(len(answers))
    return sum(yes)
	
def count_all_yes(groups: List) -> int:
    """Count questions that have all 'yes' answers."""
    yes = []
    for group in groups:
        counts = (Counter(group))
        answers = []
        for item in counts:
            if counts[item] == counts['\n'] + 1:
                answers.append(item)
        yes.append(len(answers))
    return (sum(yes))