"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():
    should_continue = True
    while should_continue:
        equation = raw_input("What do you want to calculate? (in prefix notation)")
        tokens = equation.split(' ')
        for num in range(1, len(tokens)):
            tokens[num] = int(tokens[num])
        print tokens
        if tokens[0] == 'q':
            should_continue = False
        elif tokens[0] == '+':
            print add(tokens[1], tokens[2])
        elif tokens[0] == '-':
            print subtract(tokens[1], tokens[2])
        elif tokens[0] == '*':
            print multiply(tokens[1], tokens[2])
        elif tokens[0] == '/':
            print divide(tokens[1], tokens[2])
        elif tokens[0] == 'square':
            print square(tokens[1])
        elif tokens[0] == "cube":
            print cube(tokens[1])
        elif tokens[0] == 'pow':
            print power(tokens[1], tokens[2])
        elif tokens[0] == 'mod':
            print mod(tokens[1], tokens[2])

calculator()
