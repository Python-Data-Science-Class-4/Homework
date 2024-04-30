from math import ceil
def divis(a,b) :
    '''Divides the first of the two entered numbers by the second. returns the result as float.
    If the divisor is zero, it warns the user.'''
    try:
        result = ceil(a/b)
        print(f'result:{result}')
            
    except ZeroDivisionError :
       print( 'Please enter a number other than "0"')
        
    
    