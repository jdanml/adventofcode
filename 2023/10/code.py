# Advent of code Year 2023 Day 10 solution
# Author = jdanml
# Date = December 2023

def solve(grid):
    directions = {'|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)], 'L': [(0, 1), (-1, 0)], 'J': [(0, -1), (-1, 0)], '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], 'S': [(0, 1), (1, 0), (0, -1), (-1, 0)]}
    max_distance = 0
    visited = set()
    stack = []

    # Find the starting position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                for direction in directions[grid[i][j]]:
                    stack.append((i, j, 0, direction))  # position, distance, and direction
                break

    while stack:
        x, y, distance, (dx, dy) = stack.pop()
        max_distance = max(max_distance, distance)
        visited.add((x, y))

        for ndx, ndy in directions[grid[x][y]]:
            nx, ny = x + ndx, y + ndy
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] != '.') and ((nx, ny) not in visited) and (ndx, ndy) != (-dx, -dy):
                stack.append((nx, ny, distance + 1, (ndx, ndy)))

    return max_distance

input_string = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...
"""

print(solve(input_string.splitlines()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    max_distance = (int(solve(input.splitlines())) + 1) / 2

print("Part One : "+ str(int(max_distance)))



print("Part Two : "+ str(None))