'''
Giriş olarak iki kelime alan ve üç öğeyi içeren bir listeyi aşağıdaki sıraya göre 
döndüren bir program yazın: 
İki kelime arasındaki paylaşılan harfler. 
1. kelimeye özel harfler. 
2. kelimeye özel harfler. 
Çıktının her elemanı benzersiz harflere sahip olmalı ve alfabetik olarak sıralanmalıdır. 
Ayarlanmış işlemleri kullanın. Dizeler her zaman küçük harf olacak ve 
herhangi bir noktalama işareti içermeyecektir. 
Örnek Giriş1 sharp Giriş2 soap Çıkış ['aps', 'hr', 'o']
'''

kelime_1=set(input('Birinci kelimeyi giriniz:'))
kelime_2=set(input('Ikinci kelimeyi giriniz:'))

cikis=''.join(sorted(kelime_1&kelime_2)),''.join(sorted(kelime_1-kelime_2)),''.join(sorted(kelime_2-kelime_1))
print(cikis)

