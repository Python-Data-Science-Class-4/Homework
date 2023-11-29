######################## 4- perfect_number ############

def perfect_nums(number):
    sum=0
    for i in range(1,number):
        if number%i == 0:
            sum+=i
    return sum == number

for x in range(1,1000):
    if perfect_nums(x):
        print("perfect number: ", x)