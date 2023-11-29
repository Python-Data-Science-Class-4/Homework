'''
Taş-Kağıt-Makas Oyuncuların isimlerini alıp taş - kağıt - makas oyununu oynayın. 
oyun 10 el sürecek. 
10 elin sonunda kazanan belirlenecek. 
Skor sonunda görüntülenecektir.
'''

import random


oyuncu_listesi=[]
oyuncu1_skor=0
oyuncu0_skor=0

for oyuncu in range(1, 3):
    oyuncu_adi=input(f'{oyuncu}. oyuncu adini giriniz:')
    oyuncu_listesi.append(oyuncu_adi)

print('*'*15)

oyun=['tas', 'kagit', 'makas']


for tur in range(1,11):
    oyun_secim=[]
    for k in oyuncu_listesi:
        secim=random.choice(oyun)
        oyun_secim.append(secim)
        print(k, '=', secim)

    if oyun_secim[0]=='tas' and oyun_secim[1]=='kagit':
        print(f'{tur}. tur kazanani',oyuncu_listesi[1])
        oyuncu1_skor+=1
    elif oyun_secim[0]=='kagit' and oyun_secim[1]=='tas':
        print(f'{tur}. tur kazanani',oyuncu_listesi[0])
        oyuncu0_skor+=1
    elif oyun_secim[0]=='tas' and oyun_secim[1]=='makas':
        print(f'{tur}. tur kazanani',oyuncu_listesi[0])
        oyuncu0_skor+=1
    elif oyun_secim[0]=='makas' and oyun_secim[1]=='tas':
        print(f'{tur}. tur kazanani',oyuncu_listesi[1])
        oyuncu1_skor+=1
    elif oyun_secim[0]=='kagit' and oyun_secim[1]=='makas':
        print(f'{tur}. tur kazanani',oyuncu_listesi[1])
        oyuncu1_skor+=1
    elif oyun_secim[0]=='makas' and oyun_secim[1]=='kagit':
        print(f'{tur}. tur kazanani',oyuncu_listesi[0])
        oyuncu0_skor+=1
    else:
        print('Berabere!')

    print('-' *15)  

if oyuncu0_skor<oyuncu1_skor:
    print(f'Tur sonu kazanan oyuncu:{oyuncu_listesi[1]} \nToplam skor: {oyuncu1_skor}')
elif oyuncu0_skor==oyuncu1_skor:
    print(f'Berabere!Her iki oyuncunun toplam skoru {oyuncu1_skor}')
else:
    print(f'Tur sonu kazanan oyuncu:{oyuncu_listesi[0]} \nToplam skor: {oyuncu0_skor}')