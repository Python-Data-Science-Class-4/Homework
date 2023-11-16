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

