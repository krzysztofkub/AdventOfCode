from input_reader import read_file_lines

lines = read_file_lines("test.txt")


def calc_val(numbers):
    first_numbers = [numbers[0]]
    while True:
        numbers = [numbers[i] - numbers[i + 1] for i in range(len(numbers) - 1)]
        first_numbers.append(numbers[0])

        if len(set(numbers)) == 1:
            break

    return sum(first_numbers)


def process(lines):
    return sum([calc_val([int(item) for item in line.strip().split(" ")]) for line in lines])


print(process(lines))
