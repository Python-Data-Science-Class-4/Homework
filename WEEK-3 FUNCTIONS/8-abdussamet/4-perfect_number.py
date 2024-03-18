'''4-perfect_number.py
Mükemmel sayı: Mükemmel sayı, kendi bölenlerinin toplamına eşit olan pozitif bir tam sayıdır.
En küçük mükemmel sayı 1, 2 ve 3'ün toplamı olan 6'dır.
Diğer bazı mükemmel sayılar 28(1+2+4+7+14=28), 496 ve 8128'dir.
1 ile 1000 arasındaki mükemmel sayıları bulan bir fonksiyon yazın. 
1 ile 1000 arasındaki mükemmel sayıları kontrol edin ve 
azaltma ve filtreleme fonksiyonlarını kullanarak mükemmel sayıların toplamını bulun.'''



def perfect(sayi):
    total=0
    for i in range(1,sayi):
        if sayi%i==0:
            total += i
        else:
            continue
    if sayi==total:
        print(sayi,'mukemmel sayidir')
    else:
        print(sayi,' mukemmel sayi degildir')    


sayi=int(input('lutfen bir sayı giriniz : '))

perfect(sayi)