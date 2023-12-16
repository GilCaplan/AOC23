from collections import deque
import numpy as np
file = [line.strip() for line in open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input16.txt", "r").readlines()]
directionsR = {
    '.': lambda r, dirR, c, dirC: [(r + dirR, c, dirR, 0)], '|': lambda r, dirR, c, dirC: [(r + dirR, c, dirR, 0)],
    '/': lambda r, dirR, c, dirC: [(r + dirR, c, 0, -dirR)], '\\': lambda r, dirR, c, dirC: [(r + dirR, c, 0, dirR)],
    '-': lambda r, dirR, c, dirC: [(r + dirR, c, 0, -1), (r + dirR, c, 0, 1)]
}
directionsC = {
    '.': lambda r, dirR, c, dirC: [(r, c + dirC, 0, dirC)], '-': lambda r, dirR, c, dirC: [(r, c + dirC, 0, dirC)],
    '/': lambda r, dirR, c, dirC: [(r, c + dirC, -dirC, 0)], '\\': lambda r, dirR, c, dirC: [(r, c + dirC, dirC, 0)],
    '|': lambda r, dirR, c, dirC: [(r, c + dirC, 1, 0), (r, c + dirC, -1, 0)]
}


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
        dirs, key = directionsR if dirR != 0 else directionsC, grid[r + dirR][c] if dirR != 0 else grid[r][c + dirC]
        queue.extend((row, col, dr, dc) for row, col, dr, dc in dirs.get(key, [])(r, dirR, c, dirC))


scores = []
for i in range(len(file)):
    for d, y in [(1, 0), (-1, len(file)-1)]:
        grid = [list(line.strip()) for line in file]
        charged = np.array([list(0 for _ in line) for line in grid])
        beam(i, y, *{'\\': (d, 0), '/': (0, -d)}.get(grid[i][y], (0, d)))
        scores.append(np.sum(charged))
print('part 1 solution:', scores[0], '\npart 2 solution:', max(scores))
