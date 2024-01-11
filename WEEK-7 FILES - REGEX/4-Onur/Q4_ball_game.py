import re

path = "WEEK-7 FILES - REGEX/src/puzzle_input.txt"

cube_counts = {'red': 12, 'green': 13, 'blue': 14}

def is_possible(game):
    # if non_possible game not found the function will return true but if we found impossible game then it will return False
    for set_entry in game['sets']:
        # the set tuple has count and color repeatedly so we need to increase i twice and use 2 
        for i in range(0, len(set_entry), 2):
            # first item in the order is count of ball
            count = int(set_entry[i])
            # second item in the order is color name but we needs to remove "," from the right
            color = set_entry[i + 1].rstrip(',')
            # we get the ball count from respective color and compare and return if possible or not
            if cube_counts.get(color, 0) < count:
                return False
    return True

# we use readlines to get line by line 
with open(path, 'r', encoding='utf-8') as file:
    games = [line.strip() for line in file.readlines()]

results = []

for game in games:
    # left part of ":" belongs to game number and other is set info so we split from : 
    splitted = game.split(":")

    # in first item of splitted text we need to search for digit which represents the number of the game.
    match_id = re.search("(\d+)", splitted[0])
    game_id = match_id.group(1)

    # we apply split ";" to the sets text to receive each set. then we convert the resulted list items to tuple to store count and color.
    # we use if x at the end to prevent null splits because the line might end with ;
    sets = [tuple(x.split()) for x in splitted[1].split(";") if x]
    
    # we add game number and sets to to our list as dictionary
    results.append({"game_id": int(game_id), "sets":sets})

total_count = 0

for game in results:
    game_id = game["game_id"]
    if is_possible(game):
        print(f'Game Id {game_id} is possible')
        total_count += game_id

print(f'Sum of the IDs are: {total_count}')
    







    