from input_reader import read_file_lines


def count_winnings(line):
    number_sets = line.split(":")[1].split("|")
    scratched_numbers = [int(number.strip()) for number in number_sets[1].split() if number.isdigit()]
    winning_numbers = [int(number.strip()) for number in number_sets[0].split() if number.isdigit()]
    number_of_winners = len(set(scratched_numbers) & set(winning_numbers))
    return 0 if number_of_winners == 0 else pow(2, number_of_winners - 1)


def process(lines):
    winnings = [count_winnings(line) for line in lines]
    return sum(winnings)


print(process(read_file_lines("input.txt")))
