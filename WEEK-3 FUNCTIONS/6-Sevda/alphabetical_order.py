'''Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives the output of the sorted words.
Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow'''

#'banana','watermelon','strwberry','grape','melon','apple')

def alphabetic(*words):
    ''' This function sorts the entered words in alphabetical order.'''
    alphabetic_list = '-'.join(sorted(words))  #With 'join', a (-) sing is added between them.
    return alphabetic_list
    
print(alphabetic('banana','watermelon','strwberry','grape','melon','apple'))

