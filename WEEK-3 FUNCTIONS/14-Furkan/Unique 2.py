
# Write a function that filters all the unique (unrepeated) elements of a given list.

def remove_duplicates(lst):
    unique_list = list(sorted(set(lst)))
    print (unique_list)

numbers = [1,2,3,3,3,3,4,5,5]
remove_duplicates(numbers)
