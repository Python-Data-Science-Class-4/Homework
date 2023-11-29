def is_palindrome(word):
    return word == "".join(list(word)[::-1])
        

test_case = is_palindrome('ardsa_asdra')
print(test_case)

''' Kod gayet guzel ve calisiyor, hatta daha basit bir sekilde yazailiriz.
 return word == "".join(list(word)[::-1]) bu kismi 
 return word == word[::-1] seklinde de yazabilirsiniz.
 Ayrica soruda bizden istenen kelimeleri kullanicinin girmesi. Sadece input eklemeniz yeterli olacaktir.'''
