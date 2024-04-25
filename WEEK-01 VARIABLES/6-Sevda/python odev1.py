#Asal Sayi Buldurma

while True:    
   
 a = int(input('Pozitif bir sayi giriniz:'))
 print ('Asal Sayilar:2,3,5,7')
 
 for i in  range (3,a+1):
    
    if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0 :
        print('Asal Sayilar:{}'.format(i))
        

 cevap = input('farkli bir sayi girmek ister misiniz?:E/H: ') 

 if cevap.upper() != 'E' :
      break 
