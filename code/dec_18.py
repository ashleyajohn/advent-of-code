from re import findall
from collections import deque
from operator import add, mul
from functools import partial

# Load file
in_file = open("data/day_18_input.txt", "r")
content = in_file.read()
data = content.split("\n")
in_file.close()


def tokenize(expr):
    """Tokenize input."""
    return findall(r'\d+|[+*()]', expr)

def evaluate(tokens, plus_precedence=False):
    multiplier = 1
    accumulator = 0
    op = add

    while tokens:
        tok = tokens.popleft()

        if tok.isdigit():
            val = int(tok) * multiplier
            accumulator = op(accumulator, val)
        elif tok == '+':
            op = add
        elif tok == '*':
            if plus_precedence:
                multiplier  = accumulator
                accumulator = 0
            else:
                op = mul
        elif tok == '(':
            val = evaluate(tokens, plus_precedence) * multiplier
            accumulator = op(accumulator, val)
        else: # ')'
            break

    return accumulator



exprs = tuple(map(tokenize, data))

# part 1
total = sum(map(evaluate, map(deque, exprs)))

# part 2
total = sum(map(partial(evaluate, plus_precedence=True), map(deque, exprs)))