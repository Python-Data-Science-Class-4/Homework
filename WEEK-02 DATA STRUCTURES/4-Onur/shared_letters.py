"""
4) Write a program that takes in two words as input and returns a list containing three elements,
in the following order Shared letters between two words. Letters unique to word 1. Letters unique to word 2.
Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations.
The strings will always be in lowercase and will not contain any punctuation.
Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']
"""

def process_words(word1, word2):
    set1 = set(word1)
    set2 = set(word2) #convert to set to apply set functions otherwise our list will have repeating syllabus

    shared = sorted(set1.intersection(set2))

    unique_word1 = sorted(set1 - set2)
    unique_word2 = sorted(set2 - set1)

    return [''.join(shared), ''.join(unique_word1), ''.join(unique_word2)] # create a list by joining itenms of each set


word1 = input("Please enter the first word: ")
word2 = input("Please enter the second word: ")

result = process_words(word1, word2)
print(result)