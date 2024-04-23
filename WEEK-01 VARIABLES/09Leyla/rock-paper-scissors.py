#Rock-Paper-Scissors Take the names of the players and play the stone - paper - scissors game. 
#game 10 hands it will last. At the end of 10 hands, the winner will be determined. 
#The score will be displayed at the end.m?isFullScreen=true

status=True
paper=1
stone=2
scissors=3
sayac=10
print(" Welcome to our game!\n For paper click  1 \nFor stone click  2 \nFor scissors click 3\n")
for x in range (0,10):
        player1=int(input("Player 1: "))
        player2=int(input("Player 2: "))
        if(player1==paper and player2==paper): #paper&paper
            print("You equal, please try again")
            sayac-=1
            #if sayac==0:status=False

        elif(player1==stone and player2==stone): #stone&stone
            print("You equal, please try again")
            sayac-=1
            #if sayac==0:False

        elif(player1==scissors and player2==scissors): #scissors&scissors
            print("You equal, please try again")
            sayac-=1
            #if sayac==0:False
      #_______________________________________________________

        elif player1==paper and player2==stone: #paper&stone
            print("Win Player 1")
            sayac-=1
            #if sayac==0:False

        elif player1==stone and player2==paper:  #stone&paper
            print("Win Player 2")
            sayac-=1
            #if sayac==0:False

        elif player1==scissors and player2==paper: #scissors&paper
            print("Win Player 2")
            sayac-=1
            #if sayac==0:False

        elif player1==paper and player2==scissors:#paper&scissors
            print("Win player 2")
            sayac-=1
            #if sayac==0:False

        elif player1==stone and player2==scissors:#stone&scissors
            print("Win player 1")
            sayac-=1
            #if sayac==0:False

        elif  player1==scissors and player2==stone: #scissors&stone
               print("Win player 2")
               sayac-=1
               #if sayac==0:False

        else:
            print("Please make your choose") 
            
            #if sayac==0:False

        #problem: my code is not stopped after 10 times