
# New Method For Generating Lucky Numbers

numbers = list (range (1,25))
print (numbers)

# del numbers [1::2] # n1
# del numbers [2::3] # n2
# del numbers [3::4] # n3
# del numbers [4::5] # n4
# print (numbers)

next = 2
while next<=len(numbers):
    new = [numbers[x-1] for x in range(1,len(numbers)+1) if x % next != 0]
    print(f""" Lucky list is {new}""")
    numbers = new
    next += 1
            

