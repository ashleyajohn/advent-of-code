"""Day 4 exercise."""
import re
from typing import List, Tuple

REQ_FIELDS = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])

# Load file
in_file = open("day_4_input.txt", "r")
content = in_file.read()
passports = content.split("\n\n")
in_file.close()

passports = [re.split('\n| ',passport) for passport in passports]

def passport_to_dict(passport: List) -> dict:
    """Transform a list of passport data into a dict."""
    passport_dict = {}
    for item in passport:
        k, v = item.split(':')
        passport_dict[k] = v
    return passport_dict
	
def fields_present(passport: dict) -> bool:
    """Check if required passport fields are present."""
    if set(passport.keys()).issuperset(REQ_FIELDS):
        return True
    return False
	
def validate_height(height: str) -> bool:
    """Validate height."""
    if height[-2:] == "in" and 59 <= int(height[:-2:]) <= 76:
        return True
    elif height[-2:] == "cm" and 150 <= int(height[:-2:]) <= 193:
        return True
    else:
        return False

def fields_valid_passport(passport: dict) -> bool:
    """Check if required passport fields have valid values."""
    if not 1920 <= int(passport['byr']) <= 2002:
        return False
    if not 2010 <= int(passport['iyr']) <= 2020:
        return False
    if not 2020 <= int(passport['eyr']) <= 2030:
        return False
    if not passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if not len(passport['pid']) == 9:
        return False
    if not re.match("#[0-9a-f]{6}", passport['hcl']):
        return False
    if not validate_height(passport['hgt']):
        return False
    return True

valid_passports = 0

for passport in passports:
    if fields_present(passport_to_dict(passport)):
        valid_passports += fields_valid_passport(passport_to_dict(passport))
