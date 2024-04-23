# Get two words from the users.
word1 = input("Enter the first word: ").lower()
word2 = input("Enter the second word: ").lower()

# Find shared letters
shared_letters = ''.join(sorted(set(word1) & set(word2)))

# Find the fist word's unique letters
unique_letters_word1 = ''.join(sorted(set(word1) - set(word2)))

# Find the second word's unique letters
unique_letters_word2 = ''.join(sorted(set(word2) - set(word1)))

# Print the result.
result = [shared_letters, unique_letters_word1, unique_letters_word2]
print("Output:", result)
