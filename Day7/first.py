from input_reader import read_file
from collections import Counter

lines = read_file("input.txt")
cards_hierarchy = "23456789TJQKA"  ##13 elements


def get_card_value(char):
    return cards_hierarchy.index(char) + 2


def count_card_values(hand):
    return sum([get_card_value(card) * pow(100, len(hand) - index - 1) for index, card in enumerate(hand)])


class Action:
    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = bid
        self.order = self.calculate_order(hand)

    @staticmethod
    def calculate_order(hand):
        char_count = Counter(hand)
        length_of_count = len(char_count)
        biggest_count = max(char_count.values())
        return (length_of_count * 10000000000) + (biggest_count * -10000000000) - count_card_values(hand)


def process(lines):
    actions = sorted(
        [Action("".join(line.split(" ")[0]), int(line.split(" ")[1].strip())) for line in lines],
        key=lambda action: action.order)
    return sum([action.bid * (len(actions) - index) for index, action in enumerate(actions)])


print(process(lines))
