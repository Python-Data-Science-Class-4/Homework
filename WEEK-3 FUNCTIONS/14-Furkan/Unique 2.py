
def remove_duplicates(lst):
    unique_list = list(sorted(set(lst)))
    print(unique_list)

numbers = input ("Write a set of numbers: ")
remove_duplicates(numbers)

''' Set kullanmaniz cok guzel ama bir kac duzeltme yapabiliriz.. 
**input fonksiyonu, kullanıcıdan alınan girdiyi bir string olarak alır. 
Sizin amacınız bir dizi sayı girişi almak. Bu yuzden kullanicinin girdigi sayilari diziye donusturmeniz gerekiyor.
**Yukarida belirttigim sebepten dolayi kullanici virgulle sayi girisi yaptiginda virgulu de bir sayi gibi algilayip 
islem yapiyor.'''
