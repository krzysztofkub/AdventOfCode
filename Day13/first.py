import math

from input_reader import read_file


# def find_reflection_index(strings):
#     strings_last_index = len(strings) - 1
#     for i in range(strings_last_index, 0, -1):
#         right = strings[i:strings_last_index + 1]
#         left = strings[0:i]
#
#         if (len(left) >= len(right)):
#             right_to_compare = right[::-1]
#             left_to_compare = left[len(left) - len(right): len(left) - len(right) + len(right)]
#         else:
#             right_to_compare = right[len(right) - len(left): len(right) - len(left) + len(left)][::-1]
#             left_to_compare = left
#
#         if right_to_compare == left_to_compare:
#             reflection_index = (i, i + 1)
#             print(reflection_index)
#             return reflection_index
#
#     return None


def find_reflection_index(strings):
    middle_index = len(strings) / 2
    nearest_reflection_to_middle = None
    for i in range(1, len(strings)):
        left = strings[0:i][::-1]
        right = strings[i:len(strings)]
        match = all(item1 == item2 for item1, item2 in zip(left, right))
        if match:
            if nearest_reflection_to_middle is None:
                nearest_reflection_to_middle = i
            elif abs(middle_index - i) < abs(middle_index - nearest_reflection_to_middle):
                nearest_reflection_to_middle = i

    if nearest_reflection_to_middle is not None:
        print(f'({nearest_reflection_to_middle}, {nearest_reflection_to_middle + 1})')

    return nearest_reflection_to_middle


def process_pattern(lines):
    index = find_reflection_index(lines)
    if index is None:
        columns = [''.join(string[i] for string in lines) for i in range(len(lines[0]))]
        index = find_reflection_index(columns)
        if index is None:
            raise Exception
        return index
    else:
        return 100 * index


print(sum([process_pattern(patter.split("\n")) for patter in read_file("input.txt").split("\n\n")]))
