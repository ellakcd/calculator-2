"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *



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
            print add(numbers)
        elif operator == '-':
            print subtract(numbers)
        elif operator == '*':
            print multiply(numbers)
        elif operator == '/':
            print divide(numbers)
        elif operator == 'square':
            print square(numbers)
        elif operator == "cube":
            print cube(numbers)
        elif operator == 'pow':
            print power(numbers)
        elif operator == 'mod':
            print mod(numbers)
        else:
            print 'The request was not valid.'


