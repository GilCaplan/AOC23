with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input13.txt", "r") as file:
    lines = [line.strip() for line in file]


def count_reflections(group):
    ver, hor = count_ref(group)[0], 100*count_ref(list(zip(*group)))[0]
    return hor + ver


def count_ref(group):
    total, save = 0, []
    length = len(group)
    for i in range(length - 1):
        if group[i] == group[i+1]:
            j = 1
            while i - j >= 0 and i + 1 + j < length:
                if group[i-j] != group[i+1+j]:
                    break
                else:
                    j += 1
            if (i - j == -1 or i + 1 + j == length) and group[i-j+1] == group[i+j]:
                total += i+1
                save.append(i)
    return total, save


group = []
total = 0

for line in lines:
    if len(line) == 0:
        total += count_reflections(list(zip(*group)))
        group = []
    else:
        group.append(line)
print('part 1 ', total)
