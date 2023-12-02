import re

test_case = "testcase.txt"
sum = 0

nums = {
     "one" : 1,
     "two" : 2,
     "three" : 3,
     "four" : 4,
     "five" : 5,
     "six" : 6,
     "seven" : 7,
     "eight" : 8,
     "nine" : 9
}

def process_string(input):
    #find first number
    first_digit = helper(input, False)
    #find second 
    second_digit = helper(reversed(input), True)
    return int(str(first_digit) + str(second_digit))
              
def helper(input, rev):
    digit = -1
    sub_string = ""
    for char in input:
            if not rev:
                sub_string += char
            else:
                 sub_string = char + sub_string
            if char.isdigit():
                    digit = int(char)
                    return digit
            for key in nums.keys():
                if key in sub_string:
                    digit = nums.get(key)
                    return digit
   


with open(test_case, "r") as f:
    while True:
            cur = f.readline()
            if not cur:
                 break
            sum += process_string(cur)
print(sum)

