'''The user is asked to enter a sentence.A dictionary is then used to summarize the number of occurrences of each letter.
Cases are ignored, spaces are ignored, and it is assumed that the user has not entered any punctuation.
A two-column table containing letters and their numbers appears, with the letters sorted.'''


sentence = input('Write a sentence:')
sentence1 = sentence.lower()          # With Lower, capital letters in the sentence are ignored.
new_sentence = sentence1.translate(str.maketrans("", "", "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"))
#  Punctuation marks in the sentence are ignored with 'str.maketrans'...

print(new_sentence)
a = list(sorted(new_sentence.replace(' ','')))   # Gaps in the sentence are ignored.(with 'replace')
print((new_sentence.replace(' ','')))

listlen = len(a)
list2 = list(a)

print(list2)

list1 = [i for i in range(1,listlen+1)]   # With the for loop and range, numbers are listed as long as the length of the list.
matched_list = [(list1[j],list2[j]) for j in range(listlen) ]
# Two lists are compared and their elements are matched, each letter matching a number.
print(matched_list)


''' Kod guzel ama sizden isteneni vermiyor. Mesela soyle bir cumle yazdim;
Write a sentence:bazi eyler VAR ki soyLENMIYOR
bazi eyler var ki soylenmiyor
bazieylervarkisoylenmiyor
['a', 'a', 'b', 'e', 'e', 'e', 'i', 'i', 'i', 'k', 'l', 'l', 'm', 'n', 'o', 'o', 'r', 'r', 'r', 's', 'v', 'y', 'y', 'y', 'z']
[(1, 'a'), (2, 'a'), (3, 'b'), (4, 'e'), (5, 'e'), (6, 'e'), (7, 'i'), (8, 'i'), (9, 'i'), (10, 'k'), (11, 'l'), (12, 'l'), (13, 'm'), (14, 'n'), (15, 'o'), (16, 'o'), (17, 'r'), (18, 'r'), (19, 'r'), 
(20, 's'), (21, 'v'), (22, 'y'), (23, 'y'), (24, 'y'), (25, 'z')]
sizden istenen a hrfinden kac tane varsa onu yazmasi ama siz indexleri yazdirmissiniz.
Kucuk harfe cevirmeniz ve ozel karakterleri ignore etmeniz cok guzel.'''

