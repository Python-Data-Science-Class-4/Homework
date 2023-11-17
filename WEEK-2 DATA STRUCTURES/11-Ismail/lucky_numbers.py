number = int(input('Enter a number: ')) 

lucky_numbers = []

for i in range(1,number+1):
    j=[]
    if number %i==0 :
        j.append(i)
        lucky_numbers.append(j)

print(lucky_numbers)

'''Yazdiginiz kodda girdi olarak verilen sayının bölenlerini buluyor ama bizden istenen farkli bir sey.
Şanslı sayılar oluşturulurken her geçişte belirli bir kurala göre sıralı bir liste oluşturulması gerekiyor.
Odevin aciklamasi su sekilde;
#Original sequence [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22] Remove 2nd elements [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21] 
#Remove 3rd elements [1, 3, 7, 9, 13, 15, 19, 21] 
# Remove 4th elements [1, 3, 7, 13, 15, 19] 
# Remove 5th elements [1, 3, 7, 13, 19] 
# We cannot remove every other 6th element as there is no 6th element. 
# Input 22 Output Lucky numbers are [1, 3, 7, 13, 19].'''
