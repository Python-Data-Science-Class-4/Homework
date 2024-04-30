
############### ASAL SAYI ###################

sayi = int(input("lutfen bir sayi giriniz: "))
while True:
    if sayi <= 1:
        print("lutfen  1 den buyuk bir tam sayi giriniz")

        for i in range(2, sayi+1):
            if sayi % i == 0:
                print(f"{i} sayisi asal degildir.")
            else:
                print(f"{i} sayisi asaldir")
                print("Devam etmek istyor musunuz evet veya hayir yaziniz")
                cevap = input()
                if cevap == "evet":
                    print(".......")
                elif cevap == "hayir":
                    break
##### !!!! Bunu tam yapamadim malesef.!!!!