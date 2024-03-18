#!/usr/bin/python
#Ders Puanı Hesaplamasında Kullanıcı Adı, Soyadı, Öğrenci Numarası, 4 ders adı, Vize ve Final notları istenecektir. 
#Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir. 
#Ortalama 50'den az ise ekranda "BAŞARISIZ", 50 ve üzerinde ise ekrana "Başarılı" yazacaktır. 
#Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.


isim=input("adiniz : ")
soyisim=input("soy isminiz : ")
ogrno=int(input("ogrenci numaraniz : "))

ders1=input("1.ders adi : ")
ders1_vize=int(input("1.ders vizesi : "))
ders1_final=int(input("1.ders finali : "))

ders2=input("2.ders adi : ")
ders2_vize=int(input("2.ders vizesi : "))
ders2_final=int(input("2.ders finali : "))

ders3=input("3.ders adi : ")
ders3_vize=int(input("3.ders vizesi : "))
ders3_final=int(input("3.ders finali : "))

ders4=input("4.ders adi : ")
ders4_vize=int(input("4.ders vizesi : "))
ders4_final=int(input("4.ders finali : "))

ders1_ort=(ders1_vize*0.40)+(ders1_final*0.60)
ders2_ort=(ders2_vize*0.40)+(ders2_final*0.60)
ders3_ort=(ders3_vize*0.40)+(ders3_final*0.60)
ders4_ort=(ders4_vize*0.40)+(ders4_final*0.60)

print(isim,soyisim,ogrno)


if ders1_ort < 50 :
    print(ders1,"den kaldiniz")
elif ders1_ort >= 50 :
    print(ders1,"den gectiniz. TEBRIKLER")
else:
    print("hatali bir islem var")
    
if ders2_ort < 50 :
    print(ders1,"den kaldiniz")
elif ders2_ort >= 50 :
    print(ders2,"den gectiniz. TEBRIKLER")
else:
    print("hatali bir islem var")    

if ders3_ort < 50 :
    print(ders3,"den kaldiniz")
elif ders3_ort >= 50 :
    print(ders3,"den gectiniz. TEBRIKLER")
else:
    print("hatali bir islem var")
    
if ders4_ort < 50 :
    print(ders4,"den kaldiniz")
elif ders4_ort >= 50 :
    print(ders4,"den gectiniz. TEBRIKLER")
else:
    print("hatali bir islem var")    