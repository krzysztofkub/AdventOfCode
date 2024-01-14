from dataclasses import dataclass

from input_reader import read_file_lines

lines = read_file_lines("input.txt")
counter = 0


@dataclass
class Node:
    left: str
    right: str


def map_to_node(line):
    value, nodes = line.split(" = ")
    left, right = nodes.split(", ")

    left_value = left[1:]
    right_value = right.strip()[:-1]
    return value, Node(left_value, right_value)


def traverse_to_zzz_iterative(nodes_dict, instructions):
    curr_value = "AAA"
    index = -1

    while curr_value is not None:
        index += 1
        curr_node = nodes_dict.get(curr_value)

        if curr_value == "ZZZ":
            return index

        if len(instructions) > index:
            direction = instructions[index]
        else:
            direction = instructions[index % len(instructions)]

        if direction == "R":
            curr_value = curr_node.right
        else:
            curr_value = curr_node.left

    return None


def process(lines):
    instructions = [x for x in lines[0].strip()]
    nodes_dict = {map_to_node(line)[0]: map_to_node(line)[1] for index, line in enumerate(lines[2:])}
    return traverse_to_zzz_iterative(nodes_dict, instructions)


print(process(lines))
