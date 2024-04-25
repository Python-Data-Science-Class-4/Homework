def unique_list(x):
    t = set(x) #to find the unrepeated item, we can change the list to set.
    return list(t) #since list object is asked we need to return to list before return
    

print(unique_list([1,2,3,3,3,3,4,5,5]))