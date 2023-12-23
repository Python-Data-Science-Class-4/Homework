import re

def check_ball(owned_ball_number, max_ball_number):
    return owned_ball_number <= max_ball_number

def game_identifier(text):
    pattern = re.compile(r"Game\s(.*)")
    games = pattern.findall(text)
    game_dict = []

    for i in games:
        game_dict.append({
            "id": re.split(":", i)[0],
            "sets": re.findall(r"\d:\s(.*)", i)[0].split("; ")
        })

    return game_dict


def accepted_games(text):
    total_accepted_ids = 0
    ball_num = {
        "red": 12,
        "green": 13,
        "blue": 14
    }
    games = game_identifier(text)
    for i in games:
        is_accepted = True
        for x in i["sets"]:
            for y in x.split(", "):
                num_color = re.split("[ ]", y)
                if check_ball(int(num_color[0]), ball_num[num_color[1]]) == False:
                    is_accepted = False
                    break     
            if is_accepted == False:
                break
        
        if is_accepted:
            # print(i["id"])
            total_accepted_ids += int(i["id"])
        
    return total_accepted_ids

                



with open("./WEEK-7 FILES - REGEX/src/puzzle_input.txt", "r") as file:
    text = file.read()


games = accepted_games(text)
print(games)
