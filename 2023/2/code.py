# Advent of code Year 2023 Day 2 solution
# Author = jdanml
# Date = December 2023

def count_cubes_per_game(line):
    color_counts = {"red": 0, "green": 0, "blue": 0}
    parts = line.split(":")[1].split(";")
    for part in parts:
        cubes = part.split(",")
        for cube in cubes:
            items = cube.strip().split()
            if len(items) == 2:  # handle cases like '9 green'
                count, color = items
                color_counts[color] = max(color_counts[color], int(count))
    return color_counts

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    sum_p1 = 0
    for line in input.splitlines():
        line = line.strip()
        game_id = int(line.split()[1].rstrip(':'))
        color_counts = count_cubes_per_game(line)
        if color_counts['red'] > 12 or color_counts['green'] > 13 or color_counts['blue'] > 14:
            print("Exceeded limit in game:", color_counts)
        else:
            sum_p1 += game_id

    sum_p2 = 0
    for line in input.splitlines():
        line = line.strip()
        color_counts = count_cubes_per_game(line)
        power_set = color_counts['red'] * color_counts['green'] * color_counts['blue']
        sum_p2 += power_set

print("Part One : "+ str(sum_p1))



print("Part Two : "+ str(sum_p2))