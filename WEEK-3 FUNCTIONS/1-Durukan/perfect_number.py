from functools import reduce


def perfect_number(num):
    # make a list from the dividers of num parameter
    dividers = [i for i in range(1, num) if num % i == 0]
    
    sum_of_num = sum(dividers) # sum of the dividers

    # check if the number is equal to the sum of the dividers
    # if it is equal return True, else False 
    return sum_of_num == num

    
# Make a list of numbers between 1 and 1000 with range(). Then use filter and lambda to check if the number is perfect or not.
perfect_numbers =  list(filter(lambda x: perfect_number(x), [i for i in range(1,1000)]))

# use reduce to calculate the sum of perfect numbers
sum_of_pn = reduce(lambda x,y: x+y, perfect_numbers) # sum of perfect numbers

print(sum_of_pn)

''' Kod cok guzel tebrik ederim..
Ayrica filter fonksiyonu içinde lambda yerine doğrudan perfect_number fonksiyonunu kullanabilirsiniz. '''

 
    
