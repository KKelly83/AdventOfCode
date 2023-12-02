import re

test_case = "testcase.txt"
sum = 0

def process_string(input):
    sanitized = re.sub("\D", "", input)
    num = sanitized[0] + sanitized[len(sanitized) - 1]
    return int(num)

with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            sum += process_string(cur)

print(sum)