def divide(a, b):
    """Calculates division of 2 numbers"""
    if b == 0:
        raise ValueError("Cannot be divided by zero.")
    result = a / b
    return round(result, 2)