
 ######################## 2- equal_reserve #################

list = ["madam", "tacocat", "utrecht"]
k = 1
a = 0
while True:

    for i in list:
        if list[a] == list[-k]:
            print(True)
            k -= 1
            a += 1
            if a > len(list) / 2:
                break
        else:
            print(False)
#### !!!!!!!!!!!!!!!!!!! This code doesn't work #############
