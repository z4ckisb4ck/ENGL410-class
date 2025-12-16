"""
Simple Calculator Module
Provides basic arithmetic operations: addition, subtraction, multiplication, 
division, power (exponentiation), and modulo (remainder).
"""


def add(a, b):
    """
    Add two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract second number from first number.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Difference of a and b
    """
    return a - b


def multiply(a, b):
    """
    Multiply two numbers.
    
    Args:
        a (float): First number
        b (float): Second number
    
    Returns:
        float: Product of a and b
    """
    return a * b


def divide(a, b):
    """
    Divide first number by second number.
    
    Args:
        a (float): Numerator
        b (float): Denominator
    
    Returns:
        float: Quotient of a and b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """
    Raise first number to the power of second number.
    
    Args:
        a (float): Base
        b (float): Exponent
    
    Returns:
        float: a raised to the power of b
    """
    return a ** b


def modulo(a, b):
    """
    Calculate the remainder of division.
    
    Args:
        a (float): Dividend
        b (float): Divisor
    
    Returns:
        float: Remainder of a divided by b
    
    Raises:
        ValueError: If b is zero
    """
    if b == 0:
        raise ValueError("Cannot calculate modulo with zero divisor")
    return a % b
