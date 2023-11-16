def letter_counter(sentence):
    
    # Create a list whic includes only the letters of sentence, not numeric or special characters and space.
    sentence = [i for i in sentence.lower() if i.isalpha() == True]
    count_dict = {}


    #Check the occurence of each unique item in the list and increase the count. Then add it to the dictinary.
    for i in set(sentence):
        
        count_dict[i] = sentence.count(i)
        
        # method 2
        # count = 0
        # for x in sentence:
        #     if x == i:
        #         count+=1

    for i in count_dict:
        print(f"Letter: {i} Count: {count_dict[i]}")

letter_counter(sentence=input("Please enter a sentence: "))