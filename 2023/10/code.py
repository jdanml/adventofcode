# Advent of code Year 2023 Day 10 solution
# Author = jdanml
# Date = December 2023

def solve(grid):
    directions = {'|': [(1, 0), (-1, 0)], '-': [(0, 1), (0, -1)], 'L': [(0, 1), (-1, 0)], 'J': [(0, -1), (-1, 0)], '7': [(1, 0), (0, -1)], 'F': [(1, 0), (0, 1)], 'S': [(0, 1), (1, 0), (0, -1), (-1, 0)]}
    max_distance = 0
    visited = set()
    stack = []
    max_path = []
    cell_inside = 0

    # Find the starting position
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 'S':
                for direction in directions[grid[i][j]]:
                    stack.append((i, j, 0, direction, [(i, j)]))  # position, distance, direction, and path
                break

    while stack:
        x, y, distance, (dx, dy), path = stack.pop()
        if distance > max_distance:
            max_distance = distance
            max_path = path
        visited.add((x, y))

        for ndx, ndy in directions[grid[x][y]]:
            nx, ny = x + ndx, y + ndy
            if (0 <= nx < len(grid)) and (0 <= ny < len(grid[0])) and (grid[nx][ny] != '.') and ((nx, ny) not in visited) and (ndx, ndy) != (-dx, -dy):
                stack.append((nx, ny, distance + 1, (ndx, ndy), path + [(nx, ny)]))

    # Create a copy of the grid and mark the visited cells
    loop_grid = [list(row) for row in grid]
    for x, y in visited:
        loop_grid[x][y] = '#'

    # Mark the cells inside the loop with 'I'
    for i in range(len(loop_grid)):
        for j in range(len(loop_grid[i])):
            if (i, j) not in max_path and is_inside_polygon((i, j), max_path):
                loop_grid[i][j] = 'I'
                cell_inside += 1

    # Print the loop grid
    for row in loop_grid:
        print(''.join(row))

    return max_distance, cell_inside

def is_inside_polygon(point, polygon):
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside

input_string = """...........
.S-------7.
.|F-----7|.
.||.....||.
.||.....||.
.|L-7.F-J|.
.|..|.|..|.
.L--J.L--J.
...........
"""

print(solve(input_string.splitlines()))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    max_distance, cell_inside = solve(input.splitlines())
    p1 = int((max_distance + 1) / 2)

print("Part One : "+ str(p1))



print("Part Two : "+ str(cell_inside))