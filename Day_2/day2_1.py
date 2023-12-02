import re
sum = 0
test_case = "Day_2\\testcase.txt"
test = "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"


def process_string(input):
    game_num = re.sub(":", "", input.split(" ")[1])
    game_set_list = input[7:].split(";")

    for game_set in game_set_list:
        colors = game_set.split(",")
        for color in colors:
            color_num = int(color.split(" ")[1])
            if "red" in color:
                if color_num > 12: return 0
            if "green" in color:
                if color_num > 13: return 0
            if "blue" in color:
                if color_num > 14: return 0
    return game_num

with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            sum += int(process_string(cur))
print(sum)