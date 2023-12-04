import re

test_case = "Day_3\\testcase.txt"

engine = []
asterisk_dict = dict()

def process_engine(engine):
    sum = 0
    for row in range(len(engine)):
        num = ""
        for col in range(len(engine[row])):
            char = engine[row][col]
            if char.isdigit():
                num = str(num) + str(char)
                if col == len(engine[row])-1: #edge case: no "." after number
                        find_ratios(engine, num, row, col)

            if not char.isdigit():
                if len(num) > 0:
                    find_ratios(engine, num, row, col)
                    num = ""
                else:
                        num = ""
    for key, value in asterisk_dict.items():
         if len(value) > 1:
              ratio = 1
              for num in value:
                   ratio *= int(num)
              sum += ratio
    return sum
                   

def find_ratios(engine, num, row, col):
    sub_engine = ""

    for i in range(row - 1, row + 2):
         for j in range(col - len(num) - 1, col + 1):
            if i > len(engine) - 1 or j < 0:
                 continue
            character = str(engine[i][j])
            if character == "*":
                 if (i,j) in asterisk_dict:
                    temp = asterisk_dict.get((i,j))
                    temp.append(num)
                    asterisk_dict.update({(i,j) : temp})
                 else:
                    asterisk_dict.update({(i,j) : [num]})
                 break

with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            engine.append(cur)

for i in range(len(engine)):
     engine[i] = re.sub("\n", "", engine[i])
           
print(process_engine(engine))