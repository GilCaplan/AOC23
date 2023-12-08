from math import lcm


def part1(nodes, instructions, start, num):
    cnt = num
    way = start
    for inst in instructions:
        way = nodes[way][0] if inst == 'L' else nodes[way][1]
        cnt += 1
        if way == 'ZZZ':
            return cnt
    return part1(nodes, instructions, way, cnt)


def part2(map, directions, start_nodes):
    i = 0
    cycles = []
    while True:
        for n, label in enumerate(start_nodes):
            node = map[label]
            way = node[0] if directions[i % len(directions)] == "L" else node[1]
            if way.endswith("Z"):
                cycles.append(i + 1)
            start_nodes[n] = way
        if len(cycles) == len(start_nodes):
            break
        i += 1
    return lcm(*cycles)


with open('input8.txt', 'r') as file:
    lines = file.readlines()

instructions = lines[0].strip()
nodes = [node.split('=') for node in lines[2:]]
node_data = {}

for node in nodes:
    key = node[0].strip()
    value = node[1].replace('(', '').replace(')', '').replace('\n', '').split(', ')
    node_data[key] = (value[0].strip(), value[1].strip())

start = [key for key in node_data.keys() if key.endswith('A')]
print('part 1 solution:', part1(node_data, instructions, 'AAA', 0))
print('part 2 solution:', part2(node_data, instructions, start))
