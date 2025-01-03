# Advent of code Year 2024 Day 7 solution
# Author = jdanml
# Date = December 2024

import itertools

def calibration_result(result, numbers):
    operators = ["+", "*"]
    operator_combinations = list(itertools.product(operators, repeat=len(numbers)-1))
    
    results = []
    for ops in operator_combinations:
        current_result = numbers[0]
        for i in range(1, len(numbers)):
            if ops[i-1] == "+":
                current_result += numbers[i]
            elif ops[i-1] == "*":
                current_result *= numbers[i]
        results.append(current_result)
    
    if result in results:
        return True
    else:
        return False

def calibration_result_p2(result, numbers):
    operators = ["+", "*", "||"]
    operator_combinations = list(itertools.product(operators, repeat=len(numbers)-1))
    
    results = []
    for ops in operator_combinations:
        current_result = numbers[0]
        for i in range(1, len(numbers)):
            if ops[i-1] == "+":
                current_result += numbers[i]
            elif ops[i-1] == "*":
                current_result *= numbers[i]
            elif ops[i-1] == "||":
                current_result = int(str(current_result) + str(numbers[i]))
        results.append(current_result)
    
    if result in results:
        return True
    else:
        return False
    
with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    sum_p1 = 0
    for line in input.splitlines():
        line = line.strip()
        result, numbers = line.split(":")
        result = int(result)
        numbers = list(map(int, numbers.split()))
        if calibration_result(result, numbers):
            sum_p1 += result

    sum_p2 = 0
    for line in input.splitlines():
        line = line.strip()
        result, numbers = line.split(":")
        result = int(result)
        numbers = list(map(int, numbers.split()))
        if calibration_result_p2(result, numbers):
            sum_p2 += result

print("Part One : "+ str(sum_p1))

print("Part Two : "+ str(sum_p2))