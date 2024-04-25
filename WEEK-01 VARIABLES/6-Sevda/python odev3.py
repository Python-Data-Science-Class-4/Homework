# Ders Basari Ortalama Hesaplama

ad = input('Ogrenci Adi-Soyad:')
numara = int(input('Ogrenci No:'))
ders1 = input(['1.Ders Adi:', 'vize notu:', 'final notu'])
print(ders1)
print(f'{'1.Ders Adi:'}{ders1},{'vize notu:'}{vize1},{'final notu:'}{final1}')
vize1 = int(input('vize notu:') )
final1 = int(input('final notu:'))
ders2 = input('2. Ders Adi:')
vize2 = int(input('vize notu:') )
final2 = int(input('final notu:'))
ders3 = input('3. Ders Adi:')
vize3 = int(input('vize notu:') )
final3 = int(input('final notu:'))
ders4 = input('4. Ders Adi:')
vize4 = int(input('vize notu:') )
final4 = int(input('final notu:'))

vize_puan_list = [vize1,vize2,vize3,vize4]
final_puan_list = [final1,final2,final3,final4]

'''ortalama1 = vize1*40/100 + final1*60/100 
ortalama2 = vize2*40/100 + final2*60/100 
ortalama3 = vize3*40/100 + final3*60/100 
ortalama4 = vize4*40/100 + final4*60/100''' 

print(f'{ders1}:{ortalama1}')
if ortalama1 > 50 :
    print('BASARILI')
else :
    print('BASARISIZ')    

print(ders2 +':'+str(ortalama2))
if ortalama2 > 50 :
    print('BASARILI')
else :
    print('BASARISIZ')  
print(ders3 +':'+str(ortalama3))
if ortalama3 > 50 :
    print('BASARILI')
else :
    print('BASARISIZ')  
print(ders4 +':'+str(ortalama4))
if ortalama1 > 50 :
    print('BASARILI')
else :
    print('BASARISIZ')  

Genelortalama = (ortalama1 + ortalama2 + ortalama3 + ortalama4)/4
print('Genel Ortala:', Genelortalama)

if Genelortalama > 50 :
    print('BASARILI')
else :
    print('BASARISIZ')    
