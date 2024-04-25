############## Homework 4 ############

word1 = set(input("enter the first word: "))
word2 = set(input("enter the second word: "))

my_list =[]
common_elements = sorted(word1.intersection(word2))
word1_diff_word2 =sorted(word1.difference(word2))
word2_diff_word1 = sorted(word2.difference(word1))

my_list.extend([common_elements, word1_diff_word2, word2_diff_word1])
my_list2 =[]

for i in my_list:
    my_list2.append(["".join(i)])

print(my_list2)