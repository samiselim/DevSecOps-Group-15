def add(a, b) :
    return a + b

def subtract(a, b) :
    return a - b

def multiply(a, b) :
    return a * b

def divide(a, b) :
    if b == 0:
        b = int(input("Please enter a non-zero value for b: "))
    return a / b
def power(a, b) :
    return a ** b

print("Addition of 2 and 3 is: ", add(2, 3))
print("Subtraction of 5 and 3 is: ", subtract(5, 3))
print("Multiplication of 4 and 3 is: ", multiply(4, 3))
print("Division of 10 and 2 is: ", divide(10, 2))
print("Power of 2 and 3 is: ", power(2, 3))