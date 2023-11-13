# Assignment 1

# Printing prime numbers

input_num=int(input("Please submit a number  "))

if input_num < 1:
    print("Enter a number bigger than 1")

else:
    for i in range(2,input_num+1):
        for j in range(2,i):
            if (i % j) == 0:
                break
        else: 
            print(i)