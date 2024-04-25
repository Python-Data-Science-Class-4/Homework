while True:
    asal_sayi = []
    number = int(input("Enter a number: "))
    for i in range(2,number):
        is_divisible = False
        for x in range(2,i):
            if (i % x == 0):
                is_divisible = True
        if is_divisible == False:
            asal_sayi.append(i)
    print(asal_sayi)
    game_over = input("Devam etmek icin 1'e, cikmak icin q'ya basin.\n")
    if game_over == 'q' or game_over == 'Q':
        break    

    