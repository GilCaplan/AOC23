def split_and_store_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    seed_line = next((line for line in lines if line.startswith('seeds:')), None)
    if seed_line:
        seed_list = list(map(int, seed_line.split(':')[1].strip().split()))
    else:
        seed_list = []

    map_lines = [line.strip() for line in lines if not line.startswith('seeds:')]
    data = [line.split(':') for line in map_lines]
    maps = {}
    key = ""
    for map_data in data[1:]:
        if len(map_data[0]) > 2 and map_data[0].split()[0].isdigit():
            maps[key].append(tuple(map(int, map_data[0].split())))
        elif len(map_data[0].split()) > 0 and not map_data[0].split()[0].isdigit():
            maps[map_data[0].strip()] = []
            key = map_data[0].strip()

    return seed_list, maps


def convert_category(seed, maps):
    swap = seed
    for map_line in maps:
        dest_start, source_start, length = map(int, map_line)
        if source_start <= swap < source_start + length:
            return dest_start + (seed - source_start)
    return seed


def find_lowest_location(seeds, maps):
    lowest_location = float('inf')

    conversion_order = [
        'seed-to-soil map',
        'soil-to-fertilizer map',
        'fertilizer-to-water map',
        'water-to-light map',
        'light-to-temperature map',
        'temperature-to-humidity map',
        'humidity-to-location map'
    ]

    for seed in seeds:
        location = seed
        for category in conversion_order:
            location = convert_category(location, maps[category])
        lowest_location = min(lowest_location, location)
    return lowest_location


seeds, maps = split_and_store_from_file("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input5.txt")

print("part1: Lowest Location Number:", find_lowest_location(seeds, maps))
