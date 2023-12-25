# Advent of code Year 2023 Day 11 solution
# Author = jdanml
# Date = December 2023

# Imports
from itertools import combinations

# Add a line of '.' if any line, horizontally or vertically, only contains '.'
def expand_universe(grid):
    # Convert each string in the grid to a list of characters
    grid = [list(row) for row in grid]

    rows_to_add = [i for i in range(len(grid)) if all(cell == '.' for cell in grid[i])]
    cols_to_add = [i for i in range(len(grid[0])) if all(grid[j][i] == '.' for j in range(len(grid)))]

    for i in sorted(rows_to_add, reverse=True):
        grid.insert(i+1, ['.'] * len(grid[0]))

    for i in sorted(cols_to_add, reverse=True):
        for row in grid:
            row.insert(i+1, '.')
    return grid

# Add 1000000 lines of '.' if any line, horizontally or vertically, only contains '.'
def expand_universe_p2(grid):
    # Convert each string in the grid to a list of characters
    grid = [list(row) for row in grid]

    # Find empty rows and columns
    empty_rows = [i for i, row in enumerate(grid) if all(cell == '.' for cell in row)]
    empty_cols = [i for i in range(len(grid[0])) if all(grid[j][i] == '.' for j in range(len(grid)))]

    # Find galaxies
    galaxies = [[i, j] for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '#']

    # Handle expansion on these galaxies
    for galaxy in galaxies:
        galaxy[0] += sum(row < galaxy[0] for row in empty_rows) * (1000000 - 1)
        galaxy[1] += sum(col < galaxy[1] for col in empty_cols) * (1000000 - 1)

    # Calculate the sum of distances
    total_distance = sum(abs(gal1[0] - gal2[0]) + abs(gal1[1] - gal2[1]) 
                         for k, gal1 in enumerate(galaxies) 
                         for gal2 in galaxies[k + 1:])

    return total_distance

# Replace every galaxy with a number, starting at 1
def count_galaxies(grid):
    points = []
    num = 1
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == '#':
                grid[i][j] = str(num)
                points.append((num, (i, j)))
                num += 1
    # for row in grid:
    #     print (''.join(row))
    return grid, points

# Calculate the shortest distance from each galaxy to all of the other '#'
def calculate_distance(points):
    distances = {}
    for i in range(len(points)):
        for j in range(i+1, len(points)):
            # Calculate the Manhattan distance between point i and point j
            distance = sum(abs(a-b) for a, b in zip(points[i][1], points[j][1]))
            
            # Store the distance in the dictionary
            distances[(points[i][0], points[j][0])] = distance
            
    return distances

# input_string = """...#......
# .......#..
# #.........
# ..........
# ......#...
# .#........
# .........#
# ..........
# .......#..
# #...#.....
# """

# grid = expand_universe_p2(input_string.splitlines())
# grid, points = count_galaxies(grid)
# combinations = len(list(combinations(points, 2)))
# distances = calculate_distance(points)
# print(sum(distances.values()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

grid = expand_universe(input.splitlines())
grid, points = count_galaxies(grid)
combinations = len(list(combinations(points, 2)))
distances = calculate_distance(points)
p1 = sum(distances.values())

print("Part One : "+ str(int(p1)))

total_distance = expand_universe_p2(input.splitlines())
# grid, points = count_galaxies(grid)
# combinations = len(list(combinations(points, 2)))
# distances = calculate_distance(points)
# p2 = sum(distances.values())

print("Part Two : "+ str(int(total_distance)))