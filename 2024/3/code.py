# Advent of code Year 2024 Day 3 solution
# Author = jdanml
# Date = December 2024

import re

# Regular expression to find all mul(number, number) patterns
pattern = re.compile(r'mul\((\d+),(\d+)\)')

# Regular expression to find all mul(number, number) patterns
pattern_p2 = re.compile(r'(don\'t\(\))|(do\(\))|(mul\((\d+),(\d+)\))')

sum_p1 = 0
sum_p2 = 0

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    # Find all matches
    matches = pattern.findall(input)

    # Multiply the numbers and store the results
    results = [(int(a), int(b), int(a) * int(b)) for a, b in matches]

    # Print the results
    for a, b, product in results:
       sum_p1 += product

    matches_p2 = pattern_p2.findall(input)
    enabled = True

    # Process the matches
    for match in matches_p2:
        if match[0]:  # don't() instruction
            enabled = False
        elif match[1]:  # do() instruction
            enabled = True
        elif match[2] and enabled:  # mul(a, b) instruction and enabled
            a, b = int(match[3]), int(match[4])
            sum_p2 += a * b

print("Part One : "+ str(sum_p1))



print("Part Two : "+ str(sum_p2))