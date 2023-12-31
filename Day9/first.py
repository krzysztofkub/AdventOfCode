from input_reader import read_file

lines = read_file("input.txt")


def calc_val(numbers):
    last_numbers = [numbers[-1]]
    while True:
        numbers = [numbers[i + 1] - numbers[i] for i in range(len(numbers) - 1)]
        last_numbers.append(numbers[-1])

        if len(set(numbers)) == 1:
            break

    return sum(last_numbers)


def process(lines):
    return sum([calc_val([int(item) for item in line.strip().split(" ")]) for line in lines])


print(process(lines))
