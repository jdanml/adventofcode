# Advent of code Year 2023 Day 14 solution
# Author = jdanml
# Date = December 2023

import numpy as np

import numpy as np

def slide_O_to_top(input_string):
    # Convert the input string into a numpy array
    array = np.array([list(row) for row in input_string.split()])

    # Iterate over each column
    for column in range(array.shape[1]):
        # Iterate from the bottom to the top of the column
        for row in range(array.shape[0]-1, 0, -1):
            # Check the conditions and perform the necessary replacements
            if array[row-1, column] == '.' and array[row, column] == 'O':
                array[row-1, column], array[row, column] = 'O', '.'
            elif array[row-1, column] == 'O' and array[row, column] == 'O':
                # Find the topmost '.' or '#' in the column
                for top_row in range(row-2, -1, -1):
                    if array[top_row, column] == '.':
                        array[top_row, column], array[row, column] = 'O', '.'
                        break
                    elif array[top_row, column] == '#':
                        break

    # Convert the array back to a string
    output_string = '\n'.join(''.join(row) for row in array)

    return output_string


# input_string = """O....#....
# O.OO#....#
# .....##...
# OO.#O....O
# .O.....O#.
# O.#..O.#.#
# ..O..#O..O
# .......O..
# #....###..
# #OO..#....
# """

# output = slide_O_to_top(input_string.strip())
# print(output)

# # Split the output into lines
# lines = output.split('\n')
# print(len(lines))

# # Count the number of 'O's in each line
# line_number = len(lines)
# total = 0
# for line in lines:
#     counts = line.count('O')
#     print(counts)
#     total += counts * line_number
#     line_number -= 1
#     print(total)

# print(total)

with open((__file__.rstrip("caode.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

output = slide_O_to_top(input.strip())
print(output)

# Split the output into lines
lines = output.split('\n')
print(len(lines))

# Count the number of 'O's in each line
line_number = len(lines)
total = 0
for line in lines:
    counts = line.count('O')
    total += counts * line_number
    line_number -= 1

print("Part One : "+ str(total))



print("Part Two : "+ str(None))