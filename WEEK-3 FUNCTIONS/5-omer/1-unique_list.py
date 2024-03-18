'''
@description
Write a function that filters all the unique(unrepeated) elements of a given list.

Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output : [1, 2, 3, 4, 5]
'''

#give unique elements of the list as a list
def unique_list(lst):
    #first converto to set that get the unique elements of the list, than give the set as a list
    return list(set(lst))

print(unique_list([1,2,3,3,3,3,4,5,5]))

