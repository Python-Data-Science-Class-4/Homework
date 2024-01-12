'''
Belirli bir listenin tum benzersiz (tekrarlanmayan) ogelerini filtreleyen bir fonksiyon yazın.

Ornek:

islev cagrisi: benzersiz_liste([1,2,3,3,3,3,4,5,5])

cikis : [1, 2, 3, 4, 5]
'''


def benzersiz(my_nums):
    my_list=[]
    for i in my_nums:
        my_list.append(i)
        my_list.sort()
    return my_list    

while True:
    my_nums=int(input('lutfen istediginiz kadar sayi giriniz !!'))

    print(benzersiz(list(set(my_nums))))







