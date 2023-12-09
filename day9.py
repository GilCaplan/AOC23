with open("input9.txt", "r") as file:
    puzzle_input = [line.strip() for line in file]


def predict_val(values):
    pyramid = [list(map(int, values)), ], next_val = [1]
    while not all(value == 0 for value in next_val):
        next_val = []
        for i in range(len(pyramid[-1])-1):
            next_val.append(pyramid[-1][i+1] - pyramid[-1][i])
        pyramid.append(next_val)
    length = len(pyramid)
    for i in range(length - 1):
        pyramid[length - i - 2].append(pyramid[length - i - 1][-1] + pyramid[length - i - 2][-1])

    return pyramid[0][-1]


print('part 1 solution:', sum(predict_val(line.strip().split()) for line in puzzle_input))
print('part 2 solution:', sum(predict_val(reversed(line.strip().split())) for line in puzzle_input))
