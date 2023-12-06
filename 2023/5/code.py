# Advent of code Year 2023 Day 5 solution
# Author = jdanml
# Date = December 2023

def process_input(part, input_string):
    lines = input_string.splitlines()
    categories = {}
    current_category = None

    for line in lines:
        if "seeds:" in line and part == 1:
            _, seeds_str = line.split(":")
            seeds =  map(int, seeds_str.split())
        elif "seeds:" in line and part == 2:
            _, seeds_str = line.split(":")
            seeds_pairs = list(map(int, seeds_str.split()))
            seeds = (i for start, range_ in zip(seeds_pairs[::2], seeds_pairs[1::2]) for i in range(start, start + range_))
        elif "map:" in line:
            current_category = line.split(':')[0].strip().rstrip(" map")
            categories[current_category] = []
        elif line.strip() and all(word.isdigit() for word in line.split()):
            destination, source, range_ = map(int, line.split())
            categories[current_category].append((source, source + range_, destination))

    return seeds, categories

def find_location(seed, categories):
    results = {'seed': seed}
    for category in ['seed-to-soil', 'soil-to-fertilizer', 'fertilizer-to-water', 'water-to-light', 'light-to-temperature', 'temperature-to-humidity', 'humidity-to-location']:
        for start, end, destination in categories[category]:
            if start <= seed < end:
                seed = destination + (seed - start)
                break
        results[category.split('-to-')[1]] = seed
    return 'Seed {seed}, soil {soil}, fertilizer {fertilizer}, water {water}, light {light}, temperature {temperature}, humidity {humidity}, location {location}.'.format(**results)

input_string = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
"""
# seeds, categories = process_input(input_string)
# print (categories)
# for seed in seeds:
#     location = find_location(seed, categories)
#     print(location)

with open((__file__.rstrip("code.py")+"input.txt"), 'r') as input_file:
    input = input_file.read()

    min_location = float('inf')
    min_location_seed = None
    seeds, categories = process_input(1, input)
    for seed in seeds:
        location = find_location(seed, categories)
        location_number = int(location.split('location ')[1].split('.')[0])
        if location_number < min_location:
            min_location = location_number
            min_location_seed = seed
        print(location)

    print("Part One : "+ str(min_location))

    min_location = float('inf')
    min_location_seed = None
    seeds, categories = process_input(2, input)
    for seed in seeds:
        location = find_location(seed, categories)
        location_number = int(location.split('location ')[1].split('.')[0])
        if location_number < min_location:
            min_location = location_number
            min_location_seed = seed
            print(min_location)

    print("Part Two : "+ str(min_location))