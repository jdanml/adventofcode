# Advent of code Year 2023 Day 1 solution
# Author = jdanml
# Date = December 2023

# Imports
import re


def extract_numbers(input_string):
    numbers = re.findall(r"\d", input_string)
    if numbers:
        first_number = numbers[0]
        last_number = numbers[-1]
        return int(str(first_number) + str(last_number))
    else:
        return None, None


def convert_written_numbers_to_digits(input_string):
    number_dict = {
        "zero": "0",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zerone": "01",
        "twone": "21",
        "threeight": "38",
        "fiveight": "58",
        "sevenine": "79",
        "eightwo": "82",
        "nineight": "98",
        "oneight": "18",
    }
    for word in sorted(number_dict.keys(), key=len, reverse=True):
        input_string = input_string.replace(word, number_dict[word])
    return input_string


with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    sum_p1 = 0
    for line in input.splitlines():
        line = line.strip()
        calibration_values = extract_numbers(line)
        sum_p1 += calibration_values

    sum_p2 = 0
    for line in input.splitlines():
        line = convert_written_numbers_to_digits(line.strip())
        calibration_values = extract_numbers(line)
        sum_p2 += calibration_values

print("Part One : " + str(sum_p1))

print("Part Two : " + str(sum_p2))
