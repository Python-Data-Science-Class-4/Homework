def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
# it will return True if it is a prime number

prime_list = []

while True:
    try:
        sayi = int(input("Please enter a number greater than 1"))
    except ValueError:
        print("Invalid number, please re-enter")
        continue

    if sayi <= 0:
        print("Lutfen pozitif bir sayi giriniz!")
        continue

    print(f"{sayi}'ya kadar olan asal sayilar:")

    for i in range(2, sayi+1):
        if is_prime(i):
            prime_list.append(i)

    print(prime_list)
    prime_list = []
    is_continue = input("Do you want to continue? y or n")
    if is_continue.lower() != "y":
        break


    