number = int(input('Enter a number: ')) 

lucky_numbers = []

for i in range(1,number+1):
    j=[]
    if number %i==0 :
        j.append(i)
        lucky_numbers.append(j)

print(lucky_numbers)