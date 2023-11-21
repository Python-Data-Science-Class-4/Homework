
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

''' Kod gayet guzel.
Ama set() kullanarak benzersiz elemanları alıp ve daha sonra bu seti de bir listeye dönüştürerek 
benzersiz elemanları içeren bir liste elde edebilirsiniz.Asagidaki ornegi inceleyebilirsiniz.

def remove_duplicates(lst):
    unique_list = list(set(lst))
    print(unique_list)

numbers = [1, 2, 3, 3, 3, 3, 4, 5, 5]
remove_duplicates(numbers)
'''

