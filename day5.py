def convert_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    seeds, *map_lines = lines
    maps = {}
    for map_data in [line.split(':') for line in map_lines]:
        if len(map_data[0]) > 2 and map_data[0][0].isdigit():
            maps[key].append(tuple(map(int, map_data[0].split())))
        elif len(map_data[0].split()) > 0 and not map_data[0].split()[0].isdigit():
            key, maps[key] = map_data[0].strip(), []

    return list(map(int, seeds.split()[1:])), maps


def find_lowest_location(seeds, maps):
    lowest_location = float('inf')
    conversion_order = [key for key in maps.keys() if key.endswith('map')]

    for seed in seeds:
        location = seed
        for category in conversion_order:
            location = convert_category(location, maps[category])
        lowest_location = min(lowest_location, location)
    return lowest_location


def convert_category(seed, maps):
    swap = seed
    for map_line in maps:
        dest_start, source_start, length = map(int, map_line)
        if source_start <= swap < source_start + length:
            return dest_start + (seed - source_start)
    return seed


seeds, maps = convert_data("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input5.txt")
print("part1: Lowest Location Number:", find_lowest_location(seeds, maps))
