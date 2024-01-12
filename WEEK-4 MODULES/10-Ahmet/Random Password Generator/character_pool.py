"""In line with the request from the "main" module, a random character is selected from the character pool and 
assigned to the "list" variable. As a result of the operation, the "list" variable is returned."""


import random as rd

number = ["0","1","2","3","4","5","6","7","8","9"]
word_B = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","R","S","T","U","V","W","Q","X","V","Z"]
word_L = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","r","s","t","u","v","w","q","x","v","z"]
symbol = [".",",","*","/","+","-","?"]


def generate (x):   #The "generate" function uses the "x" value it receives from the "main" module to determine the character type to be generated.
    list = 0
    if x == 0:
        i = rd.randint(0,9)
        list = number[i]
        return list
    elif x == 1:
        i = rd.randint(0,25)
        list =word_B[i]
        return list
    elif x == 2:
        i = rd.randint(0,25)
        list = word_L[i]
        return list
    elif x == 3:
        i = rd.randint(0,6)
        list = symbol[i]
        return list