def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

if __name__ == "__main__":
    print(f"Addition: {add(10, 5)}")
    print(f"Subtraction: {subtract(10, 5)}")
    print(f"Multiplication: {multiply(10, 5)}")
    print(f"Division: {divide(10, 5)}")
    print(f"Power: {power(10, 5)}")