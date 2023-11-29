'''
Vücut Kitle İndeksi Hesaplayıcı Bir kişinin kilosunun boyuna göre normal olup olmadığını 
gösteren parametre. Buna Beden Kitle İndeksi denir. Kısaca kişinin kilosu, boyuna eşittir. 
Karesine bölersek vücut kitle indeksi elde edilir. 
Kullanıcının kilosu ve boyu alınarak sonuç 25'in altında ise NORMAL, 
25-30 arasında ise AŞIRI KİLO, 30-40 ise OBSE, 40 ve üzerinde ise AŞIRI OBSE uyarısı yazdırılır.
'''

kilo = float(input('Lutfen kilonuzu giriniz:'))
boy = float(input('Lutfen metre ve cm olarak boyunuzu giriniz:'))
endeks = kilo / boy**2

if endeks < 25:
    print('Normal')
elif endeks >= 25 and endeks<30:
    print('Asiri kilo')
elif endeks >= 30 and endeks<40:
    print('Obez')
elif endeks >= 40:
    print('Asiri Obez')

