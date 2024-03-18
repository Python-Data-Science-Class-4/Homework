#Vucut Agirlik Indeksi Hesaplama

kilo = int(input('kilonuz:'))
boy = float(input('boyunuz:'))

print('Vucut agirlik indeksiniz hesaplaniyor...')

VKI = int((kilo) /(boy*boy))
print('VucutKitleIndeksi:',VKI)

if  25< VKI <30 :
    print('ASIRI KILO')
elif 30 < VKI < 40 :
    print('OBEZ')
elif 40 < VKI :
    print('ASIRI OBEZ')
else:
    print( 'NORMAL')
