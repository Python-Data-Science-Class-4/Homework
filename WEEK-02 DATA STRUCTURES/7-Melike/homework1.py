################# Homework 1 ##############

number = int(input("lutfen bir sayi giriniz:" ))

def lucky_numbers(number, k=2):
    list1 = list(range(1, number + 1))
    while True:
        list_new =[]
        k=2
        for index, number in enumerate(list1):
            if index % k == 0:
                list_new.append(number)
                k +=1
                print(list_new)
            elif k < len(list_new):
                break

lucky_numbers(number)

#!!!!!!!!!!!!!!!!  I tired a lot with this question, but unfortunately it gives an error. !!!!!!!!!!!!!!