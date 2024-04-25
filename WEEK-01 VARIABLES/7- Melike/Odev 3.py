

################# DERS NOTLARI ###############

ad = input("isminizi giriniz: ")
soyad = input("soyadinizi giriniz:")
no = int(input("4 haneli ogrenci numaranizi giriniz:"))
dersler = ["matematik", "tarih", "ingilizce","fizik"]
print(dersler)
mat_v = int(input('matematik dersinin vize notunu giriniz'))
mat_f = int(input('matematik dersinin final notunu giriniz'))
tarih_v = int(input('tarih dersinin vize notunu giriniz'))
tarih_f = int(input('tarih dersinin final notunu giriniz'))
ing_v = int(input('ingilizce dersinin vize notunu giriniz'))
ing_f = int(input('ingilizce dersinin final notunu giriniz'))
fizik_v = int(input('fizik dersinin vize notunu giriniz'))
fizik_f = int(input('fizik dersinin final notunu giriniz'))

mat_sonuc = mat_v * 0.4 + mat_f * 0.6
tarih_sonuc = tarih_v * 0.4 + tarih_f * 0.6
ing_sonuc = ing_v * 0.4 + ing_f * 0.6
fizik_sonuc = fizik_v * 0.4 + fizik_f * 0.6

if mat_sonuc >= 50:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci MATEMATIK dersinden BASARILIDIR")
else :
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci MATEMETIK dersinden BASARISIZDIR")
if tarih_sonuc >= 50:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci TARIH dersinden BASARILIDIR")
else:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci TARIH dersinden BASARISIZDIR")
if ing_sonuc >= 50:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci INGILIZCE dersinden BASARILIDIR")
else:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci INGILIZCE dersinden BASARISIZDIR")
if fizik_sonuc >= 50:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci FIZIK dersinden BASARILIDIR")
else:
    print(f"{ad} {soyad} isimli ve {no} numarali ogrenci FIZIK dersinden BASARISIZDIR")