with open('C:\\Users\\USER\\PycharmProjects\\AOC2023\\input24.txt') as f:
    split = lambda x, n: tuple(map(int, x.split(' @ ')[n].split(', ')))
    puzzle = list((split(line.strip(), 0), split(line.strip(), 1)) for line in f)

from itertools import combinations

def equation(x1, y1, vx1, vy1, x2, y2, vx2, vy2):
    m1, m2 = vy1 / vx1, vy2 / vx2
    if m1 == m2:
        return 0
    x = (x1 * m1 - x2 * m2 + y2 - y1) / (m1 - m2)
    y = m2 * (x - x2) + y2
    if (x > x1) != (vx1 > 0) or (y > y1) != (vy1 > 0) or (x > x2) != (vx2 > 0) or (y > y2) != (vy2 > 0):
        return 0
    return 1 if (200000000000000 <= x <= 400000000000000) and (200000000000000 <= y <= 400000000000000) else 0


part1 = [(line[0][:2], line[1][:2]) for line in puzzle]
total = 0

for (point1, vector1), (point2, vector2) in combinations(part1, 2):
    (x1, y1), (vx1, vy1) = point1, vector1
    (x2, y2), (vx2, vy2) = point2, vector2
    total += equation(x1, y1, vx1, vy1, x2, y2, vx2, vy2)

print(total) # part 1
