import re

test_case = "Day_4\\testcase.txt"
sum = 0


def process_input(input):
    processed = re.sub(r"\s+", " ", input[8:]).strip()
    
    num_sets = [nums.split() for nums in processed.split("|") if nums.strip()]
    winning_nums, card_nums = num_sets[:2]

    card_points = 0

    num_dict = dict()
    for num in winning_nums:
        num_dict.update({num: 1})
    for num in card_nums:
        if num_dict.get(num):
            card_points = 1 if card_points == 0 else card_points * 2
    return card_points




with open(test_case, "r") as f:
    while True:
            line = f.readline()
            if not line:
                 break
            sum += process_input(line)
print(sum)