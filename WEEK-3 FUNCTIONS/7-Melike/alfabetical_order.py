###################### 3- alfabetical_order #################

def alfabetical_order(words):

    list1= []
    list1 = words.split("-")
    list1.sort()
    print("-".join(list1))
words = input("please enter your words: ")
alfabetical_order(words)
