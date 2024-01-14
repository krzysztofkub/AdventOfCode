import itertools as it
from dataclasses import dataclass
from input_reader import read_file_lines

lines = read_file_lines("input.txt")


@dataclass
class Node:
    x: int
    y: int


def get_expand_values(lines):
    rows_to_expand = [index for index, line in enumerate(lines) if line.replace(".", "") == ""]
    cols_to_expand = [i for i in range(len(lines[0])) if ''.join(string[i] for string in lines).replace(".", "") == ""]
    return rows_to_expand, cols_to_expand


def get_range(a, b):
    min_ = min(a, b)
    max_ = max(a, b)
    return range(min_, max_)


def process(lines):
    lines = [line.strip() for line in lines]
    rows_to_expand, cols_to_expand = get_expand_values(lines)
    nodes = []
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "#":
                nodes.append(Node(char_index, line_index))

    distances = []
    for a, b in it.combinations(nodes, 2):
        x_range = get_range(a.x, b.x)
        y_range = get_range(a.y, b.y)
        x_range_expanded = len([i for i in cols_to_expand if i in x_range]) * 999999
        y_range_expanded = len([i for i in rows_to_expand if i in y_range]) * 999999
        x_length = abs(a.x - b.x) + x_range_expanded
        y_length = abs(a.y - b.y) + y_range_expanded
        distances.append(x_length + y_length)
    return sum(distances)


print(process(lines))
