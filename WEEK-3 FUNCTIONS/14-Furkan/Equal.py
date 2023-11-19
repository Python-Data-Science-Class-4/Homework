
# Write a function that controls the given inputs whether they are equal to their reversed order or not.

def equal (reverse):
    
    return word == word[::-1]
    
word = list (input ("Enter a word that is the same with its reversed form: ") . lower ()) 

print (equal (word))
