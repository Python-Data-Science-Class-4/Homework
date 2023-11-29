
def equal (a,b,c):
    
    return word_1 == word_1[::-1], word_2 == word_2[::-1], word_3 == word_3[::-1] 
 
word_1 = list (input ("Enter your first word that can be same with its reversed form: ") . lower ())
word_2 = list (input ("Enter your second word that can be same with its reversed form: ") . lower ())
word_3 = list (input ("Enter your third word that can be same with its reversed form: ") . lower ())

print (word_1, word_2, word_3)
print (equal(word_1, word_2, word_3))

'''Sizden istenen soyle bir sey.
Write a function that controls the given inputs whether they are equal to their reversed order or not.
Example:
Input >>> madam, tacocat, utrecht
Output >>> True, True, False

**Siz kelimeleri harflere ayirmissiniz ama buna gerek yok.
**Butun kelimlere tek tek ayri islem yapmamak icin fonksiyon yaziyoruz.Ama siz hepsi icin ayri islem yapmissiniz.
Soruda sizden 3 kelime istemis ama 10 isteseydi daha zor olurdu. Fonksiyonun amacina uygun olarak tekrrar bakalim bu soruya.

**Ayrica equal fonksiyonunun parametrelerini a, b, ve c olarak tanımlanmışsiniz 
ama fonksiyon içinde kullanılan isimler word_1, word_2, ve word_3. Parametre isimleri ve kullanılan isimlerin aynı olması gerekir'''
