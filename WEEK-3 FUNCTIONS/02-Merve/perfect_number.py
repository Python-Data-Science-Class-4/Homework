'''
Perfect number: Perfect number is a positive integer that is equal to the sum of its proper divisors.
The smallest perfect number is 6, which is the sum of 1, 2, and 3.
Some other perfect numbers are 28(1+2+4+7+14=28), 496 and 8128.
Write a function that finds perfect numbers between 1 and 1000. 
Check perfect numbers between 1 and 1000 and find the sum of the perfect numbers using reduce 
and filter functions.
'''

from functools import reduce

def perfect_number(sayi):
    k=0
    for i in range(1,sayi):
        if sayi%i==0:
            k+=i
    if sayi==k:
        return sayi

number=[x for x in range(1,1001)]

listem=list(filter(perfect_number, number))
liste_toplam=reduce(lambda a,b: a+b, listem)

print(listem)
print(liste_toplam)




# from functools import reduce
# l = [1, 2, 3, 4, 5, 6]
# sonuc = reduce((lambda x, y: x * y), l)
# print(sonuc)
