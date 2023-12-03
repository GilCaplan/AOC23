import re


def process_input(input_data, part1):
    rows, cols = len(input_data), len(input_data[0])
    total_sum = 0

    for i in range(rows):
        for j in range(cols):
            if part1 and not re.match("[0-9.]", input_data[i][j]):
                total_sum += calculate_pieces(input_data, i, j, True)
            elif not part1 and re.match("\\*", input_data[i][j]):
                total_sum += calculate_pieces(input_data, i, j, False)

    return total_sum


def calculate_pieces(input_data, row, col, part1):
    total_sum = 0 if part1 else 1
    count = 0
    dx, dy = [1, -1, 0, 0, 1, -1, 1, -1], [0, 0, 1, -1, 1, -1, -1, 1]

    for x, y in zip(dx, dy):
        new_row, new_col = row + x, col + y

        adjacent_char = input_data[new_row][new_col]
        original_col = new_col

        if adjacent_char.isdigit():
            num = [adjacent_char]
            input_data[new_row][new_col] = '.'

            while new_col + 1 < len(input_data) and input_data[new_row][new_col + 1].isdigit():
                num.append(input_data[new_row][new_col + 1])
                input_data[new_row][new_col + 1] = '.'
                new_col += 1

            new_col = original_col

            while new_col - 1 >= 0 and input_data[new_row][new_col - 1].isdigit():
                num.insert(0, input_data[new_row][new_col - 1])
                input_data[new_row][new_col - 1] = '.'
                new_col -= 1

            if part1:
                total_sum += int(''.join(num))
            else:
                total_sum *= int(''.join(num))
                count += 1

    if not part1 and count == 1:
        return 0

    return total_sum


def get_input():
    with open("input3.txt", "r") as file:
        return [list(line.strip()) for line in file]


print(process_input(get_input(), True))
print(process_input(get_input(), False))
