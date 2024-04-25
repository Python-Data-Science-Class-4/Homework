# Week7-Homework

## Question 1:
Write a program that detects the ID number hidden in a text. We know that the format of the ID number is 2 letters, 1 digit, 2 letters, 2 digits, 1 letter, 1 digit (For example: AA4ZA11B1).

Input : AABZA1111AEGTV5YH678MK4FM53B6
Output : MK4FM53B6

Input : AEGTV5VZ4PF94B6YH678
Output : VZ4PF94B6

## Question 2:
Search for eight-letter words within the text file named "eight_letter" located in the src folder and print them.

## Question 3:
Create a function that identifies and lists email addresses without domain names within a given text. 

Example:

sample_text =  "The advencements in biomarine studies franky@google.com with the investments necessary and Davos sinatra123@yahoo.com. Then New Yorker article on wind farms..."

Output :
["franky","sinatra123"]

## Question 4: 
You're playing a game with your friend. He shows shows you a small bag and some cubes which are either red, green, or blue. Each time you play this game, he will hide a secret number of cubes of each color in the bag, and your goal is to figure out information about the number of cubes.

To get information, once a bag has been loaded with cubes, he will reach into the bag, grab a handful of random cubes, show them to you, and then put them back in the bag. He'll do this a few times per game.

You play several games and record the information from each game (your puzzle input in the src folder). Each game is listed with its ID number (like the 11 in Game 11: ...) followed by a semicolon-separated list of subsets of cubes that were revealed from the bag (like 3 red, 5 green, 4 blue).

For example, the record of a few games might look like this:

Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
In game 1, three sets of cubes are revealed from the bag (and then put back again). The first set is 3 blue cubes and 4 red cubes; the second set is 1 red cube, 2 green cubes, and 6 blue cubes; the third set is only 2 green cubes.

Your friend would like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes?

In the example above, games 1, 2, and 5 would have been possible if the bag had been loaded with that configuration. However, game 3 would have been impossible because at one point he showed you 20 red cubes at once; similarly, game 4 would also have been impossible because he showed you 15 blue cubes at once. 

So you have game 1,2, and 5. If you add up the IDs of the games that would have been possible, you get 8.

Determine which games would have been possible if the bag had been loaded with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?


## Optional Questions on hackerrank :
1. [Matching Anything But a Newline](https://www.hackerrank.com/challenges/matching-anything-but-new-line/problem)
2. [Matching Specific String](https://www.hackerrank.com/challenges/matching-specific-string/problem)
3. [Matching Digits & Non-Digit Characters](https://www.hackerrank.com/challenges/matching-digits-non-digit-character/problem)
4. [Matching Whitespace & Non-Whitespace Character](https://www.hackerrank.com/challenges/matching-whitespace-non-whitespace-character/problem)
5. [Matching Word & Non-Word Character](https://www.hackerrank.com/challenges/matching-word-non-word/problem)
6. [Matching Start & End](https://www.hackerrank.com/challenges/matching-start-end/problem)
7. [Matching Specific Characters](https://www.hackerrank.com/challenges/matching-specific-characters/problem)
8. [Excluding Specific Characters](https://www.hackerrank.com/challenges/excluding-specific-characters/problem)
