from math import prod
from copy import deepcopy as dp
puzzle = [line.strip().split() for line in open("input19.txt", 'r').readlines()]
rules, scores, xmas = {'x': 0, 'm': 1, 'a': 2, 's': 3}, [], {'x': 0, 'm': 1, 'a': 2, 's': 3}
s = [set(i for i in range(1, 4001)) for _ in range(4)]
cnt = []


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


def part2(key, part):
    global rules
    if key == 'A':
        cnt.append(part)
        return
    elif key != 'R':
        for rule in rules[key]:
            if len(rule) == 1:
                part2(rule[0], dp(part))
            else:
                field_key, condition, amount, destination = rule
                current_field = part[field_key]
                lower, higher = set(range(1, amount + 1)), set(range(amount, 4001))
                new = current_field - (lower if condition == ">" else higher)
                part[field_key] = current_field - new
                new_part = dp(part)
                new_part[field_key] = new
                part = dp(part)
                part2(destination, new_part)


rules_input, parts_input = open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input19.txt", 'r').read().split("\n\n")
for line in rules_input.split('\n'):
    key, val = line.split('{')
    val = val[:len(val)-1]
    rules[key] = {v.split(':')[0]: v.split(':')[1] if len(v.split(':')) > 1 else None for v in val.split(',')}


for line in parts_input.split('\n'):
    piece = checkPiece(point := [int(item[2:]) for item in line[1:len(line)-1].split(',')], rules, 'in')
    scores.append(sum(point) if piece == 'A' else 0)

print(sum(scores))
new_rules = {}
for line in rules_input.splitlines():
    key, rule_string = line[:-1].split("{")
    rules_list = []
    for rule in rule_string.split(","):
        if ":" not in rule:
            rules_list.append(list([rule]))
        else:
            rule, destination = rule.split(":")
            rules_list.append((rule[0], rule[1:2], int(rule[2:]), destination))
    rules[key] = rules_list


part2("in", {s: set(range(1, 4001)) for s in "xmas"})
print(sum(prod(len(field) for field in part.values()) for part in cnt))

