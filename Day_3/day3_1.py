import re

test_case = "Day_3\\testcase.txt"

engine = []

def process_engine(engine):
      sum = 0
      for row in range(len(engine)):
            num = ""
            for col in range(len(engine[row])):
                char = engine[row][col]
                if char.isdigit():
                    num = str(num) + str(char)
                    if col == len(engine[row])-1: #edge case: no "." after number
                         if find_symbols(engine, num, row, col):
                              sum += int(num)
                if not char.isdigit():
                    if len(num) > 0:
                          if find_symbols(engine, num, row, col):
                               sum += int(num)
                          num = ""
                    else:
                         num = ""
      return sum


def find_symbols(engine, num, row, col):
    sub_engine = ""

    for i in range(row - 1, row + 2):
         for j in range(col - len(num) - 1, col + 1):
            if i > len(engine) - 1 or j < 0:
                 continue
            sub_engine = sub_engine + str(engine[i][j])
    sub_engine = re.sub(r'[A-Za-z0-9.]', '', sub_engine)
    if len(sub_engine) > 0:
         return True
    return False

with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            engine.append(cur)

for i in range(len(engine)):
     engine[i] = re.sub("\n", "", engine[i])
           
print(process_engine(engine))