wordsToNumbers = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9
}


def is_any_number_yet(substring):
    for number in wordsToNumbers:
        if number in substring:
            return wordsToNumbers.get(number)
    return None


def find_first_number(line):
    substring = ''
    number = 0
    for character in line:
        # check if we didn't just found number as digit
        if number == 0 and character.isdigit():
            number = int(character)
            break

        substring += character
        possible_number = is_any_number_yet(substring)
        if possible_number is not None:
            number = possible_number
            break
    return number


def find_last_number(line):
    substring = ''
    number = 0
    for character in line:
        # check if we didn't just found number as digit
        if number == 0 and character.isdigit():
            number = int(character)
            break

        substring = character + substring
        possible_number = is_any_number_yet(substring)
        if possible_number is not None:
            number = possible_number
            break
    return number


def fix_string_with_numbers(line):
    first_number = find_first_number(line)

    reversed_line = line[::-1]
    last_number = find_last_number(reversed_line)
    return first_number * 10 + last_number


def resolve():
    sum = 0
    with open('input.txt', 'r') as file:
        for line in file:
            try:
                sum += fix_string_with_numbers(line)
            except Exception as e:
                print(f"An error occurred in line: {line} : {e}")
    return sum


print(resolve())
