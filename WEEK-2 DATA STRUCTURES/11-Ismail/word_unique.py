# Write a program that takes in two words as input and returns a list containing three elements,
# in the following order Shared letters between two words. Letters unique to word 1. Letters unique to word 2. 
# Each element of the output should have unique letters, and should be alphabetically sorted. Use set operations. 
# The strings will always be in lowercase and will not contain any punctuation.
# Example Input1 sharp Input2 soap Output ['aps', 'hr', 'o']


#Entering two unique words
word1= str(input("Enter a word:"))
word2= str(input("Enter a word:"))

#convert to set as wrd1 and wrd2
wrd1= set(word1)
wrd2= set(word2)

sharedletters= (wrd1 & wrd2) #pull the shared letters
differenceletters1= (wrd1-wrd2)#different letters from second one
differenceletters2= (wrd2-wrd1)#different letters from fist one

letters=(sharedletters,differenceletters1,differenceletters2) 
result= sorted((letters),key=letters.index) #convert a list and sort 

print ( result)

''' Kod gayet guzel ama bir kac oneri..
**Kullanıcının girdilerini doğrudan küçük harfe çevirerek (.lower() ile) hepsini küçük harfle işleyip biraz daha güvenli hale getirebiliriz.
**sorted() fonksiyonu kullanarak sonuçları alfabetik sıraya sokabiliriz.Sadece sonuc kisminda degil de islem yaptiginiz yerde de kullanmaniz gerekiyor.
**Kodu daha açıklanabilir ve Pythonic hale getirmek için değişken adlarını değiştirebiliriz.
ornegin sharedletters yerine shared_letters gibi.'''
