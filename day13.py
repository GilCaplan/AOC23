with open("input13.txt", "r") as file:
    lines = [line.strip() for line in file]


def count_reflections(group):
    ver, hor = count_ref(group)[0], 100*count_ref(list(zip(*group)))[0]
    return hor + ver


# still working on part 2 :/
def fix_smudge(group):
    group = [list(row) for row in group]  # Convert tuple to list
    ver, r_ver = count_ref(group)
    hor, r_hor = count_ref(list(zip(*group)))

    for j in range(len(group[0])):
        for i in range(len(group)):
            group[i][j] = '.' if group[i][j] == '#' else '#'

            new_ver, new_r_ver = count_ref(group)
            new_hor, new_r_hor = count_ref(list(zip(*group)))
            flag = (new_hor == 0 and new_ver == 0)

            if new_ver != ver and not any(val in r_ver for val in new_r_ver) and not flag:
                return new_ver

            if new_hor != hor and not any(val in r_hor for val in new_r_hor) and not flag:
                return new_hor * 100

            group[i][j] = '.' if group[i][j] == '#' else '#'

    return 0


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
print(total)
total = 0
for line in lines:
    if len(line) == 0:
        total += fix_smudge(list(zip(*group)))
        group = []
    else:
        group.append(line)
print(total)
