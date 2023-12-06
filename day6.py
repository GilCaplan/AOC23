from math import prod


def solve_puzzle(num_races):
    return prod(
        sum(j * (Time[i] - j) > Distance[i] for j in range(1, Time[i] + 1))
        for i in range(num_races)
    )


Time = [44, 82, 69, 81]
Distance = [202, 1076, 1138, 1458]

print('part 1: ', (4))

Time = [44826981]
Distance = [202107611381458]

print'part 2: ', (solve_puzzle(1))
