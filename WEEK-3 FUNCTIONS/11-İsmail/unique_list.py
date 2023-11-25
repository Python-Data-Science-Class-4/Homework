given_list=[1,2,3,3,3,3,3,3,4,5,5,5]
unique_list=[]
def num_filter (given_list):
    i=0
    for i in given_list:
        if i not in unique_list:
            ''' Checking every single variable in the given_list. if variables not in the list then add to unique list'''
            unique_list.append(i)
    print(unique_list)    
    return
    
    
print(num_filter(given_list))