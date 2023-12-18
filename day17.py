import heapq
with open("input17.txt", "r") as file:
    puzzle_input = [line.strip() for line in file]


def dijkstra_shortest_path(begin, fin, c):
    queue = [(0, 1, 0, (0, 0))]
    shortest_path = {}

    while queue:
        cost, consec_steps, direction, current = heapq.heappop(queue)
        if consec_steps >= begin and current == end:
            return cost
        key = (current, direction, consec_steps)
        if key in shortest_path and shortest_path[key] <= cost:
            continue
        shortest_path[key] = cost
        neighbours = (lambda x, y: ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)))(*current)
        for index, new_direction in enumerate([(direction - 1) % 4, direction, (direction + 1) % 4]):
            conditions = [consec_steps < fin, consec_steps == c]
            if conditions[index % 2]:
                continue
            if index % 2 == 0:
                next_consec_steps = 1
            else:
                next_consec_steps = consec_steps + 1
            neighbour = neighbours[new_direction]

            if neighbour in grid and shortest_path.get((neighbour, new_direction, next_consec_steps), cost + 1) > cost:
                heapq.heappush(queue, (cost + grid[neighbour], next_consec_steps, new_direction, neighbour))
    return None


grid = {(x, y): int(puzzle_input[y][x]) for x in range(len(puzzle_input[0])) for y in range(len(puzzle_input))}
end = (len(puzzle_input[0]) - 1, len(puzzle_input) - 1)
print('part 1 solution:', dijkstra_shortest_path(0, 0, 3))
print('part 2 solution:', dijkstra_shortest_path(4, 4, 10))
