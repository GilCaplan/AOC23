from shapely import Polygon
puzzle = [line.strip().split() for line in open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input18.txt", 'r').readlines()]
dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
lagoon, lagoon2, end, end2 = [], [], (0, 0), (0, 0)
for angle, length, color in puzzle:
    lagoon.append(end := (end[0] + int(length) * dirs[angle][0], end[1] + int(length) * dirs[angle][1]))
    x, y = list(dirs.values())[int(color[7])]
    side = int(color[2:7], 16)
    lagoon2.append(end2 := (end2[0] + side * x, end2[1] + side * y))
print([('part'+str(i+1), (lambda p: int(p.area+p.length//2+1))(Polygon(d))) for i, d in enumerate([lagoon, lagoon2])])
