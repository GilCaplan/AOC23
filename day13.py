with open("input13.txt", "r") as file:
    lines = [line.strip() for line in file]
# different solution which solves both parts

def find_mirror_index(group, mismatch):
    for i in range(1, len(group)):
        if sum(1 for tp, br in zip(group[:i][::-1], group[i:]) for (t, b) in zip(tp, br) if t != b) == mismatch:
            return i
    return 0


for mismatch in [0, 1]:
    group = []
    total = 0
    for line in lines:
        if len(line) == 0:
            total += find_mirror_index(group, mismatch) * 100 + find_mirror_index(list(zip(*group)), mismatch)
            group = []
        else:
            group.append(line)
    print('part', (mismatch+1), 'solution:', total)
