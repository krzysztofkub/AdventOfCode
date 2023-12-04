from input_reader import read_file


def increment_count():
    global COUNT
    COUNT += 1


def count_winnings(line, line_index, lines):
    increment_count()
    number_sets = line.split(":")[1].split("|")
    scratched_numbers = [int(number.strip()) for number in number_sets[1].split() if number.isdigit()]
    winning_numbers = [int(number.strip()) for number in number_sets[0].split() if number.isdigit()]
    number_of_winners = len(set(scratched_numbers) & set(winning_numbers))
    if number_of_winners > 0:
        for new_index in range(line_index + 1, line_index + number_of_winners + 1):
            count_winnings(lines[new_index], new_index, lines)


def process(lines):
    for line_index, line in enumerate(lines):
        count_winnings(line, line_index, lines)
    print(COUNT)


COUNT = 0
process(read_file("test.txt"))
