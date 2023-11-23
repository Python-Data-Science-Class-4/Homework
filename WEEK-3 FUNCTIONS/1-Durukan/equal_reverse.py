def is_palindrome(word):
    return word == "".join(list(word)[::-1])
        

test_case = is_palindrome('ardsa_asdra')
print(test_case)