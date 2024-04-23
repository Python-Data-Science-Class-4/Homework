while True:
    sayi_str = input("Bir sayı girin: ")
    if sayi_str.isdigit():  # Girilen değerin bir tam sayı olduğunu kontrol eder
        sayi = int(sayi_str)
        if sayi < 2:
            print("2 veya daha büyük bir pozitif tamsayı girmelisiniz.")
        else:
            print(f"{sayi}'e kadar olan asal sayılar:")
            for i in range(2, sayi + 1):
                asal = True
                for j in range(2, i):
                    if i % j == 0:
                        asal = False
                        break
                if asal:
                    print(i, end=" ")
            print("\n")
    else:
        print("Geçerli bir sayı girmelisiniz.")
    
    devam = input("Başka bir sayı girmek ister misiniz? (E/H): ")
    if devam.lower() != 'e':
        break
