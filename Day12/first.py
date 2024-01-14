from itertools import groupby

from input_reader import read_file_lines

lines = read_file_lines("input.txt")


def generate_all_permutations(line):
    if "?" not in line:
        return [line]
    else:
        index = line.index("?")
        return (generate_all_permutations(line[:index] + "." + line[index + 1:]) +
                generate_all_permutations(line[:index] + "#" + line[index + 1:]))


def is_valid(p, damaged_spring_groups):
    grouped_hashes = [''.join(group) for char, group in groupby(p) if char == '#']
    if len(grouped_hashes) != len(damaged_spring_groups):
        return False
    return all(len(h) == d for h, d in zip(grouped_hashes, damaged_spring_groups))


def calc_possible_arrangements(line, damaged_spring_groups):
    permutations = generate_all_permutations(line)
    # print(permutations)
    return len([p for p in permutations if is_valid(p, damaged_spring_groups)])


def process(lines):
    return sum(calc_possible_arrangements(item[0], [int(number) for number in item[1].split(",")])
               for line in lines
               for item in [line.strip().split(" ", 1)])


print(process(lines))
