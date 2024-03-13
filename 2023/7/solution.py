from pathlib import Path


with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
    hands = [
        (line_split[0], int(line_split[1]))
        for line_split in (line.strip().split(" ") for line in file)
    ]

card_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
cards_strenght = {v: i for (i, v) in enumerate(card_labels)}
total_winnings = 0

hand_types = {
    "5k": [],
    "4k": [],
    "fh": [],
    "3k": [],
    "2p": [],
    "1p": [],
    "hc": [],
}

# divide into different types
for hand in hands:
    cards, _ = hand
    repeated_cards = {}

    for c in cards:
        if c not in repeated_cards:
            repeated_cards[c] = 1
        else:
            repeated_cards[c] = repeated_cards[c] + 1

    repeated_values = list(repeated_cards.values())

    match max(repeated_values):
        case 5:
            hand_types["5k"].append(hand)
        case 4:
            hand_types["4k"].append(hand)
        case 3:
            if 2 in repeated_values:
                hand_types["fh"].append(hand)
            else:
                hand_types["3k"].append(hand)
        case 2:
            repeated_values.remove(2)

            if 2 in repeated_values:
                hand_types["2p"].append(hand)
            else:
                hand_types["1p"].append(hand)
        case _:
            hand_types["hc"].append(hand)


# rank hands within types
rank_list = []


def sort_strength(hand):
    cards, _ = hand
    return [cards_strenght[card] for card in cards]


for hand in hand_types.values():
    rank_list.extend(sorted(hand, key=sort_strength, reverse=True))

for i, (_, bid) in enumerate(reversed(rank_list), start=1):
    total_winnings += i * bid

print(total_winnings)

# hands = {
#     "32T3K": 765,
#     "T55J5": 684,
#     "KK677": 28,
#     "KTJJT": 220,
#     "QQQJA": 483,
# }
