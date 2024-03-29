from input_reader import read_file_lines
from collections import Counter

TYPE_INCREMENT = 10000000000

lines = read_file_lines("input.txt")
cards_hierarchy = "J23456789TQKA"  ##13 elements


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
        hand_without_jokers = hand.replace('J', "")
        char_count = Counter(hand_without_jokers)
        length_of_count = len(char_count)
        if length_of_count == 0:
            hand_without_jokers = "JJJJJ"
            char_count = Counter(hand_without_jokers)
            length_of_count = len(char_count)
            biggest_count = max(char_count.values())
            return (length_of_count * TYPE_INCREMENT) + (biggest_count * -TYPE_INCREMENT) - count_card_values(hand)
        biggest_count = max(char_count.values())
        return (length_of_count * TYPE_INCREMENT) + (biggest_count * -TYPE_INCREMENT) - count_card_values(hand) - (TYPE_INCREMENT * Counter(hand).get("J", 0))

    def __repr__(self):
        return f'{self.hand}, order: {self.order}'


def process(lines):
    actions = sorted(
        [Action("".join(line.split(" ")[0]), int(line.split(" ")[1].strip())) for line in lines],
        key=lambda action: action.order)
    for action in actions:
        print(action)
    return sum([action.bid * (len(actions) - index) for index, action in enumerate(actions)])


print(process(lines))
