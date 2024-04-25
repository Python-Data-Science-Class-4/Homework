'''
Ders Puanı Hesaplamasında 
Kullanıcı Adı, Soyadı, Öğrenci Numarası, 4 ders adı, Vize ve Final notları istenecektir. 
Ara sınav notunun %40'ı ile final notunun %60'ının toplamı yıl sonu ortalamasını verecektir. 
Ortalama 50'den az ise ekranda "BAŞARISIZ", 50 ve üzerinde ise ekrana "Başarılı" yazacaktır. 
Bu baskı işlemi 4 derstir. yapılacak ve dersler birbiri ardına yazılacaktır.
'''

ad= input('Adinizi giriniz:')
soyad= input('Soyadinizi giriniz:')
print('-' * 45)
ders_listesi=[]
vize_puan=[]
final_puan=[]
ortalama_puan=[]


for i in range(4):

    ders=input(f'{i+1}. dersinizi giriniz:')
    vize=float(input(f'{ders}. dersinizin vize notunu giriniz:'))
    final=float(input(f'{ders}. dersinizin final notunu giriniz:'))
    ders_listesi.append(ders)
    vize_puan.append(vize)
    final_puan.append(final)
    puan=float(vize_puan[i] * 0.4) + float(final_puan[i] * 0.6)
    ortalama_puan.append(puan)
    print('-' * 45) 
 
print('\n')
print('-' * 45) 

for i in range(len(ders_listesi)):
    if ortalama_puan[i] < 50:
        print(f'{ders_listesi[i]} ortalamaniz {ortalama_puan[i]}. Sonucunuz: "BASARISIZ"')
    elif ortalama_puan[i]>=50:
        print(f'{ders_listesi[i]} ortalamaniz {ortalama_puan[i]}. Sonucunuz: "BASARILI"')
    