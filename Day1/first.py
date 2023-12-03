def find_number(line):
    number = 0
    for character in line:
        # check if we didn't just found number as digit
        if number == 0 and character.isdigit():
            number = int(character)
            break
    return number


def fix_string_with_numbers(line):
    first_number = find_number(line)

    reversed_line = line[::-1]
    last_number = find_number(reversed_line)
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
