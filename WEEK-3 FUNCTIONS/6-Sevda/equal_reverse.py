'''Write a function that controls the given inputs whether they are equal to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False'''

def pallidromes(list1) :
    '''This functions returns the words received from the user,'True' for words 
that are the same in reverse, and 'False'for words that are not the same.'''
    return list(map(lambda word : word == word[::-1],list1))
list1 = (input('enter words:')).split()
print(pallidromes(list1))