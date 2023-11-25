# Write a function that controls the given inputs whether they are equal to their reversed order or not.

# Example: Input >>> madam, tacocat, utrecht   Output >>> True, True, False

# Define a function that controls the given inputs whether they are equal to their reversed order or not >> palindromic order


def word_control(word):
    reverse= word[::-1]
    
    if reverse == word:
        return True, word
    else:
        return False
    
word=input("Enter a word :")

print(word_control(word))