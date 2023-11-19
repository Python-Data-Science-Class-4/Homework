'''
@description
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.

Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000. Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce and filter functions.
'''
from functools import reduce

def createList(value):
    #skip 1, because smallest perfect numbers start first with 6
    return [i+1 for i in range(value)]

def findPerfectNumber(value : list) -> list:
    #create prefect number list
    perfectNumList=[]
    #control each number of the list if that is perfect number
    for i in value:
        #start with 1 as a divisor ande create one list to save the number that divide the element of the list
        divisor = 1
        divisorList=[]
        while divisor<i:
            #check that if number is prober divisors. if yes, save that value in divisorList
            if i%divisor==0:
                divisorList.append(divisor)
            divisor+=1
        #in the end control that the number is equal to the sum of its proper divisors 
        if len(divisorList)!=0 and i == reduce(lambda x,y : x+y, divisorList):
            perfectNumList.append(i)
    return perfectNumList

print(f"The Lucky Numbers are : {findPerfectNumber(createList(int(input('Plese type a number : '))))}")
            


