def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
def power(a, b):
    return a ** b

# Calling each function with sample values to match the expected output
print(f"Addition: {add(10, 5)}")
print(f"Subtraction: {subtract(10, 5)}")
print(f"Multiplication: {multiply(10, 5)}")
print(f"Division: {divide(10, 5)}")
print(f"Power: {power(2, 3)}")  # Should output 8