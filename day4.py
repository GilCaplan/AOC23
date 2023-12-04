with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input4.txt", "r") as file:
    puzzle_input = [line.strip() for line in file]

games, total = [1 for _ in puzzle_input], 0
for i, line in enumerate(puzzle_input):
    left, right = line.split(':')[1].split('|')
    left_list, right_list = [list(map(int, x.strip().split())) for x in (left, right)]
    sum1 = sum(1 for elem in right_list if elem in left_list)
    total += (1 << sum1) >> 1 if sum1 > 0 else 0

    for j in range(sum(1 for elem in right_list if elem in left_list)):
        if i + j + 1 < len(puzzle_input):
            games[i + j + 1] += games[i]
print('part1 solution: ', total, '\npart2 solution: ', sum(games))
