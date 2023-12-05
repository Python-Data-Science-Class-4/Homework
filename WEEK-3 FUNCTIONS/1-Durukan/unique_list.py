def unique_list(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

test_case = unique_list([1,2,3,3,3,3,4,5,5])
print(test_case)

''' Kod guzel. Oneri olarak;
Listenizi bir set olarak çevirip sonra tekrar listeye dönüştürebilirsiniz. 
Biliyorsunuz set veri türü zaten benzersiz öğeler içerir,set e cevirdiginizde tek olan elemanlari alacaktir. 
ornek olarak bir kod paylasiyorum.

def remove_duplicates(numbers):
    unique_list=list(set(numbers))
    print(unique_list)

lst = [1, 2, 3, 3, 3, 3, 4, 5, 5]
remove_duplicates(lst)
'''
