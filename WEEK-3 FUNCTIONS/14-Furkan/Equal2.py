
def equal (a,b,c):
    
    return word_1 == word_1[::-1], word_2 == word_2[::-1], word_3 == word_3[::-1] 
 
word_1 = list (input ("Enter your first word that can be same with its reversed form: ") . lower ())
word_2 = list (input ("Enter your second word that can be same with its reversed form: ") . lower ())
word_3 = list (input ("Enter your third word that can be same with its reversed form: ") . lower ())

print (word_1, word_2, word_3)
print (equal(word_1, word_2, word_3))