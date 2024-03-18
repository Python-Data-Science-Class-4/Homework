# Tas - Kagit - Makas Oyunu 

oyuncu = input('Oyuncunun Ismi:')
oyuncu1 = input('Oyuncunun ismi1:')

puan_oyuncu = 0
puan_oyuncu1 = 0
# Oyun 10 el surecek! 
for el in range(10) :
    print(f'{'el:'}{el+1}')

    secim = input(oyuncu + ', T/K/M (Taş/Kağit/Makas) seçimi yapin: ')
    secim1 = input(oyuncu1 + ', T/K/M (Taş/Kağit/Makas) seçimi yapin: ')

    secim = secim.upper()
    secim1 = secim1.upper()
    if secim == 'T' and secim1 == 'K'or secim == 'M' and secim1 == 'T'or secim == 'K' and secim1 == 'M' :

        print ('{} 1 puan kazandi...'.format(oyuncu1))
        puan_oyuncu1 +=1

    elif secim == 'K' and secim1 == 'T' or secim == 'T' and secim1 == 'M' or secim == 'M' and secim1 == 'K':
        print ('{} 1 puan kazandi...'.format(oyuncu))
        puan_oyuncu +=1  
    else:
        print('Berabere') 
    
print (f'{oyuncu}:{puan_oyuncu} puan' )
print (f'{oyuncu1}:{puan_oyuncu1} puan')

if puan_oyuncu > puan_oyuncu1 :
    print(f'{oyuncu} Tebrikler Kazandiniz')
    
elif puan_oyuncu1 > puan_oyuncu :
    print(f'{oyuncu1} Tebrikler Kazandiniz') 

else:
    print('Oyun Berabere!')       
    

                 



            
            

      
    
                
    

         



















      


      


        
         



