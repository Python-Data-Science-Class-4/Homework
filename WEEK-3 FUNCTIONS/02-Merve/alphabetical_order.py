'''
Write a function that takes an input of different words with hyphen (-) in between them and then:
sorts the words in alphabetical order, adds hyphen icon (-) between them, gives 
the output of the sorted words.
Example:
Input >>> green-red-yellow-black-white
Output >>> black-green-red-white-yellow
'''


girdi=input('lutfen kelime giriniz:')

def order(kelimeler):
    # kelimeler=girdi.split('-')
    # liste='-'.join((sorted(kelimeler)))
    # return liste
    
    return '-'.join((sorted(girdi.split('-'))))

print(order(girdi))
