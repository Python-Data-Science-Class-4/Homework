def is_possible_game(subsubsets):
    expected_counts = {'red': 12, 'green': 13, 'blue': 14}

    for subset in subsubsets:
        for item in subset:
            count, color = item.split()

        if int(count) > expected_counts[color]:
            return False

    return True

def possible_games_sum(input_text):
    games = input_text.strip().split('Game')
    possible_games = []

    for game in games[1:]:  # Skip the first element (empty string before the first 'Game')
        game_info = game.split(':')
        print (game_info)
        game_id = int(game_info[0].strip())
        subsubsets = [subsubset.strip().split(', ') for subset in game_info[1:] for subsubset in subset.split(';')]

        print (subsubsets)
        
        if is_possible_game(subsubsets):
            possible_games.append(game_id)

    return sum(possible_games)

# Read input from the file
file_path = 'WEEK-7 FILES - REGEX/3-Yusuf/src/game_records.txt'
try:
    with open(file_path, 'r') as file:
        input_text = file.read()
        result = possible_games_sum(input_text)
        print(result)

except Exception as e:
    print(f"An error occurred: {e}")
