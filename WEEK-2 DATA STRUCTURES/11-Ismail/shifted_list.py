#2.	Write a program that takes two inputs; one of them is a list and the other is a number,
#and returns the list obtained by shifting the elements in the list n places to the right (left) when n is positive (negative).
# Use wrap-around if an element is shifted beyond the end of the list, then continue to shift starting at the beginning of the list.
#Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]


createlist = [] #create a empty list    

n = int(input("Enter a number: "))


for i in range (1,n):   
    
    createlist.append(i)#create a list with numbers up to the value entered by the user

m = int(input("Enter a number: "))

if m > 0: 
    shifted_left = createlist[m:] + createlist[:m] #If the user enters a positive number, the list will shift to the right by the number entered.
    print("Shifted left:", shifted_left)
elif m < 0:
    shifted_right = createlist[-m:] + createlist[:-m] #If the user enters a negative number, the list will shift to the right by the number entered.
    print("Shifted right:", shifted_right)
else:
    print("No shift, the list remains the same:", createlist) 