def part1(in2):
    # max 12 red, 13 green, 14 blue
    # {Game id : list with color and amount}
    return sum(int(game) for game, line in in2.items() if check(line))


def check(line):
    # line is "[color number]
    for elem in line:
        l = elem.split()
        if l[1] == 'red' and int(l[0]) > 12:
            return False
        elif l[1] == 'green' and int(l[0]) > 13:
            return False
        elif l[1] == 'blue' and int(l[0]) > 14:
            return False
    return True


def part2(in2):
    return sum(power(num) for num in in2.values())


def power(line):
    red = max(int(item.split()[0]) for item in line if item.split()[1] == 'red')
    green = max(int(item.split()[0]) for item in line if item.split()[1] == 'green')
    blue = max(int(item.split()[0]) for item in line if item.split()[1] == 'blue')
    return red * green * blue


def input2():
    file_path = r"input2.txt"

    input_data = []

    with open(file_path, 'r') as file:
        for line in file:
            input_data.append(line.strip())

    in1 = {game.split(r':')[0].split()[1]: game.split(r':')[1].replace(';', ',').split(',') for game in input_data}
    # {Game id : list with color and amount}
    return in1


print(part1(input2()))
print(part2(input2()))
