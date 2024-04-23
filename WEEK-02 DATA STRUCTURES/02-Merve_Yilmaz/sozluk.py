'''
Kullanıcıdan gelen bir cümleyi giren ve ardından her harfin oluşum sayısını özetlemek için 
bir sözlük kullanan bir kod parçacığı yazın. Büyük/küçük harf dikkate almayın, 
boşlukları dikkate almayın ve kullanıcının herhangi bir noktalama işareti girmediğini varsayalım. 
Harflerin ve sayılarının iki sütunlu bir tablosunu, harfler sıralanmış şekilde görüntüleyin. 
Örnek Giriş Bu, birkaç kelimeden oluşan örnek bir metindir. 
Bu, bazı farklı kelimelerden oluşan daha fazla örnek metindir 
Çıktı [('a', 4), (' d', 3),('e', 10), ('f', 2), ('h', 4), ('i', 7), ('l', 3), 
('m' , 4), ('n', 1), ('o', 4), ('p', 2), ('r', 5), ('s', 10), ('t', 9) ), ('v', 1), 
('w', 4), ('x', 2)]
'''

cumle=input('Bir cumle giriniz:')
sirali_harf=sorted(set(cumle))
cikti=[]

cikti=[(i,cumle.count(i)) for i in sirali_harf]
        # for i in sirali_harf:
        #     harf_sayisi=cumle.count(i)
        #     set=i,harf_sayisi
        #     cikti.append(x)
print(cikti)