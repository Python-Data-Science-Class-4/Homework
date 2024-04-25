"""
TASK
2) Write a program that takes two inputs; one of them is a list and the other is a number, and returns the list obtained by shifting the
elements in the list n places to the right (left) when n is positive (negative). Use wrap-around if an element is shifted beyond the end of the list,
 then continue to shift starting at the beginning of the list. Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 
 Output [3, 4, 5, 1, 2]
"""

user_text = input("Please write the list you want to shift/ Ex: [1, 2, 3, 4, 5]")
modified= user_text.replace('[', '').replace(']', '').replace(' ', '') # remove unwanted charachters from the string to be able to convert to list
user_string_list = modified.split(",") # convert to list 

user_final = [int(item) for item in user_string_list] # convert each element to integer inside the list
user_shift_input = int(input("Please write how many item you want to shift"))

shift = user_shift_input%5 #we need to shift 2 item if user input 7 because shift of 5 eqauls to same list
print(user_final[-shift:]+user_final[:-shift])