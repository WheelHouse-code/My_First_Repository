#Learning to Create a Python Library
def add(x, y):
    """Addition of two numbers."""
    return x + y

def subtract(x, y):
    """Subtraction of two numbers."""
    return x - y

def multiply(x, y):
    """Multiplication of two numbers."""
    return x * y

def divide(x, y):
    """Division of two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y
