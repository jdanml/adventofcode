# Advent of code Year 2024 Day 2 solution
# Author = jdanml
# Date = December 2024

def asc_desc(line):
    # Extract numbers from the line
    numbers = [int(num) for num in line.split()]

    if len(numbers) == len(set(numbers)):
        # Check if the list is sorted in ascending or descending order
        if (numbers == sorted(numbers) or numbers == sorted(numbers, reverse=True)):
            return 0  # All numbers are sorted
        else:
            return 2
    # Check for duplicates
    elif (len(numbers) - len(set(numbers))) == 1:
        return 1
    else:
        return 3

def calculate_difference(line):
    differences = []
    
    # Check if line is a string and convert it to a list of numbers
    if isinstance(line, str):
        numbers = [int(num) for num in line.split() if num.isdigit()]
    else:
        numbers = line

    # Calculate the differences
    for i in range(len(numbers) - 1):
        differences.append(abs(numbers[i] - numbers[i + 1]))
    
    return differences

def corrected_report(line):
    # Extract numbers from the line
    numbers = [int(num) for num in line.split()]

    modified_report = []
    count_not_sorted_asc, count_not_sorted_desc = 0, 0

    sorted_numbers_asc = sorted(numbers)
    count_not_sorted_asc = sum(1 for i in range(len(numbers)) if numbers[i] != sorted_numbers_asc[i])
    sorted_numbers_desc = sorted(numbers, reverse=True)
    count_not_sorted_desc = sum(1 for i in range(len(numbers)) if numbers[i] != sorted_numbers_desc[i])

    if (count_not_sorted_asc < count_not_sorted_desc) and count_not_sorted_asc == 1:
        for i in range(len(numbers) - 1):
            if (numbers[i] > numbers[i + 1]):
                modified_report = numbers[:i] + numbers[i + 1:]
                break
        return modified_report
    elif (count_not_sorted_asc > count_not_sorted_desc) and count_not_sorted_desc == 1:
        for i in range(len(numbers) - 1):
            if (numbers[i] < numbers[i + 1]):
                modified_report = numbers[:i] + numbers[i + 1:]
                break
        return modified_report
    else:
        pass

def remove_duplicate(line):
    numbers = [int(num) for num in line.split()]
    seen = set()
    for i, num in enumerate(numbers):
        if num in seen:
            return numbers[:i] + numbers[i+1:]
        seen.add(num)
    return numbers

safe_reports = 0
safe_reports_p2 = 0

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()
    for line in input.splitlines():
        # Part One
        if asc_desc(line) == 0:
            level_diffs = calculate_difference(line)
            if any(num >= 4 for num in level_diffs) or any(num == 0 for num in level_diffs):
                pass
            else:
                safe_reports += 1
        # Part Two
        elif asc_desc(line) == 1:
            corrected = remove_duplicate(line)
            level_diffs = calculate_difference(corrected)
            if any(num >= 4 for num in level_diffs) or any(num == 0 for num in level_diffs):
                pass
            else:
                safe_reports_p2 += 1
        elif asc_desc(line) == 2: 
            corrected = corrected_report(line)
            if corrected is not None:
                level_diffs = calculate_difference(corrected)
                if any(num >= 4 for num in level_diffs) or any(num == 0 for num in level_diffs):
                    pass
                else:
                    safe_reports_p2 += 1
        else:
            pass
        
print("Part One : "+ str(safe_reports))

print("Part Two : "+ str(safe_reports + safe_reports_p2))