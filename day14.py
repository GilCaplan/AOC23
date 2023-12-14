import numpy as np

with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input14.txt", "r") as file:
    lines = [list(line.strip()) for line in file]

puzzle1 = np.array(lines)
puzzle2 = np.array(lines)


def convert(arr):
    if len(arr[0]) == 1:
        arr = np.array([list(row[0]) for row in arr])
    return arr


def tilt_left(arr):
    sorted_rocks = []
    for col in arr:
        sub_lists = ''.join(col).split('#')

        sorted_sub_lists = []
        for sub in sub_lists:
            o_count = sum(1 for s in sub if s == 'O')
            sorted_sublist = ['O'] * o_count + ['.'] * (len(sub) - o_count)
            sorted_sub_lists.append(''.join(sorted_sublist))

        sorted_rocks.append(['#'.join(sorted_sub_lists)])
    return sorted_rocks


def solve(array):
    return weight(tilt_left(array.T))


def weight(array):
    if len(array[0]) != 1:
        array = [[''.join(row)] for row in array]
    return sum((len(array) - i) * row[0].count('O') for i, row in enumerate(array))


def cycle(array):
    array = convert(tilt_left(np.rot90(array))) # north
    array = convert(tilt_left(np.rot90(array, k=-1))) # west
    array = convert(tilt_left(np.rot90(array, k=3)))
    array = convert(tilt_left(np.rot90(array, k=3)))
    return np.rot90(array, k=2)


def part2(array):
    boards = {}
    loads = [0]
    l, start = 0, 0
    # find cycle length
    for t in range(1, 1000):
        array = cycle(array)

        loads.append(weight(array))
        h = hash(array.tobytes())
        if h in boards.keys():
            l, start = t - boards[h], boards[h]
            break
        boards[h] = t

    times = start + (1000000000 - start) % l

    return loads[times]


print(solve(puzzle1))
print(part2(puzzle2))
