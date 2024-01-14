from input_reader import read_file


def find_reflection_index(strings):
    for i in range(1, len(strings)):
        left = strings[0:i][::-1]
        right = strings[i:len(strings)]
        match = all(item1 == item2 for item1, item2 in zip(left, right))
        if match:
            print(f'({i}, {i + 1})')
            return i


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
