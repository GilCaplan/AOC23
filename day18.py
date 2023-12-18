from shapely import Polygon
puzzle = [line.strip().split() for line in open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input18.txt", 'r').readlines()]

dirs = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
dig_site, dig_site2, end, end2 = [], [], (0, 0), (0, 0)
for angle, length, color in puzzle:
    end = (end[0] + int(length) * dirs[angle][0], end[1] + int(length) * dirs[angle][1])
    dig_site.append(end)

    length = int(color[2:7], 16)
    x, y = list(dirs.values())[int(color[7])]
    end2 = (end2[0] + length * x, end2[1] + length * y)
    dig_site2.append(end2)

pol1, pol2 = Polygon(dig_site), Polygon(dig_site2)
print("Area 1:", int(pol1.area + pol1.length//2 + 1), '\nArea 2:', int(pol2.area + pol2.length//2 + 1))
