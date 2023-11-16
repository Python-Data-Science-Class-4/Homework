'''
@description
Write a program that takes two inputs; one of them is a list and the other is a number, 
and returns the list obtained by shifting the elements in the list n places to the right (left) 
when n is positive (negative). Use wrap-around if an element is shifted beyond the end of the list, 
then continue to shift starting at the beginning of the list. 
Example Inputs [1, 2, 3, 4, 5], 2 Output [4, 5, 1, 2, 3] 
Inputs [1, 2, 3, 4, 5], -2 Output [3, 4, 5, 1, 2]

'''
sizeOfTheList = input("Please give a number of List: ")

#check if value is a number
if not sizeOfTheList.isdigit():
    while not sizeOfTheList.isdigit():
        sizeOfTheList=(input("!!!! must be a number that a given value !!!!!\nPlease retry : "))

#covert value to number
sizeOfTheList=int(sizeOfTheList)

#create a list
list = [i+1 for i in range (sizeOfTheList)]

shiftStart = int(float(input("Please give a number that starts shifting: ")))

if shiftStart >=0 :
    list = list[shiftStart+1::] + list[:shiftStart+1:]
else:
    list = list[shiftStart-1::]+list[:shiftStart-1:]
print(list)
    