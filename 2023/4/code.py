# Advent of code Year 2023 Day 4 solution
# Author = jdanml
# Date = December 2023

# Imports
from collections import Counter


def count_matching_numbers(line):
    card_id, numbers = line.split(":")
    card_id = int(line.split()[1].rstrip(":"))
    left, right = numbers.split("|")
    left_numbers = set(map(int, left.split()))
    right_numbers = map(int, right.split())
    count = sum(1 for number in right_numbers if number in left_numbers)
    return int(card_id), int(count)


# input_string = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    sum_p1 = 0
    for line in input.splitlines():
        line = line.strip()
        _, power = count_matching_numbers(line)
        if power > 0:
            sum_p1 += 2 ** (power - 1)

    sum_p2 = 0
    card_count = []
    for line in input.splitlines():
        line = line.strip()
        card_id, power = count_matching_numbers(line)
        card_count.append(card_id)
        if power > 0:
            # print (power)
            new_cards = list(range((card_id + 1), (card_id + power + 1), 1))
            # print (new_cards)
            # print (f"Card {card_id} has {(card_count.count(card_id))} instances")
            for i in range(0, (card_count.count(card_id))):
                card_count.extend(new_cards)
            # print (card_count)
        element_counts = Counter(card_count)
    print (element_counts)
    sum_p2 = len(card_count)


print("Part One : " + str(sum_p1))


print("Part Two : " + str(sum_p2))
