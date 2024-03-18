############# Homework 3 ##########

list1 = list(input("please enter your text :"))
list2 = []
for i in list1:
    list1.count(i)
    list2.append(({i : list1.count(i)}))
print(list2)