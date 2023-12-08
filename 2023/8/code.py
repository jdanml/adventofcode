# Advent of code Year 2023 Day 8 solution
# Author = jdanml
# Date = December 2023

# Imports
import math

def process_input(input):
    directions = None
    coordinates_dict = {}
    for index, line in enumerate(input.splitlines()):
        line = line.strip()
        if index == 0:
            directions = ''.join(line.split())
        elif "=" in line:
            coordinates, destinations = line.split("=")
            coordinates = coordinates.strip()
            destinations = destinations.strip()[1:-1].split(", ")
            coordinates_dict[coordinates] = destinations
        else:
            continue
    return directions, coordinates_dict

input_string = """LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)
"""

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    directions, coordinates_dict = process_input(input)

    coordinate = "AAA"
    steps = 0
    direction_index = 0
    while coordinate != "ZZZ":
        direction = directions[direction_index % len(directions)]
        destinations = coordinates_dict[coordinate]
        if direction == "L":
            coordinate = destinations[0]
        else:
            coordinate = destinations[1]
        steps += 1
        direction_index += 1

print("Part One : "+ str(steps))

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    directions, coordinates_dict = process_input(input)

    coordinates = [key for key in coordinates_dict.keys() if key.endswith("A")]
    print(f"Starting at {coordinates}")
    steps_p2 = 0

    def steps(coordinate):
        steps = 0
        direction_index = 0
        while not coordinate.endswith("Z"):
            direction = directions[direction_index % len(directions)]
            destinations = coordinates_dict[coordinate]
            if direction == "L":
                coordinate = destinations[0]
            else:
                coordinate = destinations[1]
            steps += 1
            direction_index += 1
        print(f"Reached {coordinate} in {steps} steps")
        return direction_index
    
    ret = 1
    for coordinate in coordinates:
        ret = math.lcm(ret, steps(coordinate))

print("Part Two : "+ str(ret))