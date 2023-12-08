data = """32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483"""


def sort_cards_key(c, type_prefix):
    c = c.replace('A', 'Z')
    c = c.replace('K', 'Y')
    c = c.replace('Q', 'X')
    c = c.replace('J', '0')
    c = type_prefix + ' ' + c
    return c


cards_map = {
    5: {1: "5K"},
    4: {1: "4K"},
    3: {2: "4H", 1: "3K"},
    2: {2: "2P", 1: "1P"},
    1: {1: "0H"}
}


if __name__ == "__main__":
    lines = data.split("\n")
    hands = []

    for line in lines:
        token = line.split()
        hands.append((token[0], int(token[1])))

    for h, (hand, bid) in enumerate(hands):
        hand_symbols = {}
        for character in hand:
            if character in hand_symbols:
                hand_symbols[character] += 1
            else:
                hand_symbols[character] = 1

        jokers = hand_symbols.get('J', 0)
        if jokers in range(1, 5):
            del hand_symbols['J']
        sorted_hand = sorted(hand_symbols.items(), key=lambda x: x[1], reverse=True)

        if jokers in range(1, 5):
            best_card, count = sorted_hand[0]
            sorted_hand[0] = (best_card, count + jokers)

        most_cards = sorted_hand[0][1]
        if most_cards != 5:
            next_most = sorted_hand[1][1]
        else:
            next_most = 1

        c_type = cards_map[most_cards][next_most]

        key = sort_cards_key(hand, c_type)
        hands[h] = (key, hand, bid)

    ranked = sorted(hands, reverse=True)

    result = 0
    nbr_hands = len(ranked)
    for h, (key, hand, bid) in enumerate(ranked):
        result += (nbr_hands - h) * bid

    print(result)