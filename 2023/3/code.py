# Advent of code Year 2023 Day 3 solution
# Author = jdanml
# Date = December 2023


def find_numbers(input_string):
    lines = input_string.splitlines()
    grid = [list(line) for line in lines]
    numbers = []
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                start_j = j
                while j < len(grid[i]) and grid[i][j].isdigit():
                    j += 1
                number = int("".join(grid[i][start_j:j]))
                has_symbol = False
                for k in range(start_j, j):
                    for dx, dy in [
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1),
                        (-1, -1),
                        (-1, 1),
                        (1, -1),
                        (1, 1),
                    ]:
                        nx, ny = i + dx, k + dy
                        if (
                            0 <= nx < len(grid)
                            and 0 <= ny < len(grid[nx])
                            and not grid[nx][ny].isdigit()
                            and grid[nx][ny] != "."
                        ):
                            has_symbol = True
                            break
                    if has_symbol:
                        break
                if has_symbol:
                    numbers.append(number)
            else:
                j += 1
    return numbers


def find_multiple_numbers_adjacent_to_asterisk(input_string):
    lines = input_string.splitlines()
    grid = [list(line) for line in lines]
    asterisks = {}
    for i in range(len(grid)):
        j = 0
        while j < len(grid[i]):
            if grid[i][j].isdigit():
                start_j = j
                while j < len(grid[i]) and grid[i][j].isdigit():
                    j += 1
                number = int("".join(grid[i][start_j:j]))
                for k in range(start_j, j):
                    for dx, dy in [
                        (-1, 0),
                        (1, 0),
                        (0, -1),
                        (0, 1),
                        (-1, -1),
                        (-1, 1),
                        (1, -1),
                        (1, 1),
                    ]:
                        nx, ny = i + dx, k + dy
                        if (
                            0 <= nx < len(grid)
                            and 0 <= ny < len(grid[nx])
                            and grid[nx][ny] == "*"
                        ):
                            if (nx, ny) in asterisks:
                                if number not in asterisks[(nx, ny)]:
                                    asterisks[(nx, ny)].append(number)
                            else:
                                asterisks[(nx, ny)] = [number]
            else:
                j += 1
    pairs = [tuple(numbers) for numbers in asterisks.values() if len(numbers) > 1]
    return pairs


with open((__file__.rstrip("code.py") + "input.txt"), "r") as input_file:
    input = input_file.read()

    numbers = find_numbers(input)
    sum_p1 = sum(numbers)

    pairs = find_multiple_numbers_adjacent_to_asterisk(input)
    sum_p2 = sum(a * b for a, b in pairs)

print("Part One : " + str(sum_p1))


print("Part Two : " + str(sum_p2))
