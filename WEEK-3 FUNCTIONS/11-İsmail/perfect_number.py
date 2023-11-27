# #Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.

# The smallest perfect number is 6, which is the sum of 1, 2, and 3.

# Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.

# Write a function that finds perfect numbers between 1 and 1000. 

# Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.

from functools import reduce

def perfect_numbers (n): # Create funciton which is firstly creating a list with "append".
    sum_1=0
    perf_num=[]
    for i in range(1,n): 
        if n % i == 0:
            sum_1+=i # If sum of the numbers "that is the first if block" (called sum_1)equals all of the i variables,
            if sum_1==n:
                perf_num.append(i) #Create a list which is name perf_num.
    return perf_num

result = list(filter(perfect_numbers,range(1,1000))) #Filter the perfect number until 1000, then convert this a list. 

print(result)  

def sum_perf(x,y):

    return x+y
result_1 = reduce(sum_perf,result)

print(result_1)