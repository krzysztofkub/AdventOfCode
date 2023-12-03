from typing import List

from Day3.classes_with_mappers import map_to_line_dataclass


def do_line_have_symbols_at_indexes(line, indexes_to_check):
    symbols_indexes = line.symbols_indexes
    return set(indexes_to_check).intersection(set(symbols_indexes))


def find_valid_engine_parts(lines_arr):
    valid_engine_parts = []
    # map string to dataclasses
    lines = []
    for line_index, line_string in enumerate(lines_arr):
        lines.append(map_to_line_dataclass(line_string.strip(), line_index))

    # process dataclasses
    for line in lines:
        numbers = line.numbers
        if len(numbers) == 0:
            continue

        for number in numbers:
            first_number_index = number.number_chars_indexes[0]
            last_number_index = number.number_chars_indexes[len(number.number_chars_indexes) - 1]

            # check if symbol is in the same line
            indexes_to_check_for_same_line = [first_number_index - 1, last_number_index + 1]
            if do_line_have_symbols_at_indexes(line, indexes_to_check_for_same_line):
                valid_engine_parts.append(number.value)
                continue

            # check if symbol is in the adjacent lines
            adjacent_lines = [adjacent_line for adjacent_line in lines if
                              adjacent_line.index == line.index - 1 or adjacent_line.index == line.index + 1]
            indexes_to_check_for_adjacent_lines = indexes_to_check_for_same_line + number.number_chars_indexes
            for adjacent_line in adjacent_lines:
                if do_line_have_symbols_at_indexes(adjacent_line, indexes_to_check_for_adjacent_lines):
                    valid_engine_parts.append(number.value)
                    break

    return valid_engine_parts


def resolve():
    with open('input.txt', 'r') as file:
        numbers = find_valid_engine_parts(file.readlines())
    print(numbers)
    return sum(numbers)


print(resolve())
