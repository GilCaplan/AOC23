import numpy as np
import itertools


def expand(grid):
    return tuple(map(lambda axis: [i for i in range(grid.shape[axis]) if
                                    all(c == '.' for c in (grid[i] if axis == 0 else grid[:, i]))], [0, 1]))


def find_points(grid):
    return [(i, j) for i in range(grid.shape[0]) for j in range(grid.shape[1]) if grid[i][j] == '#']


def calc_man_dist(x, y, expand, num):
    return abs(x - y) + sum(num - 1 for c in expand if min(x, y) <= c <= max(x, y))


def cal_min_dis(points, expand_rows, expand_cols, num):
    return int(sum((calc_man_dist(r2, r1, expand_rows, num) + calc_man_dist(c2, c1, expand_cols, num))
                   for (r1, c1), (r2, c2) in itertools.combinations(points, 2)))


with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input11.txt", "r") as file:
    grid = np.array([list(line.strip()) for line in file])
rows, cols = expand(grid)

print('part 1 solution: ', cal_min_dis(find_points(grid), rows, cols, 2), 
      '\npart 2 solution:', cal_min_dis(find_points(grid), rows, cols, 1000000))
