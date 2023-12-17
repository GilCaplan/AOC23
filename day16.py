from collections import deque
import numpy as np
file = [line.strip() for line in open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input16.txt", "r").readlines()]
lamR = lambda x, y: lambda r, dirR, c, dirC: [(r+dirR, c, x * dirR, y * dirR)]
directionsR = {'.': lamR(1, 0), '|': lamR(1, 0), '/': lamR(0, -1), '\\': lamR(0, 1),
               '-': lambda r, dirR, c, dirC: [(r + dirR, c, 0, -1), (r + dirR, c, 0, 1)]}
lamC = lambda x, y: lambda r, dirR, c, dirC: [(r, c+dirC, x * dirC, y * dirC)]
directionsC = {'.': lamC(0, 1), '-': lamC(0, 1), '/': lamC(-1, 0), '\\': lamC(1, 0),
               '|': lambda r, dirR, c, dirC: [(r, c + dirC, 1, 0), (r, c + dirC, -1, 0)]}


def beam(r, c, dirR, dirC):
    queue, visited = deque([(r, c, dirR, dirC)]), set()
    while queue:
        r, c, dirR, dirC = queue.popleft()
        if (r, c, dirR, dirC) in visited:
            continue
        visited.add((r, c, dirR, dirC))
        charged[r][c] = 1
        if not -1 < r + dirR < len(grid) or not -1 < c + dirC < len(grid[0]):
            continue
        dirs, key = (directionsR, grid[r + dirR][c]) if dirR != 0 else (directionsC, grid[r][c + dirC])
        queue.extend((row, col, dr, dc) for row, col, dr, dc in dirs.get(key, [])(r, dirR, c, dirC))


scores = []
for i in range(len(file)):
    for d, y in [(1, 0), (-1, len(file)-1)]:
        grid = [list(line.strip()) for line in file]
        charged = np.zeros_like(grid, dtype=int)
        beam(i, y, *{'\\': (d, 0), '/': (0, -d)}.get(grid[i][y], (0, d)))
        scores.append(np.sum(charged))
print('part 1 solution:', scores[0], '\npart 2 solution:', max(scores))
