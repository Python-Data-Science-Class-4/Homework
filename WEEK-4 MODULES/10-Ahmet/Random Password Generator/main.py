"""RANDOM PASSWORD GENERATOR

- Password length will be between 10 and 20 characters
- It will contain at least 2 capital letters, 2 numbers and 2 special symbols (punctuation marks).
- All characters will be mixed.
- The character numbers of the passwords will also be shown in the output."""






import character_pool   #The "character_pool" module, which generates random characters, is called.
import random as rd

password = []

z = int(input("Specify how long your password will be (Min: 10 - Max: 20):"))

lst = []
a = 0


while a < 4:      #The loop runs 4 times to produce 2 of each of 4 different character types.
    i = 0
    while i < 2:
        lst.append(character_pool.generate(a))      #The variable a determines our character type. The "generate" function in the 
        i += 1                                      #"character_pool" module is run for each character. After two characters are 
    a += 1                                          #produced, the next character type is used.


#After at least 2 of each character are produced, random characters are generated and assigned to the remaining spaces in the "lst" list.
while len(lst) < z:                                 
    chance = rd.randint(0,3)        #In order to generate random characters, a random index number is generated.
    lst.append(character_pool.generate(chance))


#The characters kept in the "lst" list are mixed and assigned to the "password" list.
while len(lst) > 0:
    q = rd.randint(0,len(lst)-1)
    password.append(lst[q])
    del lst[q]


print(f"Password : {password}\nTotal {z} Characters")