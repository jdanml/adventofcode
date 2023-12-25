# Advent of code Year 2023 Day 15 solution
# Author = jdanml
# Date = December 2023

def process_string(s):
    current_value = 0
    for char in s:
        ascii_code = ord(char)
        current_value += ascii_code
        current_value *= 17
        current_value %= 256
    return current_value

input_string="HASH"
input_string_2="rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

print(process_string(input_string))

values = 0
for string in input_string_2.split(","):
    values += process_string(string)

print(values)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

values_p1 = 0
for string in input.split(","):
    values_p1 += process_string(string)

print("Part One : "+ str(values_p1))



print("Part Two : "+ str(None))