"""
3) Write a code snippet that inputs a sentence from the user, then uses a dictionary to summarize the number of occurrences of
each letter. Ignore case, ignore blanks and assume the user does not enter any punctuation. Display a two-column table of the letters
and their counts with the letters in sorted order.Example Input This is a sample text with several words This is more sample text with
some different words Output [('a', 4), ('d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), ('m', 4), ('n', 1), ('o' ,4), ('p', 2)
, ('r', 5), ('s', 10), ('t', 9), ('v', 1), ('w', 4), ('x', 2)]
"""


user_input = input("Please nter a sentence: ")

cleaned_input = user_input.lower().replace(" ", "") # we remove the spaces and lower the item to ignore case

unique_letters = set(cleaned_input) # change the item to a set to find unique occurences

letter_counts = {} #dictionary to hold results

for letter in unique_letters:
    count = cleaned_input.count(letter) # check how many occurence exists
    letter_counts[letter] = count #add to the dictionary

sorted_counts = sorted(letter_counts.items()) #create a list from the key value pair of dictionary using tuples

print(sorted_counts)