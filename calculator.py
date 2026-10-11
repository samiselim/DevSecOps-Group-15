def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the difference of a and b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b, handling division by zero."""
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b

def power(a, b):
    """Return a raised to the power of b."""
    return a ** b


print("Addition:", add(10, 5))
print("Subtraction:", subtract(10, 5))
print("Multiplication:", multiply(10, 5))
print("Division:", divide(10, 5))
print("Power:", power(2, 3))