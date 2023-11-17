def shift_list(lst, n):

    # when the shift reaches the length of the list, elements returns the starting point. That's why take the modulus of shifts
    shift = n % len(lst)

    if n>=0:
        # if the number is positive go to the right
        print(lst[(len(lst) - shift):] + lst[: (len(lst)-shift)] )
    else:
        # if the number is negative go to the left
        print(lst[(shift*-1):] + lst[:(shift*-1)])

shift_list(lst=(input("Enter a comma seperated list (eg.: 1,2,3): ")).split(","), n=int(input("Enter the number of shift: ")))

'''Kod cok basarili
Sadece oneri olarak sunlari soyleyebilirim.
**shift değerini direkt olarak negatif bir değere çarpmak yerine, 
lst[shift:] + lst[:shift] ve lst[(len(lst) - shift):] + lst[:(len(lst) - shift)] ifadelerini kullanarak daha acik ifade edebiliriz.
**Listenin elemanlarini tek tek alabilirsiniz kullanicidan
list_1 = []
while True:
    
    inp_1 = input('Lutfen sayi girin: ')
    
    if inp_1 == 'q' or inp_1 == 'Q':
        break
    
    list_1.append(int(inp_1))
    Duzeltmeye gerek yok sadece bir kac oneri. Ellerinize saglik..
'''
