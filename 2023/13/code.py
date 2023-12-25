# Advent of code Year 2023 Day 13 solution
# Author = jdanml
# Date = December 2023

import numpy as np

def create_arrays(input_string):
    # Split the input string into separate strings for each array
    array_strings = input_string.strip().split("\n\n")

    # Convert each string into a numpy array and store them in a list
    arrays = [np.array([list(row) for row in array_string.split("\n")]) for array_string in array_strings]

    return arrays

def find_reflection(array):
    result = 0
    horizontal_failures = 0
    vertical_failures = 0
    horizontal_array = array
    candidate_horizontal = []
    candidate_vertical = []
    discarded_horizontal = []
    discarded_vertical = []
    for i in range(len(horizontal_array)):
        print(f"i: {i}")
        if np.array_equal(horizontal_array[i], horizontal_array[i-1]):
                j = i - 2
                k = i + 1
                print(f"candidate line: {i}")
                candidate_horizontal.append(i)
                while j >= 0 and k < len(horizontal_array):
                    print(f"j: {j}, k: {k}")
                    print(f"j: {horizontal_array[j]}, k: {horizontal_array[k]}")
                    if np.array_equal(horizontal_array[j], horizontal_array[k]):
                        j -= 1
                        k += 1
                    else:
                        discarded_horizontal.append(i)
                        horizontal_failures += 1
                        break
    vertical_array = np.transpose(array)
    for i in range(len(vertical_array)):
        print(f"i: {i}")
        if np.array_equal(vertical_array[i], vertical_array[i-1]):
            j = i - 2
            k = i + 1
            print(f"candidate line: {i}")
            candidate_vertical.append(i)
            while j >= 0 and k < len(vertical_array):
                print(f"j: {j}, k: {k}")
                print(f"j: {vertical_array[j]}, k: {vertical_array[k]}")
                if np.array_equal(vertical_array[j], vertical_array[k]):
                    j -= 1
                    k += 1
                else:
                    discarded_vertical.append(i)
                    vertical_failures += 1
                    break
    if 0 in candidate_horizontal:
        candidate_horizontal.remove(0)
    if 0 in candidate_vertical:
        candidate_vertical.remove(0)
    for i in discarded_horizontal:
        if i in candidate_horizontal:
            candidate_horizontal.remove(i)
    for i in discarded_vertical:
        if i in candidate_vertical:
            candidate_vertical.remove(i)
    print(f"candidate horizontal: {candidate_horizontal}")
    print(f"candidate vertical: {candidate_vertical}")
    print(f"horizontal failures: {horizontal_failures}")
    print(f"vertical failures: {vertical_failures}")
    print(f"discarded horizontal: {discarded_horizontal}")
    print(f"discarded vertical: {discarded_vertical}")
    if (len(candidate_horizontal) != 0 and horizontal_failures == 0) or (len(candidate_vertical) == 0  and len(candidate_horizontal) != 0):
        result = candidate_horizontal[0]*100
    elif (len(candidate_vertical) != 0 and vertical_failures == 0) or (len(candidate_vertical) != 0  and len(candidate_horizontal) == 0):
        result = candidate_vertical[0]
    return result

# def find_reflection(array):
#     horizontal_array = array
#     if np.array_equal(horizontal_array[int(len(horizontal_array)/2)], horizontal_array[(int(len(horizontal_array)/2))+1]):
#         return (((len(horizontal_array)+1)/2))*100
#     else:
#         vertical_array = np.transpose(array)
#         if np.array_equal(vertical_array[int(len(vertical_array)/2)], vertical_array[(int(len(vertical_array)/2))+1]):
#                 return (((len(vertical_array)+1)/2))

input_string = """#.######.#.#.
##.##.###...#
#.....#....##
.#.......###.
.#.......###.
##....#....##
##.##.###...#
#.######.#.#.
#.#.##.#.#.##
..#.########.
..#.########.
#.#.##.#.#.##
#.######.#.#.
"""

arrays = create_arrays(input_string)
sum = 0
for array in arrays:
    sum += find_reflection(array)

print(sum)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

arrays = create_arrays(input)
sum_p1 = 0
for array in arrays:
    print(array)
    if find_reflection(array) == 0:
        print("ERROR")
        break
    sum_p1 += find_reflection(array)
    print(sum_p1)


print("Part One : "+ str(sum_p1))



print("Part Two : "+ str(None))