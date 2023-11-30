# Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
# The smallest perfect number is 6, which is the sum of 1, 2, and 3.
# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
# Write a function that finds perfect numbers between 1 and 1000. 
# Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

def perfect_numbers(pn):
   divisors = [i for i in range(1, pn) if pn % i == 0]
   return pn == sum(divisors)
numbers = list(filter(perfect_numbers, range(1, 1000)))
print("Perfect numbers are: ", numbers)

from functools import reduce
def sum_pn (x,y):
   return x+y
print(f"The sum of perfect numbers is: ", {reduce(sum_pn,numbers)})
