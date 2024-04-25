import random

def print_score(winner,player_1_round,player_2_round,score):
    print(f"""    {Player1}:{player_1_round}
    {Player2}:{player_2_round}
    ------------
    {winner}, win the ROUND
    ------------
    Currenct Score:
    {Player1}:{score[0]}
    {Player2}:{score[1]}""")

Player1 = input("Please enter Player 1 name")
Player2 = input("Please enter Player 2 name")

round = 1
round_limit = 10

score = [0,0]
options = ["rock", "paper", "scissors"]

while round <= round_limit:
    player_1_round = random.choice(options)
    player_2_round = random.choice(options)
    print(f"ROUND {round} BEGINS")
    if player_1_round == "rock":
        if player_2_round == "paper":
            score[1] += 1
            print_score(Player2,player_1_round,player_2_round,score)
        elif player_2_round == "scissors":
            score[0] += 1
            print_score(Player1,player_1_round,player_2_round,score)
        else:
            print(f"    Both player selected {player_1_round}. It is a draw.")
    elif player_1_round == "paper":
        if player_2_round == "scissors":
            score[1] += 1
            print_score(Player2,player_1_round,player_2_round,score)
        elif player_2_round == "rock":
            score[0] += 1
            print_score(Player1,player_1_round,player_2_round,score)
        else:
            print(f"    Both player selected {player_1_round}. It is a draw.")
    else:
        if player_2_round == "rock":
            score[1] += 1
            print_score(Player2,player_1_round,player_2_round,score)
        elif player_2_round == "paper":
            score[0] += 1
            print_score(Player1,player_1_round,player_2_round,score)
        else:
            print(f"    Both player selected {player_1_round}. It is a draw.")
    
    round += 1

print(f"""END OF THE GAME
      SCORES:
      {Player1}: {score[0]}
      {Player2}: {score[1]}
      -----
      END OSCARD GOES TOOOOO : {Player1 if score[0]>score[1] else Player2}""")