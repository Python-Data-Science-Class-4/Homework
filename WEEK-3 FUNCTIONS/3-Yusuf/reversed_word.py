def reverse_control(word):
    word = word.lower()
    if word==word[::-1]:
       return True 
    else:
        return False

words = input("Please type the woords seperated with commas.:  ")
words_list = words.split(',')


for word in words_list:
    result = reverse_control(word)
    print(f"{word}: {result}")