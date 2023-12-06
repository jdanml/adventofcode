# Advent of code Year 2023 Day 6 solution
# Author = jdanml
# Date = December 2023

# Imports
import math

def count_winning_scenarios(time, distance):
    hold_time = 0
    win_count = 0
    for hold_time in range(hold_time, time):
        distance_traveled = (time - hold_time) * hold_time
        if distance_traveled > distance:
            win_count += 1
    return win_count


# input_string = """Time:      7  15   30
# Distance:  9  40  200
# """

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    time = []
    distance = []
    for index, line in enumerate(input.splitlines()):
        line = line.strip()
        _, params = line.split(":")
        if index == 0:
            time = list(map(int, params.split()))
        else:
            distance = list(map(int, params.split()))

    win_count = []
    for t, d in zip(time, distance):
        win_count.append(count_winning_scenarios(t, d))

    margin = math.prod(win_count)

    time_p2 = []
    distance_p2 = []
    for index, line in enumerate(input.splitlines()):
        line = line.strip()
        _, params = line.split(":")
        if index == 0:
            time_p2 = int(params.replace(" ", ""))
        else:
            distance_p2 = int(params.replace(" ", ""))

    win_count_p2 = []
    win_count_p2.append(count_winning_scenarios(time_p2, distance_p2))

    margin_p2 = math.prod(win_count_p2)
    
print("Part One : " + str(margin))


print("Part Two : " + str(margin_p2))
