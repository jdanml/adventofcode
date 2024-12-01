# Advent of code Year 2024 Day 1 solution
# Author = jdanml
# Date = December 2024

left_numbers = []
right_numbers = []
distance_sum = 0

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    for line in input.splitlines():
        # Split each line into two numbers
        left, right = line.split()
        # Append the numbers to the respective lists
        left_numbers.append(int(left))
        right_numbers.append(int(right))
        # Sort both lists
        left_numbers.sort()
        right_numbers.sort()

# Part One

for i in range(len(left_numbers)):
    # Calculate the distance between the two numbers
    distance = abs(left_numbers[i] - right_numbers[i])
    # Add the distance to the sum
    distance_sum += distance

# Print the lists (optional)
print("Left numbers:", left_numbers)
print("Right numbers:", right_numbers)


print("Part One : "+ str(distance_sum))

# Part Two

ocurrences_sum = 0
#Count the ocurrences of each number of the left list in the right list
for number in left_numbers:
    count = right_numbers.count(number)
    ocurrences_sum += count*number

print("Part Two : "+ str(ocurrences_sum))