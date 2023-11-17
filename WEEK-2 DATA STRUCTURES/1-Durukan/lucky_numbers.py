def lucky_numbers(n):

    num_list = list(range(1,n+1))
    # It creates a list from 1 till the user input

    passed_index = 2

    while len(num_list) > passed_index:
        #while removed indexes are smaller then the length of list, this loop works and updates the list.
        num_list = [num_list[i] for i in range(len(num_list)) if (i+1) % passed_index != 0]
        passed_index += 1
    
    

    print(num_list)

lucky_numbers(n=int(input("Please enter a number: "))) 

'''Kod cok basarili tebrik ederim..
**PEP 8 standartlarına bakip kodlarimizi daha duzenli hale getirebiliriz. Sizin kodlariniz gayet guzel ama bu linki incelerseniz 
daha uygun bi formatla yazmis olursunuz.--->https://peps.python.org/pep-0008/
**Bir onceki odevde de dedigim gibi bunu da fonksiyonsuz yapabilir miydik bir bakalim. Tekrar yuklemenize gerek yok.
Direkt bana gonderebilirsiniz.'''

