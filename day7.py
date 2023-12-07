from collections import Counter

value = dict(zip('23456789TJQKA', range(13)))
value2 = dict(zip('J23456789TQKA', range(13)))


def get_input():
    inp = list()
    with open("input7.txt", "r") as file:
        for line in file:
            hand, bid = line.strip().split()
            inp.append((hand, int(bid)))
    return inp


def sort_hands(input_hands, part1):
    hands = []
    for hand in input_hands:
        if part1:
            hands.append([sorted([num for _, num in Counter(hand[0]).most_common()], reverse=True), [value[card] for card in hand[0]], [hand[1]]])
        else:
            if hand[0] == 'JJJJJ':
                hands.append([[[5]], [1, 1, 1, 1, 1], [hand[1]]])
            elif 'J' in hand[0]:
                cnt = Counter(hand[0]).most_common()
                rmv = next((i for i, (card, count) in enumerate(cnt) if card == 'J'), None)
                jkr = cnt.pop(rmv)[1]
                srt = [sorted([num for _, num in cnt], reverse=True)]
                cnt[0] = (cnt[0][0], cnt[0][1] + jkr)
                hands.append([srt, [value2[card] for card in list(hand[0])], [hand[1]]])
            else:
                hands.append([[sorted([num for _, num in Counter(hand[0]).most_common()], reverse=True)],
                              [value2[card] for card in list(hand[0])], [hand[1]]])

    hands = sorted(hands, key=lambda hand: hand[0][0], reverse=True)

    hand_types = {str(i): [] for i in range(1, 6)}
    hand_types['full'] = []
    hand_types['high'] = []
    for hand in hands:
        key = (
            '5' if hand[0] == [5] else
            '4' if hand[0] == [4, 1] else
            'full' if hand[0] == [3, 2] else
            '3' if hand[0] == [3, 1, 1] else
            '2' if hand[0] == [2, 2, 1] else
            '1' if hand[0] == [2, 1, 1, 1] else
            'high'
        )
        hand_types[key].append([hand[1], hand[2]])

    for key, value_list in hand_types.items():
        hand_types[key] = sorted(value_list, key=lambda x: x[0])

        # Combine the lists into a single list, sorted by the keys of hand_types
    sorted_result = []
    for key in reversed(['5', '4', 'full', '3', '2', '1', 'high']):
        sorted_result.extend(hand_types[key])

    return sorted_result


inp = get_input()
print(sum((i+1)*bid for i, [_, [bid]] in enumerate(sort_hands(inp, True))))
print(sum((i+1)*bid for i, [_, [bid]] in enumerate(sort_hands(inp, False))))

