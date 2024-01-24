import math     #The "math" module is called.

def calculation (x,y):
    result = (x + y)
    result = math.ceil(result)  #If the addition result is a fraction, it is rounded up to the next number.
    return result  