def part1(in1):
    sum1 = 0
    for line in in1:
        first = get_digit(line)
        last = get_digit(line[::-1]) if first is not None else None
        if last is not None:
            sum1 += int(str(first) + str(last))
    return sum1


def get_digit(line):
    for char in line:
        if char.isdigit():
            return char
    return None


def convert_numb(line):
    numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    digits = [str(x) for x in range(1, 10)]
    order = []
    for n, d in zip(numbers, digits):
        index = line.find(n)
        while index != -1:
            order.append((index, n, d))
            index = line.find(n, index + 1)
    order = sorted(order, key=lambda x: x[0])
    new_line = ''
    for i in range(len(line)):
        if line[i].isdigit():
            new_line += line[i]
        else:
            for index, _, digit in order:
                if i == index:
                    new_line += digit
                    break
    return new_line


def part2(in2):
    for i in range(len(in2)):
        in2[i] = convert_numb(in2[i])
    return part1(in2)


def input1():
    file_path = "input"

    input_data = []

    with open(file_path, 'r') as file:
        for line in file:
            input_data.append(line.strip())

    return input_data


print(part1(input1()))
print(part2(input1()))
