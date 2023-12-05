#tas-KagÄ±t-Makas Oyuncularin isimlerini alip tas - kagit - makas oyununu oynayin. 
#oyun 10 el surecek. 10 elin sonunda kazanan belirlenecek. Puan sonunda goruntulenecektir.
import random

#tas=0
#kagit=1
#makas=2
sayac=0
kisi_puan=0
makina_puan=0
while sayac<10:
    print(sayac+1,". Tur")
    
    kisi=input("lutfen 0-1-2 sayilarindan birini secin : ")
    print("kullanici tercihi : " ,kisi)
    
    makina =int(random.uniform(0,3))
    print("bilgisayarin tercihi : " ,makina)
    
    if int(kisi) == makina :
        print("berabere")
        sayac+=1
        
    elif(int(kisi)==0 and makina==2) or (int(kisi)==1 and makina==0) or (int(kisi)==2 and makina==1):
        kisi_puan += 10
        print("Kisi puani :", kisi_puan ,"oldu" )
        sayac+=1
    
    elif(int(kisi)==1 and makina==2) or (int(kisi)==2 and makina==0) or (int(kisi)==0 and makina==1):
        makina_puan+= 10
        print("Makina puani : ",makina_puan ,"oldu")
        sayac+=1
    else :
        print('hatali giris yaptiniz tekrar deneyiniz')
    
print("Kisi puani:", kisi_puan)
print("Makine puani:", makina_puan)
if kisi_puan>makina_puan :
    print("KISI KAZANDI")
elif makina_puan>kisi_puan:
    print("makina KAZANDI")
else:
    print("BERABERE BITTI")
print("oyun sonlandiriliyor")