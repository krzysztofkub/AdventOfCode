from dataclasses import dataclass
import re
from math import lcm

from input_reader import read_file

lines = read_file("input.txt")
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


def traverse_to_zzz_iterative(nodes_dict, instructions, curr_value):
    index = -1

    while curr_value is not None:
        index += 1
        curr_node = nodes_dict.get(curr_value)

        if curr_value.endswith('Z'):
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


def map_node(index, instructions, nodes_dict, curr_value):
    curr_node = nodes_dict.get(curr_value)
    if len(instructions) > index:
        direction = instructions[index]
    else:
        direction = instructions[index % len(instructions)]
    if direction == "R":
        curr_value = curr_node.right
    else:
        curr_value = curr_node.left
    return curr_value


def process(lines):
    instructions = [x for x in lines[0].strip()]
    nodes_dict = {map_to_node(line)[0]: map_to_node(line)[1] for index, line in enumerate(lines[2:])}

    pattern = re.compile(r'.*A$')

    totals = [traverse_to_zzz_iterative(nodes_dict, instructions, key) for key in nodes_dict if pattern.match(key)]
    return lcm(*totals)


print(process(lines))
