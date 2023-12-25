# Advent of code Year 2023 Day 1 solution
# Author = jdanml
# Date = December 2023

import re
import itertools

def count_arrangements(line, part=1):
    tiles, groups = line.split()
    if part == 2:
        tiles = tiles * 5
        groups = groups + ','
        groups = groups * 5
        groups = groups[:-1]
        print(tiles, groups)
    groups = list(map(int, groups.split(',')))
    groups = [str(x) for x in groups]
    unknown_tiles = tiles.count('?')
    arrangements = 0

    for combination in itertools.product(['.', '#'], repeat=unknown_tiles):
        new_tiles = tiles
        for c in combination:
            new_tiles = new_tiles.replace('?', c, 1)
        found_groups = [str(len(x)) for x in re.findall(r'#+', new_tiles)]
        if found_groups == groups:
            arrangements += 1

    return arrangements


input_data = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

for line in input_data.splitlines():
    print(count_arrangements(line))

with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

arrangements = 0
for line in input.splitlines():
    arrangements += count_arrangements(line)

print("Part One : " + str(arrangements))

# arrangements_p2 = 0
# for line in input.splitlines():
#     arrangements_p2 += count_arrangements(line, 2)

# print("Part Two : " + str(arrangements_p2))
