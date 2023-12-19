puzzle = [line.strip().split() for line in open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input19.txt", 'r').readlines()]
rules, scores, xmas = {}, [], {'x': 0, 'm': 1, 'a': 2, 's': 3}


def find_nth_appearance(arr, trg, n):
    cnt = 0
    for i, letter in enumerate(arr):
        if letter == trg and cnt == n:
            return i
        cnt += 1 if letter == trg else 0
    return -1


def checkPiece(line, rules, k):
    if k in ['A', 'R']:
        return k
    rule = rules[k]
    keys = list(rule.keys())
    letters = [e[0] for e in keys if rule[e] is not None]
    recnt = [0, 0, 0, 0]
    for l in letters:
        i = find_nth_appearance(letters, l, recnt[xmas[l]])
        recnt[xmas[l]] += 1
        if keys[i][1] == '>' and line[xmas[l]] > int(keys[i][2:]):
            return checkPiece(line, rules, rule[keys[i]])
        elif keys[i][1] == '<' and line[xmas[l]] < int(keys[i][2:]):
            return checkPiece(line, rules, rule[keys[i]])
    return checkPiece(line, rules, keys[len(keys)-1])


rules_input, parts_input = open("input19.txt", 'r').read().split("\n\n")
for line in rules_input.split('\n'):
    key, val = line.split('{')
    val = val[:len(val)-1]
    rules[key] = {v.split(':')[0]: v.split(':')[1] if len(v.split(':')) > 1 else None for v in val.split(',')}


for line in parts_input.split('\n'):
    piece = checkPiece(point := [int(item[2:]) for item in line[1:len(line)-1].split(',')], rules, 'in')
    scores.append(sum(point) if piece == 'A' else 0)

print(sum(scores))
