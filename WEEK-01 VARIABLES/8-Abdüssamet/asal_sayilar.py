while True:
    N=int(input("Lütfen N sayisini giriniz (1den buyuk olmalidir) : "))
    asal_sayilar= []
    
    for sayi in range(2, N+1 ):
        asal=True
        for i in range(2,sayi):
            if sayi % i == 0:
                asal=False
                break
        if asal:
            asal_sayilar.append(sayi)
            
    print(f"1den {N}`e kadar olan asal sayilar : {asal_sayilar}")
        
    devam=input("yeni bir N sayisi girmek istermisiniz ? (evet yada hayir) : ").strip().lower()        
    if devam != "evet" :
        print("Program sonlandiriliyor...")
        break