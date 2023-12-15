encoded = open("input15.txt", "r").readline().split(',')
hash = lambda x, y: ((ord(x)+int(y)) * 17) % 256


def hol(dec):
    t = 0
    for d in dec:
        t = hash(d, t)
    return t


box = {i: [] for i in range(256)}
for dec in encoded:
    if '=' in dec:
        d = dec.split('=')
        h = hol(d[0])
        if d[0] in [val[0] for val in box[h] if len(val) > 0]:
            for i in range(len(box[h])):
                if box[h][i][0] == d[0]:
                    box[h][i][1] = d[1]
        else:
            box[h].append([d[0], d[1]])
    else:
        d = dec.split('-')[0]
        box[hol(d)] = [item for item in box[hol(d)] if item[0] != d]
print('part 1', sum(hol(dec) for dec in encoded))
print('part 2', sum(sum((key+1) * (1+i) * int(pair[1]) for i, pair in enumerate(box[key])) for key in box.keys()))
