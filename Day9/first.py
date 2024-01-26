from input_reader import read_file_lines

lines = read_file_lines("input.txt")


def calc_val(numbers):
    last_numbers = [numbers[-1]]
    while len(set(numbers)) != 1:
        numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        last_numbers.append(numbers[-1])
    return sum(last_numbers)


def process(lines):
    return sum([calc_val([int(item) for item in line.strip().split(" ")]) for line in lines])


print(process(lines))
