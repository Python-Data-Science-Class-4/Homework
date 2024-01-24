'''İki basamaklı bir giriş numarasının transkripsiyonunu veren bir fonksiyon yazın.

Örnek:

28---------------->Yirmisekiz
'''
birler={1:"bir",2:"iki",3:"uc",4:"dort",5:"bes",6:"alti",7:"yedi",8:"sekiz",9:"dokuz",0:""}
onlar={1:"on",2:"yirmi",3:"otuz",4:"kirk",5:"elli",6:"atmiş",7:"yetmis",8:"seksen",9:"doksan",0:""}

def sayilar(sayi):
    """bolum=sayi//10
    modul=sayi%10
    text1=onlar[bolum]
    text2=birler[modul]
    return text1+' '+text2"""
    
    return onlar[sayi // 10] + ' ' + birler[sayi % 10]

rakam=int(input('lutfen iki haneli sayi giriniz : '))
print(sayilar(rakam))





















