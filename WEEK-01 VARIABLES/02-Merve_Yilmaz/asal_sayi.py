while True:
    
    sayi=int(input('Lutfen pozitif bir sayi giriniz:'))

    for sayi in range(2,sayi+1):
        sayac=0
        for k in range(2,sayi):
            if sayi % k == 0 :
                sayac+=1
                break

        if sayac==0:
            print(sayi,'asal sayidir.')   
                
            
    cevap=input('Yeni bir sayi girmek ister misiniz? E/H : ')
    if cevap=='H':
        break
 
 
    