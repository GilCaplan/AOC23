from functools import reduce

file_path = 'C:\\Users\\USER\\PycharmProjects\\AOC2023\\input5.txt'
file_content = open(file_path).read().split('\n\n')

seeds, *mappings = file_content
seeds = list(map(int, seeds.split()[1:]))


# Define a function to find the transformed values
def transform_input_range(inputs, mapping_rules):
    for start, length in inputs:
        while length > 0:
            for mapping in mapping_rules.split('\n')[1:]:
                destination, source, mapping_length = map(int, mapping.split())
                delta = start - source
                if delta in range(mapping_length):
                    transformed_length = min(mapping_length - delta, length)
                    yield destination + delta, transformed_length
                    start += transformed_length
                    length -= transformed_length
                    break
            else:
                # If no mapping is applied, yield the original range
                yield start, length
                break

# Process each seed range and find the minimum transformed value


result = 1 << 60

for seed_range in [zip(seeds[0::2], seeds[1::2])]:
    min_transformed_value = min(reduce(transform_input_range, mappings, seed_range))[0]
    result = min(result, min_transformed_value)

print(result)
