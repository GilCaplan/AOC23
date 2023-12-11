import numpy as np


def expand(grid):
    rows, cols = grid.shape
    empty_rows = []
    empty_cols = []

    for i in range(rows):
        if all(c == '.' for c in grid[i]):
            empty_rows.append(i)

    for j in range(cols):
        if all(c == '.' for c in grid[:, j]):
            empty_cols.append(j)

    return empty_rows, empty_cols


def find_points(grid):
    rows, cols = grid.shape
    points = []
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == '#':
                points.append((i, j))
    return points


def cal_min_dis(points, expand_rows, expand_cols, num):
    total = 0
    for r1, c1 in points:
        for r2, c2 in points:
            c_sum = abs(c2 - c1) + sum(num-1 for c in expand_cols if min(c2, c1) <= c <= max(c2, c1))
            r_sum = abs(r2 - r1) + sum(num-1 for r in expand_rows if min(r2, r1) <= r <= max(r2, r1))
            total += c_sum + r_sum
    return int(total / 2)


with open("input11.txt", "r") as file:
    grid = np.array([list(line.strip()) for line in file])
rows, cols = expand(grid)

print(cal_min_dis(find_points(grid), rows, cols, 2))
print(cal_min_dis(find_points(grid), rows, cols, 1000000))




