from input_reader import read_file


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
