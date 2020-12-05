"""Day 2 exercise."""
from typing import List, Tuple

# Load file
in_file = open("data/day_2_input.txt", "r")
content = in_file.read()
terrain = content.split("\n")
in_file.close()

def parse_input_passwords(passwords: list) -> List[Tuple]:
    """Parse password input.
    
    Parse password rule from sample password. 
    Example: input of 2-3 r: jrfrvrk is returned
    as ('2-3 r', 'jrfrvrk')
    """
    parsed_passwords = []
    for item in passwords:
        rule, password = item.split(':')
        parsed_passwords.append((rule, password))
    return parsed_passwords

def check_valid_password_count(rule: str, password: str) -> bool:
    """Check if a password is valid according to its rule based on char count."""
    count_range, letter = rule.split(' ')
    min_count = int(count_range.split('-')[0])
    max_count = int(count_range.split('-')[1])
    return min_count <= password.count(letter) <= max_count

def check_valid_password_position(rule: str, password: str) -> bool:
    """Check if a password is valid according to its rule based on char position."""
    count_range, letter = rule.split(' ')
    pos_a = int(count_range.split('-')[0])
    pos_b = int(count_range.split('-')[1])
    if sum((password[pos_a] == letter, password[pos_b] == letter)) == 1:
        return True
    return False
