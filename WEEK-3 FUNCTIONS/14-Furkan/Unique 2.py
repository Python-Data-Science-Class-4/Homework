
def remove_duplicates(lst):
    unique_list = list(sorted(set(lst)))
    print(unique_list)

numbers = input ("Write a set of numbers: ")
remove_duplicates(numbers)