"""Day 8 exercise."""
import re
from typing import Dict, List

# Load file
in_file = open("data/day_8_input.txt", "r")
content = in_file.read()
steps = content.split("\n")
in_file.close()

def find_step(steps: List) -> bool:
    accumulator = 0
    position = 0 
    step_list = []

    while True:
        increment = steps[position].split(' ')[1]
        action = steps[position][:3]
        if action == 'acc':
            accumulator += int(increment)
            position += 1
        elif action == 'jmp':
            position = position + int(increment)
        elif action == 'nop':
            position += 1
        if position in step_list:
            print(f'Found the Loop! Accumulation equals {accumulator}')
            return False
        else:
            step_list.append(position)
			
def fix_steps(steps: List) -> bool: 
    accumulator = 0 
    position = 0 
    tryalt = False
    step_list = []
    alt_steps = []
    copymoves = []
    
    while position <= len(steps) -1:
        increment = steps[position].split(' ')[1]
        action = steps[position][:3]
        if action == 'acc': 
            accumulator += int(increment)
            position += 1
        elif action == 'jmp':
            if tryalt != True and position not in alt_steps: 
                copymoves = step_list.copy()
                alt_steps.append(position)
                tempaccel = accumulator
                position += 1
                tryalt = True
            else:
                position = position + int(increment)
        elif action == 'nop':
            if tryalt != True and position not in alt_steps: 
                copymoves = step_list.copy()
                alt_steps.append(position)
                tempaccel = accumulator
                position = position + int(increment)
                tryalt = True
            else: 
                position += 1
        if position in step_list:
            position = alt_steps[-1]
            step_list = copymoves
            accumulator = tempaccel
            tryalt = False     
        else:
            step_list.append(position)
        
    print(f'Reached the end! Accumulation equals {accumulator}')
