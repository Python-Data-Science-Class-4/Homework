import math

def calculation (x,y):
    if y != 0 :
        result = (x / y)
        result = math.ceil(result)
        return result
    elif y == 0 :
        result = "***UNDEFINED***"
        return result