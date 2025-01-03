# Advent of code Year 2024 Day 5 solution
# Author = jdanml
# Date = December 2024

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read().splitlines()

before_list = []
after_list = []
for line in input:
    if '|' in line:
        before, after = map(int, line.strip().split('|'))
        before_list.append(before)
        after_list.append(after)

with open((__file__.rstrip("code.py")+"input2.txt"), 'r') as input_file:
    input2 = input_file.read().splitlines()

def check_order(page_list, before_list, after_list):
    for before, after in zip(before_list, after_list):
        try:
            before_index = page_list.index(before)
            after_index = page_list.index(after)
            if before_index > after_index:
                return False
        except ValueError:
            # If either before or after is not in the page_list, continue checking other pairs
            continue
    return True

def reorder(page_list, before_list, after_list):
    for before, after in zip(before_list, after_list):
        try:
            before_index = page_list.index(before)
            after_index = page_list.index(after)
            if before_index > after_index:
                page_list[before_index], page_list[after_index] = page_list[after_index], page_list[before_index]
        except ValueError:
            # If either before or after is not in the page_list, continue checking other pairs
            continue
    return page_list

count_middle = 0
count_middle_p2 = 0
for line in input2:
    if line.strip():  # Check if the line is not empty
        page_list = list(map(int, line.strip().split(',')))
        print(f"Page list: {page_list}")
        if check_order(page_list, before_list, after_list):
            print(f"Page is sorted: {page_list}")
        
            # Get the middle element
            middle_index = len(page_list) // 2
            middle_element = page_list[middle_index]
            print(f"Middle element: {middle_element}")
            count_middle += middle_element
        
        else:
            print(f"Page is not sorted: {page_list}")
            page_list = reorder(page_list, before_list, after_list)
            while not check_order(page_list, before_list, after_list):
                page_list = reorder(page_list, before_list, after_list)
            print(f"Reordered page list: {page_list}")
        
            # Get the middle element
            middle_index = len(page_list) // 2
            middle_element = page_list[middle_index]
            print(f"Middle element: {middle_element}")
            count_middle_p2 += middle_element

print("Part One : "+ str(count_middle))


print("Part Two : "+ str(count_middle_p2))