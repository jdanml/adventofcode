# Advent of code Year 2024 Day 6 solution
# Author = jdanml
# Date = December 2024

def move_guard(grid):
    # Convert each string in the grid to a list of characters for mutability
    grid = [list(row) for row in grid]

    # Directions: up (^), right (>), down (v), left (<)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Start facing up (^)

    # Find the guard's initial position
    guard_positions = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '^']
    if not guard_positions:
        print("No guard ('^') found in the grid.")
        return 0
    y, x = guard_positions[0]

    # Set to keep track of walked cells
    walked = set()
    walked.add((y, x))  # Include the starting position

    while True:
        # Compute the cell in front of the guard based on current direction
        dy, dx = directions[direction_index]
        ny, nx = y + dy, x + dx

        # Check if the next position is out of bounds
        if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])):
            break  # Guard moves out of bounds

        # Check for obstacle
        if grid[ny][nx] == '#':
            # Turn right 90 degrees
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            walked.add((ny, nx))  # Mark the new position as walked
            y, x = ny, nx

    # Mark walked cells with 'X' on the grid
    for (i, j) in walked:
        # Preserve obstacles and the initial guard symbol
        if grid[i][j] not in ('#', '^'):
            grid[i][j] = 'X'

    # Convert the grid back to strings for display
    resulting_grid = [''.join(row) for row in grid]

    # Count the total number of 'X' in the resulting grid
    x_count = sum(row.count('X') for row in resulting_grid)

    # Print the resulting grid
    print("Resulting Grid with Walked Path Marked as 'X':")
    for row in resulting_grid:
        print(row)

    return x_count

def loop_guard(grid):
    # Convert each string in the grid to a list of characters for mutability
    grid = [list(row) for row in grid]

    # Directions: up (^), right (>), down (v), left (<)
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    direction_index = 0  # Start facing up (^)

    # Find the guard's initial position
    guard_positions = [(i, j) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == '^']
    if not guard_positions:
        print("No guard ('^') found in the grid.")
        return False
    y, x = guard_positions[0]

    # Set to keep track of walked cells and visited states
    walked = set()
    visited_states = set()
    walked.add((y, x))  # Include the starting position
    visited_states.add((y, x, direction_index))

    while True:
        # Compute the cell in front of the guard based on current direction
        dy, dx = directions[direction_index]
        ny, nx = y + dy, x + dx

        # Check if the next position is out of bounds
        if not (0 <= ny < len(grid) and 0 <= nx < len(grid[0])):
            break  # Guard moves out of bounds

        # Check for obstacle
        if grid[ny][nx] == '#':
            # Turn right 90 degrees
            direction_index = (direction_index + 1) % 4
        else:
            # Move forward
            y, x = ny, nx
            walked.add((ny, nx))  # Mark the new position as walked

        # Check if the current state (position and direction) has been visited before
        if (y, x, direction_index) in visited_states:
            return True
        visited_states.add((y, x, direction_index))

    return False

def check_loop_with_guard(grid):
    # Convert each string in the grid to a list of characters for mutability
    grid = [list(row) for row in grid]

    count_loop = 0

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            # Make a copy of the grid to modify
            new_grid = [row[:] for row in grid]
            # Add a '#' at the current position
            new_grid[i][j] = '#'
            # Check if this causes a loop
            if loop_guard(new_grid):
                count_loop += 1

    return count_loop

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

count_p1 = move_guard(input) + 1

print("Part One : "+ str(count_p1))

count_p2 = check_loop_with_guard(input)

print("Part Two : "+ str(count_p2))