from shapely import Polygon
puzzle = [line.strip().split() for line in open("input18.txt", 'r').readlines()]
dirs, lagoon, lagoon2, end, end2 = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}, [], [], (0, 0), (0, 0)
for angle, length, color in puzzle:
    lagoon.append(end := (end[0] + int(length) * dirs[angle][0], end[1] + int(length) * dirs[angle][1]))
    x, y = list(dirs.values())[int(color[7])]
    lagoon2.append(end2 := (end2[0] + int(color[2:7], 16) * x, end2[1] + int(color[2:7], 16) * y))
print([('part'+str(i+1), (lambda p: int(p.area+p.length//2+1))(Polygon(d))) for i, d in enumerate([lagoon, lagoon2])])
