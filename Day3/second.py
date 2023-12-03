from typing import List

from Day3.classes_with_mappers import map_to_line_dataclass, Gear


def add_numbers_from_indexes(gear, line, indexes_to_check):
    for number in line.numbers:
        if set(indexes_to_check).intersection(set(number.number_chars_indexes)):
            gear.add_number(number.value)


def find_valid_gears_ratio(lines_arr):
    gear_ratios = []
    # map string to dataclasses
    lines = []
    for line_index, line_string in enumerate(lines_arr):
        lines.append(map_to_line_dataclass(line_string.strip(), line_index))

    # process dataclasses
    for line in lines:
        star_indexes = line.star_symbol_indexes
        if len(star_indexes) == 0:
            continue

        for star_index in star_indexes:
            gear = Gear(star_index)

            # get numbers from same line
            indexes_to_check = [star_index - 1, star_index + 1, star_index]
            lines_to_check = [line_to_check for line_to_check in lines if
                              line_to_check.index in range(line.index - 1, line.index + 2)]
            for line_to_check in lines_to_check:
                add_numbers_from_indexes(gear, line_to_check, indexes_to_check)
            gear_ratios.append(gear.calculate_ratio())

    return gear_ratios


def resolve():
    with open('input.txt', 'r') as file:
        numbers = find_valid_gears_ratio(file.readlines())
    print(numbers)
    return sum(numbers)


print(resolve())
