
# Write a function that controls the given inputs whether they are equal to their reversed order or not.

def equal (word):
    return word == word [::-1]
    
word_input = input ("Write a word that can be same with its reversed: ") . lower ()

print (word_input)
print (equal(word_input)) 






Write a word that can be same with its reversed: madam
madam
True
Write a word that can be same with its reversed: ali
ali
False
