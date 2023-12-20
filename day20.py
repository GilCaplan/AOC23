from collections import deque
from math import lcm
# print(((224602011344203//20000) * 16) /3600)
execute = deque([])
low_pulse, high_pulse = 0, 0
part2 = {'ng': 1, 'sv': 1, 'ft': 1, 'jz': 1}
cjj = list(part2.keys())
cycle = 0
# ng, sv, ft, jz
# how many cycles does it take for each one to get all high
# (%): if high_pulse nothing, else low_pulse then switch from on to off or off to on
# if was off then send high pulse, if was on then send low_pulse
def flipflop(key, pulse):
    global high_pulse, low_pulse, modules, cycle
    if pulse == 'low':
        modules[key] = (modules[key][0], pl := [1] if modules[key][1] == [0] else [0])
        for kl in modules[key][0]:
            high_pulse += 1 if pl == [1] else 0
            low_pulse += 1 if pl == [0] else 0
            execute.append((kl.strip(), 'high' if pl == [1] else 'low', key))
    # ignore high pulses


# (&): remembers the most recent pulse type from each connected module, default low_pulse
# if all modules pulses are high then send low_pulse else high_pulse
def conjunction(key, pulse, prev_key):
    global low_pulse, high_pulse, cycle
    if prev_key is not None:
        modules[key][1][prev_key] = 0 if pulse == 'low' else 1
    pl = 'low' if sum(modules[key][1].values()) == len(list(modules[key][1].keys())) else 'high'
    for kl in modules[key][0]:
        high_pulse += 1 if pl == 'high' else 0
        low_pulse += 1 if pl != 'high' else 0
        kl = kl.strip()
        execute.append((kl, pl, key))

def send_pulses(key, pulse, prev):
    global low_pulse, high_pulse, execute, modules, cycle
    if key == 'broadcaster':
        for module in modules[key][0]:
            module = module.strip()
            low_pulse += 1
            execute.append((module.strip(), 'low', key))
    else:
        if (key if '%' in key else '%'+key) in modules.keys():
            key = key if '%' in key else '%' + key
            flipflop(key, pulse)
        elif (key if '&' in key else '&'+key) in modules.keys():
            key = key if '&' in key else '&' + key
            conjunction(key, pulse, prev)


with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input20.txt", 'r') as file:
    input1 = [line.strip().split(' -> ') for line in file]
modules = {line[0].strip(): (line[1].split(','), [0] if line[0][0] == '%' else {}) for line in input1}
for m in modules.keys():
    if isinstance(modules[m][1], dict):
        for k2 in modules.keys():
            if m != k2 and m[1:] in modules[k2][0]:
                modules[m][1][k2] = 0
for i in range(1000):
    low_pulse += 1

    send_pulses('broadcaster', 'low', None)
    while len(execute) > 0:
        k, p, prev = execute.popleft()
        send_pulses(k, p, prev)
# print(low_pulse, high_pulse)
print(low_pulse * high_pulse)
for cj in list(part2.keys()):
    cycle = 0
    modules = {line[0].strip(): (line[1].split(','), [0] if line[0][0] == '%' else {}) for line in input1}
    for _ in range(4000):
        low_pulse += 1
        cycle += 1
        send_pulses('broadcaster', 'low', None)
        while len(execute) > 0:
            k, p, prev = execute.popleft()
            send_pulses(k, p, prev)
        if sum(part2.values())/4 == list(part2.values())[0] and cycle > 5:
            break
# just part 1, part two should be able to be solved with lcm, but for some reason I am not able to currently find those cycles with this code
