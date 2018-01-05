"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from original_arithmetic import *



while True:
    equation = raw_input("What do you want to calculate? (in prefix notation)")
    tokens = equation.split()
    
    operator = tokens[0]
    numbers = []

    for token in tokens[1:]:
        try:
            numbers.append(int(token))
        except:
            print "Please only use operators and numbers."
            break
    
    # print tokens
    if len(numbers) > 0:
        if operator == 'q':
            break
        elif operator == '+':
            print reduce(lambda x, y: add(x, y), numbers)
        elif operator == '-':
            print reduce(lambda x, y: subtract(x, y), numbers)
        elif operator == '*':
            print reduce(lambda x, y: multiply(x, y), numbers)
        elif operator == '/':
            print reduce(lambda x, y: divide(x, y), numbers)
        elif operator == 'square':
            print reduce(lambda x, y: square(x, y), numbers)
        elif operator == "cube":
            print reduce(lambda x, y: cube(x, y), numbers)
        elif operator == 'pow':
            print reduce(lambda x, y: power(x, y), numbers)
        elif operator == 'mod':
            print reduce(lambda x, y: mod(x, y), numbers)
        else:
            print 'The request was not valid.'


