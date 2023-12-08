data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""

combinations = {
    "high": [],
    "one": [],
    "two": [],
    "three": [],
    "full house": [],
    "four": [],
    "five": [],
}


def sort_cards(c):
    c = c.replace("A", "E")
    c = c.replace("K", "D")
    c = c.replace("Q", "C")
    c = c.replace("J", "B")
    c = c.replace("T", "A")
    return c


if __name__ == "__main__":
    result = 0
    data_dict = {}
    for line in data.split("\n"):
        line_parts = line.split()
        data_dict[line_parts[0]] = int(line_parts[1])
        hand_symbols = {}
        for character in line_parts[0]:
            if character in hand_symbols:
                hand_symbols[character] += 1
            else:
                hand_symbols[character] = 1

        if len(hand_symbols) == 1:
            combinations["five"].append(line_parts[0])
        elif len(hand_symbols) == 2:
            for hand in hand_symbols.values():
                if hand in [2, 3]:
                    combinations["full house"].append(line_parts[0])
                    break
            else:
                combinations["four"].append(line_parts[0])
        elif len(hand_symbols) == 3:
            for hand in hand_symbols.values():
                if hand == 3:
                    combinations["three"].append(line_parts[0])
                    break
            else:
                combinations["two"].append(line_parts[0])
        elif len(hand_symbols) == 4:
            combinations["one"].append(line_parts[0])
        elif len(hand_symbols) == 5:
            combinations["high"].append(line_parts[0])
    rank = 1
    for combination in combinations:
        sorted_combination = sorted(combinations[combination], key=sort_cards)
        for x in sorted_combination:
            result += rank*data_dict[x]
            rank += 1
    print(result)
