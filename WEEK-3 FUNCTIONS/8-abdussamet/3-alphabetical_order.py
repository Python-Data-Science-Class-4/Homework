'''
3-alphabetical_order
AralarÃÂ±nda tire (-) bulunan farklÃÂ± kelimelerin girdisini alan bir fonksiyon yazÃÂ±n ve ardÃÂ±ndan:

Kelimeleri alfabetik sÃÂ±raya gÃÂ¶re sÃÂ±ralar, aralarÃÂ±na tire simgesi (-) ekler, sÃÂ±ralanan kelimelerin ÃÂ§ÃÂ±ktÃÂ±sÃÂ±nÃÂ± verir.

ÃÂrnek:

giris >>> yesil-kirmizi-sari-siyah-beyaz

cikis >>> beyaz-kırmızı-sarı-siyah-yesil

'''
def words(sozcuk):

    return '-'.join(sorted(text.split('-')))


text=input('kelimeler giriniz')
print(words(text))





