n = int(input("Enter a number between 2-10: "))
my_list = list(range(1, n + 1))
print(my_list)

del_Num = 2
while del_Num <= len(my_list):
    new_list = []
    for i in range(len(my_list)):
        if (i + 1) % del_Num != 0:
            new_list.append(my_list[i])

    my_list = new_list  
    print(new_list)

    del_Num += 1





