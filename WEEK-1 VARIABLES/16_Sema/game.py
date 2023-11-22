import random
hand=["stone","paper","scissors"]

def game(name1,name2):
    result1=0
    result2=0
    for a in range(10):
        player1=random.choice(hand)
        player2=random.choice(hand)
        print(a,player1,player2)
        if(player1==player2):
            print("You are equal")
        elif ((player1=="stone")and(player2=="paper")):
            result2+=1
        elif ((player1=="stone")and(player2=="scissors")):
            result+=1
        elif ((player2=="stone")and(player1=="scissors")):
            result2+=1
        elif ((player2=="stone")and(player1=="paper")):
            result1+=1
        elif ((player2=="paper")and(player1=="scissors")):
            result1+=1
        elif ((player1=="paper")and(player2=="scissors")):
            result2+=1
        elif ((player1=="scissors")and(player2=="stone")):
            result2+=1
    if(result1>result2):
        print(name1," You Win!")
    else:
        print(name2, "You Win!")

name1 = input("Enter Player 1's name: ")
name2 = input("Enter Player 2's name: ")

game(name1, name2)