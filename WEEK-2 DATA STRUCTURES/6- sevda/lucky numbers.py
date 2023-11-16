# Finding Lucky Numbers Game

'''A list is created including the number entered by the user.At each step, the numbers in the 2nd, 3nd,4nd,...
rows are removed respectively and this continues until there are no more numbers left to remove.'''

number = int(input('Enter a number:'))
step = 1
number_list = [i for i in range(1,number+1) ]   #A list is created including the number entered by the user.
print(number_list)
n = 1    # Index from which we will delete numbers

#Using the for loop and the del function, numbers are removed from the list step bystep and lucky numbers are found

for i in number_list: 
    del number_list[n: :n+1] 
    step +=1                         
    n += 1
    print(number_list)

print('Lucky Numbers',number_list)    





