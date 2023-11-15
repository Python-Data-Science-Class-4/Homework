player1 = input("İlk oyuncunun adını girin: ")
player2 = input("İkinci oyuncunun adını girin: ")

score1 = 0
score2 = 0

for i in range(10):
    print(f"El {i + 1}:")
    choice1 = input(f"{player1}, taş (t), kağıt (k) veya makas (m) seçin: ").lower()
    choice2 = input(f"{player2}, taş (t), kağıt (k) veya makas (m) seçin: ").lower()

    if choice1 == choice2:
        print("Berabere!")
    elif (choice1 == "t" and choice2 == "m") or (choice1 == "k" and choice2 == "t") or (choice1 == "m" and choice2 == "k"):
        print(f"{player1} bu eli kazandı!")
        score1 += 1
    else:
        print(f"{player2} bu eli kazandı!")
        score2 += 1

if score1 > score2:
    print(f"{player1} oyunu {score1}-{score2} skorla kazandı!")
elif score2 > score1:
    print(f"{player2} oyunu {score2}-{score1} skorla kazandı!")
else:
    print("Oyun berabere bitti!")
