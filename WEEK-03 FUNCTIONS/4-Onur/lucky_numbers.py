from functools import reduce
def my_add(x,y):
    return x + y

def is_perfect(number):
    dividers = list(filter(lambda x: (number % x == 0),range(1,number)))
    sum_of_dividers = reduce(my_add, dividers)
    if number == sum_of_dividers:
        return True
    else:
        return False

perfect_numbers = []

for x in range(2,1001):
    if is_perfect(x) == True:
        print(x)
        perfect_numbers.append(x)

print(f"Sum of Perfect Numbers until 1000 is {reduce(my_add,perfect_numbers)}")