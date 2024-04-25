import re

sum_list=[]
with open(r'C:\Users\Gebruiker\Desktop\Python\Week7\src\puzzle_input.txt', 'r') as my_file:
    my_file.seek(0)
    number=0
    for i in my_file.readlines():
        number+=1   #It is the number of games.
        #It shows the number of green cubes recorded in each game.
        result=re.findall(r"\d+\ green",i)  #13
        #It shows the number of red cubes recorded in each game.
        result1=re.findall(r"\d+\ red",i)  #12
        #It shows the number of blue cubes recorded in each game.
        result2=re.findall(r"\d+\ blue",i)  #14

        #It checks if the recorded number of green cubes is greater than 13. 
        #If it is, the game cannot be played. The game number is then added to the list.
        for k in range(len(result)):
            if int(re.search(r"\d+",result[k]).group())>13:
                sum_list.append(number)
                break
        #It checks if the recorded number of red cubes is greater than 12.
        #If it is, the game cannot be played. The game number is then added to the list.
        for k in range(len(result1)):
            if int(re.search(r"\d+",result1[k]).group())>12:
                sum_list.append(number)
                break
        #It checks if the recorded number of blue cubes is greater than 14.
        #If it is, the game cannot be played. The game number is then added to the list.
        for k in range(len(result2)):
            if int(re.search(r"\d+",result2[k]).group())>14:
                sum_list.append(number)
                break
            
#The sum of game numbers that cannot be played.
sum_set= sum(set(sum_list))       
#The sum of all game numbers   
sum_game=sum([i for i in range(1,101)])
print(sum_game-sum_set)
