from dataclasses import dataclass
from typing import List


@dataclass
class Number:
    value: int
    number_chars_indexes: List[int]


@dataclass
class Line:
    index: int
    numbers: List[Number]
    symbols_indexes: List[int]
    star_symbol_indexes: List[int]


def map_to_numbers_dataclass_arr(line_string):
    numbers = []

    current_number = None
    for char_index, char in enumerate(line_string):
        if char.isdigit():
            if current_number is None:
                current_number = int(char)
                current_number_indexes = [char_index]
            else:
                current_number = current_number * 10 + int(char)
                current_number_indexes.append(char_index)
        elif current_number is not None:
            numbers.append(Number(current_number, current_number_indexes))
            current_number = None

    # Check for a number at the end of the string
    if current_number is not None:
        numbers.append(Number(current_number, current_number_indexes))

    return numbers


def find_symbols_indexes(line_string):
    return [index for index, char in enumerate(line_string) if not (char.isalpha() or char.isdigit() or char == ".")]


def find_star_symbol_indexes(line_string):
    return [index for index, char in enumerate(line_string) if char == "*"]


def map_to_line_dataclass(line_string, line_index):
    numbers = map_to_numbers_dataclass_arr(line_string)
    symbols_indexes = find_symbols_indexes(line_string)
    gears_indexes = find_star_symbol_indexes(line_string)
    return Line(line_index, numbers, symbols_indexes, gears_indexes)


class Gear:
    def __init__(self, index):
        self.numbers = []
        self.index = index

    def add_number(self, number):
        self.numbers.append(number)
        return len(self.numbers) > 2

    def calculate_ratio(self):
        if len(self.numbers) != 2:
            return 0
        return self.numbers[0] * self.numbers[1]
