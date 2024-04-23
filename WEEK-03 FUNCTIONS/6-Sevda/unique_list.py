# unique_list
'''Write a function that filters all the unique(unrepeated) elements of a given list.
Example:
Function call: unique_list([1,2,3,3,3,3,4,5,5])
Output : [1, 2, 3, 4, 5]'''


repetitive_list = [1,2,2,3,3,4,4,5,5,6,7,7]
def unique_list(lists):
    '''set(), creates a set containing the elements of the list.
    The cluster data structure contains unipue elements.'''
    return list(set(lists)) 
    
print(unique_list(repetitive_list))    

''' Cok guzel,tebrik ederim.'''




