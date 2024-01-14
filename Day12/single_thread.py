import time
from itertools import groupby

from input_reader import read_file_lines

lines = read_file_lines("test.txt")


def is_valid_so_far(line, damaged_spring_groups):
    line_so_far_processed = line.split("?")[0]
    grouped_hashes = [''.join(group) for char, group in groupby(line_so_far_processed) if char == '#']

    if not grouped_hashes:
        return True

    if len(line_so_far_processed) < len(line) and line[len(line_so_far_processed)] == "?":
        grouped_hashes.pop()

    return all(len(h) == d for h, d in zip(grouped_hashes, damaged_spring_groups))


def generate_all_permutations(line, unfolded_damaged_spring_groups):
    stack = [(line, 0)]  # Stack stores tuples of (current string, current index)
    permutations = []

    while stack:
        current_line, index = stack.pop()

        # Check for validity early to avoid unnecessary processing
        if not is_valid_so_far(current_line, unfolded_damaged_spring_groups):
            continue

        # Find the next question mark to replace, starting from the current index
        next_question_mark = current_line.find("?", index)

        if next_question_mark == -1:
            # No more question marks - add to permutations
            permutations.append(current_line)
        else:
            # Push the next states to the stack
            stack.append((current_line[:next_question_mark] + "." + current_line[next_question_mark + 1:], next_question_mark + 1))
            stack.append((current_line[:next_question_mark] + "#" + current_line[next_question_mark + 1:], next_question_mark + 1))

    return permutations


def is_valid(p, damaged_spring_groups):
    grouped_hashes = [''.join(group) for char, group in groupby(p) if char == '#']
    if len(grouped_hashes) != len(damaged_spring_groups):
        return False
    return all(len(h) == d for h, d in zip(grouped_hashes, damaged_spring_groups))


def calc_possible_arrangements(line, damaged_spring_groups):
    unfolded_line = line
    unfolded_damaged_spring_groups = damaged_spring_groups
    for i in range(0, 4):
        unfolded_line = unfolded_line + "?" + line
        unfolded_damaged_spring_groups = unfolded_damaged_spring_groups + damaged_spring_groups
    permutations = generate_all_permutations(unfolded_line, unfolded_damaged_spring_groups)
    print(f'generated {len(permutations)} for line {line}')
    valid_permutations = [p for p in permutations if is_valid(p, unfolded_damaged_spring_groups)]
    return len(valid_permutations)


def process(lines):
    return sum(calc_possible_arrangements(item[0], [int(number) for number in item[1].split(",")])
               for line in lines
               for item in [line.strip().split(" ", 1)])


start_time = time.time()
print(process(lines))
elapsed_time = (time.time() - start_time) * 1000  # Convert to milliseconds
print(f'elapsed time: {elapsed_time}')
