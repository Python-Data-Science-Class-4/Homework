'''Perfect number: Perfect number is a positive 
integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the
perfect numbers using reduce and filter functions.'''
from functools import reduce

def perfect_numbers(n):
    '''This fuction calculates the sum of the divisors of an entered number.'''
    sum1 = 0
    for i in range(1,n) :
        if n % i == 0 :
            sum1 +=i
            
    return sum1 == n   

result = list(filter(perfect_numbers,range(1,1000)))
'''Perfect_numbers between 1 and 1000 are found with the 'filter' funcition.'''
print(result)

def sum_fuc(x,y):
    '''This function performs addition.'''
    return x+y
result_1 = reduce(sum_fuc,result)
# We add perfect numbers with reduce.
print(result_1)
