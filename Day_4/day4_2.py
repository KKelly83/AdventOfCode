import re

test_case = "Day_4\\testcase.txt"


card_list = []

def process_input(input):
    card_num = re.sub(":", "", input.split(" ")[1])
    processed = re.sub(r"\s+", " ", input[8:]).strip()
    num_sets = [nums.split() for nums in processed.split("|") if nums.strip()]
    winning_nums, card_nums = num_sets[:2]

    card_points = 0

    num_dict = dict()
    for num in winning_nums:
        num_dict.update({num: 1})
    for num in card_nums:
        if num_dict.get(num):
            card_points += 1
    card_list.append((card_points, 1))
         
def handle_copies():
    sum = 0
    for card in range(len(card_list)):
        for copy in range(0, card_list[card][1]):
            for j in range(1, card_list[card][0] + 1):
                card_list[card + j] = (card_list[card + j][0], card_list[card + j][1] + 1)
        sum += card_list[card][1]        
    return sum
         


with open(test_case, "r") as f:
    while True:
            line = f.readline()
            if not line:
                 break
            process_input(line)

print(handle_copies())