'''
Write a function that outputs the transcription of an input number with two digits.

Example:
28---------------->Twenty Eight
'''

giris=int(input('Bir sayi giriniz:') )

number=[1,2,3,4,5,6,7,8,9]
birler=['one','two','three','four','five','six','seven','eight','nine']
onlar=['ten','twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninety']
tens=['ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']


def x(giris):
    k=()
    l=()
    for i in range(0,10):
    
        if giris // 10!= 1 and giris % 10!= 0  :
            
            if giris // 10==i+1:
                k=onlar[i]
            if giris % 10 == i+1:
                l=birler[i]
            y=k,l
          

        elif giris // 10 == 0:
                y=onlar[i]

        else :
            if giris % 10==i:
                y=tens[i]
        
    
    print(y)

x(giris)

# def b():
#     y=birler[1]
#     l=birler[4]

#     return y+l

# print(b)