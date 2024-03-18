
 ######################## 2- equal_reserve #################

def equal_reserve(word1):
    word2 = word1[::-1]
    if word1==word2:
        print(True)
    else:
        print(False)





word1=input("enter your word: ")
equal_reserve(word1)
