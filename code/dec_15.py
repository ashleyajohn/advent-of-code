from typing import List

puzzle_input = [16,12,1,0,15,7,11]

def play_game(puzzle_input: List, max_rounds: int) -> int:
    """Play the elf game."""
    count = 1
    short_term  = {}
    long_term = {}

    while count <= max_rounds:
        if count <= len(puzzle_input):
            num = puzzle_input[count-1]
            short_term[num] = count
        else:
            if num in long_term:
                num = short_term[num] - long_term[num]
                if num in short_term:
                    long_term[num] = short_term[num]
                    short_term[num] = count
                else:
                    short_term[num] = count
            else:
                num = 0 
                if num in short_term:
                    long_term[num] = short_term[num]
                    short_term[num] = count
                else:
                    short_term[num] = count
        count += 1
    return num