import itertools as it
from dataclasses import dataclass
from input_reader import read_file

lines = read_file("input.txt")


@dataclass
class Node:
    x: int
    y: int


def expand(lines):
    rows_to_expand = [index for index, line in enumerate(lines) if line.replace(".", "") == ""]
    cols_to_expand = [i for i in range(len(lines[0])) if ''.join(string[i] for string in lines).replace(".", "") == ""]

    expanded = []
    for line_index, line in enumerate(lines):
        new_line = ""
        for char_index, char in enumerate(line):
            new_line += char
            if char_index in cols_to_expand:
                new_line += "."

        expanded.append(new_line)
        if line_index in rows_to_expand:
            expanded.append(''.join("." for string in expanded[0]))
    print(expanded)
    return expanded


def process(lines):
    lines = [line.strip() for line in lines]
    lines = expand(lines)
    nodes = []
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == "#":
                nodes.append(Node(char_index, line_index))

    return sum([abs(a.x - b.x) + abs(a.y - b.y) for a, b in it.combinations(nodes, 2)])




print(process(lines))