import math

def multiply(x, y):
    try:
        result = x * y
        return math.ceil(result)
    except Exception as e:
        print("An error occurred:", e)