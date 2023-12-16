from collections import deque
import numpy as np
file = open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input16.txt", "r").readlines()
grid = [list(line.strip()) for line in file]


def beam(r, c, dirR, dirC):
    queue = deque([(r, c, dirR, dirC)])
    visited = set()

    while queue:
        r, c, dirR, dirC = queue.popleft()
        if (r, c, dirR, dirC) in visited:
            continue
        visited.add((r, c, dirR, dirC))
        charged[r][c] = 1  # Marking the cell

        if dirR != 0 and -1 < r + dirR < len(grid):
            directions = {
                '.': [(r+dirR, c, dirR, 0)],
                '|': [(r+dirR, c, dirR, 0)],
                '/': [(r+dirR, c, 0, -dirR)],
                '\\': [(r+dirR, c, 0, dirR)],
                '-': [(r + dirR, c, 0, -1), (r + dirR, c, 0, 1)]
            }
            # traveling up or down
            if grid[r + dirR][c] in directions:
                for row, col, dr, dc in directions[grid[r+dirR][c]]:
                    queue.append((row, col, dr, dc))

        elif -1 < c + dirC < len(grid[0]):
            # traveling right or left
            directions = {
                '.': [(r, c + dirC, 0, dirC)],
                '-': [(r, c + dirC, 0, dirC)],
                '/': [(r, c + dirC, -dirC, 0)],
                '\\': [(r, c + dirC, dirC, 0)],
                '|': [(r, c + dirC, 1, 0), (r, c + dirC, -1, 0)]
            }
            if grid[r][c + dirC] in directions:
                for row, col, dr, dc in directions[grid[r][c + dirC]]:
                    queue.append((row, col, dr, dc))



scores = []
for i in range(len(grid)):
    for d in [1, -1]:
        grid = [list(line.strip()) for line in file]
        charged = np.array([list(0 for _ in line) for line in grid])
        dirX, dirY = d, 0
        if grid[i][0] == '\\':
            dirY, dirX = d, 0
        elif grid[i][0] == '/':
            dirY, dirX = -d, 0
        elif grid[i][0] == '-':
            beam(i, 0, 0, -1)
            dirY, dirX = d, 0
        beam(i, 0 if d == 1 else len(grid)-1, dirY, dirX)

        scores.append(np.sum(charged))


print('part 1 solution:', scores[0])
print('part 2 solution:', max(scores))

