from functools import reduce

def number_control(number):
    divisionlist = []
    for i in range(1, number):
        if number % i == 0:
            divisionlist.append(i)
    if number == sum(divisionlist):
        return True
    else:
        return False
    
    
numbers = list(range(1, 1001))

# i have found the perfect numbers using filter function.
perfect_nums = list(filter(lambda x: number_control(x), numbers))

# to sum the perfect numbers, i used reduce funstion.
sum_of_per_nums = reduce(lambda x, y: x + y, perfect_nums, 0)


print("Perfect numbers :", perfect_nums)
print("Sum of perfect numbers:", sum_of_per_nums)
