from collections import deque
import numpy as np
file = open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input16.txt", "r").readlines()


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
            # traveling up or down
            if grid[r + dirR][c] in ('.', '|'):
                queue.append((r + dirR, c, dirR, 0))
            elif grid[r + dirR][c] in ('/', '//'):
                queue.append((r + dirR, c, 0, -dirR))
            elif grid[r + dirR][c] in ('\\', '\\'):
                queue.append((r + dirR, c, 0, dirR))
            elif grid[r + dirR][c] == '-':
                queue.append((r + dirR, c, 0, 1))
                queue.append((r + dirR, c, 0, -1))
        elif -1 < c + dirC < len(grid[0]):
            # traveling right or left
            if grid[r][c + dirC] in ('.', '-'):
                queue.append((r, c + dirC, 0, dirC))
            elif grid[r][c + dirC] == '/':
                queue.append((r, c + dirC, -dirC, 0))
            elif grid[r][c + dirC] == '\\':
                queue.append((r, c + dirC, dirC, 0))
            elif grid[r][c + dirC] == '|':
                queue.append((r, c + dirC, -1, 0))
                queue.append((r, c + dirC, 1, 0))


grid = [list(line.strip()) for line in file]
charged = np.array([list(0 for _ in line) for line in grid])
beam(0, 0, 1, 0)

scores = []
print(np.sum(charged))

scores.append(np.sum(charged))

for i in range(len(grid)):
    grid = [list(line.strip()) for line in file]
    charged = np.array([list(0 for _ in line) for line in grid])
    dirX, dirY = 1, 0
    if grid[i][0] == '\\':
        dirY, dirX = 1, 0
    elif grid[i][0] == '/':
        dirY, dirX = -1, 0
    elif grid[i][0] == '-':
        beam(i, 0, 0, -1)
        dirY, dirX = 1, 0
    beam(i, 0, dirX, dirY)

    scores.append(np.sum(charged))

    grid = [list(line.strip()) for line in file]
    charged = np.array([list(0 for _ in line) for line in grid])
    dirX, dirY = 0, -1
    if grid[i][0] == '\\':
        dirY, dirX = -1, 0
    elif grid[i][0] == '/':
        dirY, dirX = 1, 0
    elif grid[i][0] == '-':
        beam(i, 0, 0, -1)
        dirY, dirX = 1, 0
    beam(i, len(grid)-1, dirX, dirY)

    scores.append(np.sum(charged))
    # assumption that the either the top row or bottom row has the starting point that gives the highest charged result (it did, could code for the sides too but didn't need for my input)
print(max(scores))
