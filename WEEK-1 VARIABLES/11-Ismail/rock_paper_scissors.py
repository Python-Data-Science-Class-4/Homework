#Rock-Paper-Scissors we will take the names of the players and play the stone - paper - scissors game. 
#After 10 hands the game will last. At the end of 10 hands, the winner will be determined. The score will be displayed at the end.
options=["ROCK","PAPER","SCISSORS"]
player1_name=input("Enter Player Name:") 
player2_name=input("Enter Player Name:")
player1_score=0 
player2_score=0
for i in range (0,11): #it will turn ten times
    
    player1=input(f"{player1_name}, ROCK/PAPER/SCISSORS?").upper() #we used format"upper" because of the two choises of user
    player2=input(f"{player2_name}, ROCK/PAPER/SCISSORS?").upper()
    
    if player1==options[0] and player2==options[1]:
        player2_score+=1
        print("Win!", player2_name,player2_score)
        
    elif player1==options[0] and player2==options[2]:
        player1_score+=1
        print("Win!!",player1_name,player1_score)
    elif player1==options[1] and player2==options[0]:
        player1_score+=1
        print("Win!",player1_name,player1_score)
    elif player1==options[1] and player2==options[2]:
        player2_score+=1
        print("Win!",player2_name,player2_score)
    elif player1==options[2] and player2==options[0]:
        player2_score+=1
        print("Win!",player2_name,player2_score)
    elif player1==options[2] and player2==options[1]:
        player1_score+=1
        print("Win!",player1_name,player1_score)    
    else:
        print("Draw!")
    
    
print("Result:\n",player1_name,player1_score,"\n",player2_name,player2_score) # we will see the results end of the game. 