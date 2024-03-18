def shift_list_elements(lst, n):
    n = n % len(lst)  
    shifted_list = lst[-n:] + lst[:-n]  

    return shifted_list


input_list = input("Enter a list of numbers separated by spaces: ")

input_list = [int(x) for x in input_list.split()]


shift_value = int(input("Enter the shift value: "))


output = shift_list_elements(input_list, shift_value)
print(f"Input: {input_list}, Shift: {shift_value}, Output: {output}")
