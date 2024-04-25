import random
print("Welcome to the game")
options = ["Rock", "Paper", "Scissor"]
while True:
    gamer = input("Enter the name of the player: ")
    gamer_score = 0
    computer_score = 0
    while gamer_score != 3 and computer_score != 3:
        computer_option = random.choice(options)
        gamer_option = input("Enter Rock/ Paper/ Scissor :").title()
        print(f"Computer select {computer_option}")
        print(f"{gamer.title()} select {gamer_option}")

        if computer_option == gamer_option:
            print('Tie')
            print(f'''
                    Computer {computer_score} vs {gamer_score} {gamer.title()}
                    ''')
             
        elif (computer_option =='Rock' and gamer_option  == 'Scissor') or (computer_option =='Scissor' and gamer_option =='Paper') or (computer_option =='Paper' and gamer_option =='Rock'):
            print("Computer wins")
            print(f'''
                    Computer {computer_score+1} vs {gamer_score} {gamer.title()}
                    ''')
            if computer_score + 1 == 3:
                print("The winner is computer")
            elif gamer_score + 1 == 3:
                print(f"The winner is {gamer.title()}")
            computer_score += 1
        elif (gamer_option =='Rock' and computer_option  == 'Scissor') or (gamer_option =='Scissor' and computer_option =='Paper') or (gamer_option =='Paper' and computer_option =='Rock'):
            print(f"{gamer.title()} wins")
            print(f'''
                    Computer {computer_score} vs {gamer_score+1} {gamer.title()}
                    ''')
            if computer_score + 1 == 3:
                print("The winner is computer")
            elif gamer_score + 1 == 3:
                print(f"The winner is {gamer.title()}")
            gamer_score += 1
        else:
            print("Choose a valid option to play this game.")
        
    
    game_over = input("Press any key to continue or press enter to quit: ")
    if game_over == "":
        break