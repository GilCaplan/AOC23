def part1(in1):
    sum1 = 0
    for line in in1:
        first = get_digit(line)
        last = get_digit(line[::-1])
        if last is not None:
            sum1 += int(first) * 10 + int(last)
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
    new_line = ''
    for i, char in enumerate(line):
        if char.isdigit():
            new_line += char
        else:
            for index, _, digit in order:
                if i == index:
                    new_line += digit
                    break
    return new_line


def part2(in2):
    return part1([convert_numb(elem) for elem in in2])


def input1():    
    with open(r"AOC2023\input1", 'r') as file:
        input_data = [line.strip() for line in file]

    return input_data


print(part1(input1()))
print(part2(input1()))
