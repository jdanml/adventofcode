# Advent of code Year 2024 Day 4 solution
# Author = jdanml
# Date = December 2024

def count_occurrences(line, substrings):
    counts = {substring: 0 for substring in substrings}
    for substring in substrings:
        counts[substring] += line.count(substring)
    return counts

def transpose(matrix):
    return [''.join(row) for row in zip(*matrix)]

def get_diagonals(matrix):
    diagonals = []
    n, m = len(matrix), len(matrix[0])
    
    # Get diagonals from top-left to bottom-right
    for d in range(n + m - 1):
        diag1, diag2 = [], []
        for i in range(max(0, d - m + 1), min(n, d + 1)):
            diag1.append(matrix[i][d - i])
            diag2.append(matrix[i][m - 1 - (d - i)])
        diagonals.append(''.join(diag1))
        diagonals.append(''.join(diag2))
    
    return diagonals

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

substrings = ["XMAS", "SAMX"]
total_counts = {substring: 0 for substring in substrings}

# Process horizontally
for line in input:
    counts = count_occurrences(line, substrings)
    for substring in substrings:
        total_counts[substring] += counts[substring]

# Process vertically
transposed_input = transpose(input)
for line in transposed_input:
    counts = count_occurrences(line, substrings)
    for substring in substrings:
        total_counts[substring] += counts[substring]

# Process diagonally
diagonals = get_diagonals(input)
for line in diagonals:
    counts = count_occurrences(line, substrings)
    for substring in substrings:
        total_counts[substring] += counts[substring]

print("Part One : "+ str(total_counts["XMAS"] + total_counts["SAMX"]))

def count_x_shapes(matrix):
    n, m = len(matrix), len(matrix[0])
    count = 0
    
    for i in range(1, n - 1):
        for j in range(1, m - 1):
            if matrix[i][j] == 'A':
                upper_left = matrix[i - 1][j - 1]
                upper_right = matrix[i - 1][j + 1]
                bottom_left = matrix[i + 1][j - 1]
                bottom_right = matrix[i + 1][j + 1]
                
                if (upper_left == 'M' and upper_right == 'M' and bottom_left == 'S' and bottom_right == 'S') or \
                   (upper_left == 'S' and upper_right == 'S' and bottom_left == 'M' and bottom_right == 'M') or \
                   (upper_left == 'S' and upper_right == 'M' and bottom_left == 'S' and bottom_right == 'M') or \
                   (upper_left == 'M' and upper_right == 'S' and bottom_left == 'M' and bottom_right == 'S'):
                    count += 1
    
    return count

total_count_x_shapes = count_x_shapes(input)

print("Part Two : "+ str(total_count_x_shapes))