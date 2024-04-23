'''
@description
Write a function that controls the given inputs whether they are equal to their reversed order or not.

Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False
'''
# take a string value by user
value = input('please write a string value to check if string is equal of reversed wroten order ')

# check that with a func
def controlReversedOrder(value):
     if value == value[::-1]:
          return True
     return False

print(controlReversedOrder(value))
     