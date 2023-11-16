# Assignment 2.1
# Rock-Paper-Scissors

# Input for the names of players
player1_name = input("Enter Player 1's name: ")
player2_name = input("Enter Player 2's name: ")

# Assign a variable name for the scores
player1_score=0
player2_score=0
players_even_score=0

for i in range(1, 2):
    # Input for the choices
    player1 = input(f"{player1_name}, enter your choice (rock/paper/scissors): ").lower()
    player2 = input(f"{player2_name}, enter your choice (rock/paper/scissors): ").lower()
    
    # Who is the winner for each round?
    if player1 == player2:
        players_even_score+=1
    elif (player1 == "rock" and player2 == "scissors") or (player1 == "scissors" and player2 == "paper") or (player1 == "paper" and player2 == "rock"):
        player1_score += 1
    else:
        player2_score += 1
        
print(f"{player1_name} = {player1_score} vs {player2_name} = {player2_score}")    
# Who is the winner overall?
if player1_score > player2_score:
    print(player1_name + " is the winner!")
elif player2_score > player1_score:
    print(player2_name + " is the winner!")
else:
    print("EVEN!")