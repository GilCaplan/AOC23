from functools import reduce

def part1(in2):
    return sum(int(game) for game, line in in2.items() if check(line))


def check(line):
    for elem in line:
        lne = elem.split()
        for col, color in zip(['red', 'green', 'blue'], [12, 13, 14]):
            if lne[1] == col and int(lne[0]) > color:
                return False
    return True


def part2(in2):
    return sum(power(num) for num in in2.values())


def power(line):
    return reduce(lambda x, color: x * max(int(item.split()[0]) for item in line if item.split()[1] == color),
                  ['red', 'green', 'blue'], 1)


def input2():
    with open(r"C:\Users\USER\PycharmProjects\AOC2023\input2.txt", 'r') as file:
        input_data = [line.strip() for line in file]

    in1 = {game.split(r':')[0].split()[1]: game.split(r':')[1].replace(';', ',').split(',') for game in input_data}
    return in1


print(part1(input2()))
print(part2(input2()))
