# Advent of code Year 2023 Day 9 solution
# Author = jdanml
# Date = December 2023


def calculate_differences(lst):
    return [j - i for i, j in zip(lst[:-1], lst[1:])]


input_string = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    extrapolations = []
    for line in input.splitlines():
        input = list(map(int, line.split()))

        diffs = [input]
        while diffs[-1] != [0] * (len(input) - len(diffs) + 1):
            diffs.append(calculate_differences(diffs[-1]))

        diffs[-1].append(0)

        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].append(diffs[i][-1] + diffs[i + 1][-1])

        extrapolations.append(diffs[0][-1])

    result_p1 = sum(extrapolations)

print("Part One : " + str(result_p1))

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    extrapolations = []
    for line in input.splitlines():
        input = list(map(int, line.split()))

        diffs = [input]
        while diffs[-1] != [0] * (len(input) - len(diffs) + 1):
            diffs.append(calculate_differences(diffs[-1]))

        diffs[-1].insert(0, 0)

        for i in range(len(diffs) - 2, -1, -1):
            diffs[i].insert(0, diffs[i][0] - diffs[i + 1][0])

        extrapolations.append(diffs[0][0])
    result_p2 = sum(extrapolations)

print("Part Two : " + str(result_p2))
