
'''Verilen girislerin ters siralarina esit olup olmadiklarini kontrol eden bir fonksiyon yazin.

ornek:

Giris >>> hanımefendi, tacocat, utrecht

cikis >>> Dogru, Dogru, Yanlis'''


def ters_sira(kelime):
    kelimeters=kelime[::-1]
    
    if kelimeters==kelime :
        print('ters siralama esit : ' , kelime)
    else:
        print('ters siralama esit degil : ' ,kelimeters)  


kelime=input('lütfen bir kelime veya cümle giriniz: ')    

ters_sira(kelime)