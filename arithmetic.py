"""Math functions for calculator."""


def add(numbers):
    """Return the sum of the two inputs."""
    total = 0
    for number in numbers:
        total += number
    return total

print add([1, 2, 3])

def subtract(numbers):
    """Return the second number subtracted from the first."""

    total = numbers[0]
    for number in numbers[1:]:
        total -= number
    return total

print subtract([20, 4, 5])

def multiply(numbers):
    """Multiply the two inputs together."""

    total = numbers[0]
    for number in numbers[1:]:
        total *= number
    return total

print multiply([1, 2, 3])

def divide(numbers):
    """Divide the first input by the second and return the result."""

    total = numbers[0]
    for number in numbers[1:]:
        total /= number
    return total

print divide([10, 5, 2])

def square(numbers):
    """Return the square of the input."""

    if len(numbers) != 1:
        print "This operator only takes one number."
    return numbers[0] ** 2


def cube(numbers):
    """Return the cube of the input."""

    if len(numbers) != 1:
        print "This operator only takes one number."
    return numbers[0] ** 3


def power(numbers):
    """Raise num1 to the power of num2 and return the value."""

    total = numbers[0]
    for number in numbers[1:]:
        total = total ** number
    return total

print power([2, 3, 2])


def mod(numbers):
    """Return the remainder of num1 / num2."""

    if len(numbers) < 2:
        print "That is not a valid input. Try again with at least 2 numbers."
    else:
        total = numbers[0]
        for number in numbers[1:]:
            total = total % number
        return total

print mod([10, 6, 3])

def add_mult(numbers):
    """Adds the first two and multiples sum with third"""
    if len(numbers) < 3:
        print "That is not a valid input. Try again with three numbers."
    else:
        return (numbers[0] + numbers[1]) * numbers[2]

print add_mult([1])
print add_mult([1, 2, 3])

def add_cubes(numbers):
    """Cubes two numbers and returns the sum of the cubes"""

    total = 0
    for number in numbers:
        total += number ** 3
    return total

print add_cubes([1, 2, 3])