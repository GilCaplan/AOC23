from collections import deque
from copy import deepcopy as dp
from functools import lru_cache

def convert_maze(maze):
    conversion_dict = {'#': 1, '.': 0, '>': 2, '<': 3, '^': 4, 'v': 5}
    return [[conversion_dict[cell] for cell in row] for row in maze]
def convert_maze_2(maze):
    return [[0 if cell != 1 else 1 for cell in row] for row in maze]

maze = convert_maze(tuple(line.strip() for line in open("input22.txt", "r").readlines()))


def bfs_longest_path(maze, start=(0, 0), part1=True):
    dirs = {2: (0, 1), 3: (0, -1), 4: (-1, 0), 5: (1, 0)}
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    paths = []

    def is_valid(x=0, y=0):
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != 1

    queue = deque([(start[0], start[1], {(0, 0)})])

    while queue:
        x, y, path = queue.popleft()
        if x == len(maze) - 1 and maze[len(maze) - 1][y] == 0:
            paths.append(len(path))
            continue
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if 1 < maze[x][y] < 6 and (dx, dy) != dirs[maze[x][y]]:
                continue
            if is_valid(new_x, new_y) and (new_x, new_y) not in path:
                path.add((new_x, new_y))
                queue.append((new_x, new_y, dp(path)))
                path.remove((new_x, new_y))
    return max(paths)


for part1 in [False]:
    if not part1:
        maze = convert_maze_2(maze)
    print(bfs_longest_path(maze, (0, 0), part1) - 2)
    # 2414


# turn to graph with nodes, then convert to a weighted map and run dfs
