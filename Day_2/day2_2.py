import re

sum = 0
test_case = "Day_2\\testcase.txt"

def process_string(input):
    game_set_list = input[7:].split(";")
    max_red = max_green = max_blue = -1

    for game_set in game_set_list:
        colors = game_set.split(",")
        for color in colors:
            color_num = int(color.split(" ")[1])
            if "red" in color:
                if color_num > max_red: max_red = color_num
            if "green" in color:
                if color_num > max_green: max_green = color_num
            if "blue" in color:
                if color_num > max_blue: max_blue = color_num
    return max_red * max_green * max_blue



with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            sum += int(process_string(cur))
print(sum)