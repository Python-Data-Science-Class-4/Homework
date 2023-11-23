def unique_list(lst):
    unique_list = []
    for i in lst:
        if i not in unique_list:
            unique_list.append(i)

    return unique_list

test_case = unique_list([1,2,3,3,3,3,4,5,5])
print(test_case)

