from pathlib import Path

def sort_strength(hand: tuple, cards_strenght: dict[str, int]) -> list[int]:
    cards, _ = hand
    return [cards_strenght[card] for card in cards]

def get_strongest_card(cards: list[str], cards_strenght: dict[str, int]) -> str:
    for k, v in cards_strenght.items():
        if v == max(cards):
            return k

def solution_p1(hands: list[tuple]) -> int:
    card_labels = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
    cards_strenght = {v: i for (i, v) in enumerate(card_labels)}
    hand_types = {k:[] for k in ["5k", "4k", "fh", "3k", "2p", "1p", "hc"]}
    total_winnings = 0

    for hand in hands:
        cards, _ = hand
        repeated_cards = {}

        for c in cards:
            repeated_cards[c] = repeated_cards.get(c, 0) + 1

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

    rank_list = []

    for hand in hand_types.values():
        rank_list.extend(sorted(hand, key=lambda h: sort_strength(h, cards_strenght), reverse=True))

    for i, (_, bid) in enumerate(reversed(rank_list), start=1):
        total_winnings += i * bid
    return total_winnings


def solution_p2(hands: list[tuple]) -> int:
    card_labels = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]
    cards_strenght = {v: i for (i, v) in enumerate(card_labels)}
    hand_types = {k:[] for k in ["5k", "4k", "fh", "3k", "2p", "1p", "hc"]}
    total_winnings = 0

    for hand in hands:
        cards, _ = hand
        repeated_cards = {}

        for c in cards:
            repeated_cards[c] = repeated_cards.get(c, 0) + 1

        if 'J' in cards and repeated_cards['J'] < 5:
            j_value = repeated_cards['J']
            repeated_cards.pop('J')

            most_common_cards = []

            for k, v in repeated_cards.items():
                if v == max(repeated_cards.values()):
                    most_common_cards.append(cards_strenght[k])
                    
            strongest_card = get_strongest_card(most_common_cards, cards_strenght)

            repeated_cards[strongest_card] += j_value

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

    rank_list = []

    for hand in hand_types.values():
        rank_list.extend(sorted(hand, key=lambda h: sort_strength(h, cards_strenght), reverse=True))

    for i, (_, bid) in enumerate(reversed(rank_list), start=1):
        total_winnings += i * bid
    return total_winnings


if __name__ == "__main__":
    with open(Path(__file__).parent.joinpath("input.txt"), "r") as file:
        hands = [
            (line_split[0], int(line_split[1]))
            for line_split in (line.strip().split(" ") for line in file)
        ]
    print(solution_p1(hands))
    print(solution_p2(hands))
