'''
@description
Write a program that takes in two words as input and returns a list containing three elements, in the following order Shared letters between two words. Letters unique to word 1. 
Letters unique to word 2. Each element of the output should have unique letters, and should be alphabetically sorted. 
Use set operations. 
The strings will always be in lowercase and will not contain any punctuation. 
Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o'] 
'''

word1 = input('Please write one word : ')
word2 = input('Please write another word : ')

#create a list, all caracter small
list1 = [i for i in word1.lower()]
list2 = [i for i in word2.lower()]

#order list
list1.sort()
list2.sort()
set1 = set(list1)
set2=set(list2)

resultList = ["","",""]

#find same&different letters with intersections/subtraction between sets and ensure ordering
for i in set1&set2:
    resultList[0] = resultList[0]+i
resultList[0] = ''.join(sorted(resultList[0]))

for i in set1-set2:
    resultList[1] = resultList[1]+i
resultList[1] = ''.join(sorted(resultList[1]))

for i in set2-set1:
    resultList[2] = resultList[2]+i
resultList[2] = ''.join(sorted(resultList[2]))

print(resultList)



