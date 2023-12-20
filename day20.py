from collections import deque
from math import lcm
execute = deque([])
low_pulse, high_pulse = 0, 0
part2 = {'ng': 1, 'sv': 1, 'ft': 1, 'jz': 1}
cjj = list(part2.keys())

with open("C:\\Users\\USER\\PycharmProjects\\AOC2023\\input20.txt", 'r') as file:
    input1 = [line.strip().split(' -> ') for line in file]


# ng, sv, ft, jz
# how many cycles does it take for each one to get all high
# (%): if high_pulse nothing, else low_pulse then switch from on to off or off to on
# if was off then send high pulse, if was on then send low_pulse
def flipflop(key, pulse, modules, cycle):
    global high_pulse, low_pulse
    if pulse == 'low':
        modules[key] = (modules[key][0], pl := [1] if modules[key][1] == [0] else [0])
        for kl in modules[key][0]:
            high_pulse += 1 if pl == [1] else 0
            low_pulse += 1 if pl == [0] else 0
            execute.append((kl.strip(), 'high' if pl == [1] else 'low', key))
    # ignore high pulses


# (&): remembers the most recent pulse type from each connected module, default low_pulse
# if all modules pulses are high then send low_pulse else high_pulse
def conjunction(key, pulse, prev_key, modules, cycle):
    global low_pulse, high_pulse
    if prev_key is not None:
        modules[key][1][prev_key] = 0 if pulse == 'low' else 1
    pl = 'low' if sum(modules[key][1].values()) == len(list(modules[key][1].keys())) else 'high'
    if pl == 'high' and key[1:] in list(part2.keys()):
        part2[key[1:]] = cycle
    for kl in modules[key][0]:
        high_pulse += 1 if pl == 'high' else 0
        low_pulse += 1 if pl != 'high' else 0
        kl = kl.strip()
        execute.append((kl, pl, key))


def send_pulses(key, pulse, prev, modules, cycle):
    global low_pulse, high_pulse, execute
    if key == 'broadcaster':
        for module in modules[key][0]:
            module = module.strip()
            low_pulse += 1
            execute.append((module.strip(), 'low', key))
    else:
        if (key if '%' in key else '%'+key) in modules.keys():
            key = key if '%' in key else '%' + key
            flipflop(key, pulse, modules, cycle)
        elif (key if '&' in key else '&'+key) in modules.keys():
            key = key if '&' in key else '&' + key
            conjunction(key, pulse, prev, modules, cycle)


def run(times, prt=True):
    global low_pulse, high_pulse
    low_pulse, high_pulse = 0, 0
    cycle = 0
    modules = {line[0].strip(): (line[1].split(','), [0] if line[0][0] == '%' else {}) for line in input1}
    for m in modules.keys():
        if isinstance(modules[m][1], dict):
            for k2 in modules.keys():
                if m != k2 and m[1:] in modules[k2][0]:
                    modules[m][1][k2] = 0
    for i in range(times):
        low_pulse += 1
        cycle += 1
        send_pulses('broadcaster', 'low', None, modules, cycle)
        while len(execute) > 0:
            k, p, prev = execute.popleft()
            send_pulses(k, p, prev, modules, cycle)
    if prt:
        print(low_pulse, high_pulse)
        print(low_pulse * high_pulse)
    else:
        print(lcm(*list(part2.values())))
        # print(prod(list(part2.values()))) 
        # because in this case all the cycle numbers are prime numbers anyways


run(1000)
run(4000, False)
# for part 2 I make the assumption that I find the cycles for the four modules in less than 4000 cycles (button pressed)
# from the input we can tell that exactly 4 modules [ng, ft, sv, jz] in my puzzle input that go directly to xm module which is a conjunction type, 
# and that goes to rx which we are looking for.
# Therefore in order for a single low pulse to be sent to rx, I need to find the cycle number (buttons pressed) for each of these for module conjunctions
# when they each send a high pulse on the same cycle to - 
# xm conjunction module => xm sends a single low pulse to rx at the lcm (or in this case prod) of those four seperate cycles
