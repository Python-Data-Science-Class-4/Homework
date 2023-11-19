
#Write a function that filters all the unique(unrepeated) elements of a given list.

# numbers = [1,2,3,3,3,3,4,5,5]
# numbers_2 = list (set(numbers))
# print (numbers_2)

def unique_list (team):    
    numbers_2 =[]
    for i in team:
        if i not in numbers_2:
            numbers_2.append(i)
        else:
            pass
    
    print (numbers_2)
    
numbers = [1,2,3,3,3,3,4,5,5] 
unique_list(numbers)
