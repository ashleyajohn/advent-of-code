from copy import deepcopy
from typing import List

# Load file
in_file = open("data/day_19_input.txt", "r")
content = in_file.read()
data = content.split("\n")
in_file.close()

def parse_input(data: List) -> List:
    """Parse input data."""
    rules = {}
    for line in data:
        if not line:
            break

        rule_id, options = line.split(": ")
        if '"' in options:
            rule = options[1:-1]
        else:
            rule = []
            for option in options.split('|'):
                option = option.split()
                option = [int(i) for i in option]
                rule.append(tuple(option))
        rules[int(rule_id)] = rule
    return rules

def find_match(rules: dict, string: str, rule=0, index=0) -> List:
    if index == len(string):
        return []
    
    rule = rules[rule]
    if type(rule) is str:
        if string[index] == rule:
            return [index +1]
        return []
    
    matches = []
    for option in rule:
        sub_matches = [index]
        
        for sub_rule in option:
            new_matches = []
            for idx in sub_matches:
                new_matches += match(rules, string, sub_rule, idx)
            sub_matches = new_matches
        matches += sub_matches
    return matches 

rules = parse_input(data)
rules[8]  = [(42,), (42, 8)]
rules[11] = [(42, 31), (42, 11, 31)]