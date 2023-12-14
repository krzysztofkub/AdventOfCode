from dataclasses import dataclass


@dataclass
class Part:
    number_part: int
    symbol: chr
    x: int
    y: int
    number_vector: list  # [231 123 123 312]
    sum: int




def set_numbers(chosen_part, lines):
    #   [1st] [2nd] [3rd]
    #   [4th] [ @ ] [5th]
    #   [6th] [7th] [8th]

    end_sum: int = 0

    # 1st position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y - 1].strip()[chosen_part.x - 1].isdigit():

        digit_array = []
        left_upper_number = ""
        i = 0
        if not lines[chosen_part.y - 1].strip()[chosen_part.x].isdigit():
            while lines[chosen_part.y - 1].strip()[chosen_part.x - 1 - i].isdigit():
                digit_array.append(lines[chosen_part.y - 1].strip()[chosen_part.x - 1 - i])
                i += 1
        else:
            digit_array = [0]

        for digit in digit_array[::-1]:
            left_upper_number += str(digit)

        print("Lewa gorna liczba: " + left_upper_number)
        chosen_part.number_vector.append(left_upper_number)
        end_sum+=int(left_upper_number)
    # 2nd position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y - 1].strip()[chosen_part.x].isdigit():

        digit_array = []
        central_upper_number: str = ""
        i = 0
        if not lines[chosen_part.y - 1].strip()[chosen_part.x + 1].isdigit():
            while lines[chosen_part.y - 1].strip()[chosen_part.x - i].isdigit():
                digit_array.append(lines[chosen_part.y - 1].strip()[chosen_part.x - i])
                i += 1
        else:
            digit_array = [0]

        for digit in digit_array[::-1]:
            central_upper_number += str(digit)

        print("Srodkowa gorna liczba: " + central_upper_number)
        chosen_part.number_vector.append(central_upper_number)
        end_sum += int(central_upper_number)
    # 3rd position:
    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y - 1].strip()[chosen_part.x + 1].isdigit():

        digit_array = []
        right_upper_number = ""
        i = 0
        k = 1

        if lines[chosen_part.y - 1].strip()[chosen_part.x].isdigit():

            if lines[chosen_part.y - 1].strip()[chosen_part.x - 1].isdigit():
                while True:
                    if not lines[chosen_part.y - 1].strip()[chosen_part.x - 1 + i].isdigit():
                        while True:
                            if not lines[chosen_part.y - 1].strip()[chosen_part.x - 1 + i - k].isdigit():
                                break
                            digit_array.append(lines[chosen_part.y - 1].strip()[chosen_part.x - 1 + i - k])
                            k += 1
                        break
                    i += 1

            else:
                while lines[chosen_part.y + 1].strip()[chosen_part.x + i].isdigit():
                    digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x + i])
                    print(lines[chosen_part.y + 1].strip()[chosen_part.x + i])
                    i += 1

            for digit in digit_array[::-1]:
                right_upper_number += str(digit)

            print("Prawa gorna liczba: " + right_upper_number)
            chosen_part.number_vector.append(right_upper_number)
            end_sum += int(right_upper_number)
        else:

            while lines[chosen_part.y-1].strip()[chosen_part.x + 1 + i].isdigit():
                digit_array.append(lines[chosen_part.y-1].strip()[chosen_part.x + 1 + i])
                i += 1

            for digit in digit_array:
                right_upper_number += str(digit)

            print("Prawa gorna liczba: " + right_upper_number)
            chosen_part.number_vector.append(right_upper_number)
            end_sum += int(right_upper_number)
        # 4th position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y].strip()[chosen_part.x - 1].isdigit():

        digit_array = []
        left_number = ""
        i = 0
        while lines[chosen_part.y].strip()[chosen_part.x - 1 - i].isdigit():
            digit_array.append(lines[chosen_part.y].strip()[chosen_part.x - 1 - i])
            i += 1

        for digit in digit_array[::-1]:
            left_number += str(digit)

        print("Lewa liczba: " + left_number)
        chosen_part.number_vector.append(left_number)
        end_sum += int(left_number)
        # 5th position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y].strip()[chosen_part.x + 1].isdigit():

        digit_array = []
        right_number = ""
        i = 0

        while lines[chosen_part.y].strip()[chosen_part.x + 1 + i].isdigit():
            digit_array.append(lines[chosen_part.y].strip()[chosen_part.x + 1 + i])
            i += 1

        for digit in digit_array:
            right_number += str(digit)

        print("Prawa liczba: " + right_number)
        chosen_part.number_vector.append(right_number)
        end_sum += int(right_number)
        # 6th position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y + 1].strip()[chosen_part.x - 1].isdigit():

        digit_array = []
        left_lower_number = ""
        i = 0
        if not lines[chosen_part.y + 1].strip()[chosen_part.x].isdigit():
            while lines[chosen_part.y + 1].strip()[chosen_part.x - 1 - i].isdigit():
                digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x - 1 - i])
                i += 1
        else:
            digit_array = [0]

        for digit in digit_array[::-1]:
            left_lower_number += str(digit)

        print("Lewa dolna liczba: " + left_lower_number)
        chosen_part.number_vector.append(left_lower_number)
        end_sum += int(left_lower_number)
        # 7th position:

    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y + 1].strip()[chosen_part.x].isdigit():

        digit_array = []
        central_lower_number: str = ""
        i = 0
        if not lines[chosen_part.y + 1].strip()[chosen_part.x + 1].isdigit():
            while lines[chosen_part.y + 1].strip()[chosen_part.x - i].isdigit():
                digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x - i])
                i += 1
        else:
            digit_array = [0]

        for digit in digit_array[::-1]:
            central_lower_number += str(digit)

        print("Srodkowa dolna liczba: " + central_lower_number)
        chosen_part.number_vector.append(central_lower_number)
        end_sum += int(central_lower_number)
        # 8th position:
    if chosen_part.x > 0 and chosen_part.y > 0 and lines[chosen_part.y + 1].strip()[chosen_part.x + 1].isdigit():

        digit_array = []
        right_lower_number = ""
        i = 0
        k = 1

        if lines[chosen_part.y + 1].strip()[chosen_part.x].isdigit():

            if lines[chosen_part.y + 1].strip()[chosen_part.x - 1].isdigit():
                while True:
                    if not lines[chosen_part.y + 1].strip()[chosen_part.x - 1 + i].isdigit():
                        while True:
                            if not lines[chosen_part.y + 1].strip()[chosen_part.x - 1 + i - k].isdigit():
                                break
                            digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x - 1 + i - k])
                            k += 1
                        break
                    i += 1

            else:
                while lines[chosen_part.y + 1].strip()[chosen_part.x + i].isdigit():
                    digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x + i])
                    print(lines[chosen_part.y + 1].strip()[chosen_part.x + i])
                    i += 1

            for digit in digit_array[::-1]:
                right_lower_number += str(digit)

            print("Prawa dolna liczba: " + right_lower_number)
            chosen_part.number_vector.append(right_lower_number)
            end_sum += int(right_lower_number)
        else:

            while lines[chosen_part.y + 1].strip()[chosen_part.x + 1 + i].isdigit():
                digit_array.append(lines[chosen_part.y + 1].strip()[chosen_part.x + 1 + i])
                i += 1

            for digit in digit_array:
                right_lower_number += str(digit)

            print("Prawa dolna liczba: " + right_lower_number)
            chosen_part.number_vector.append(right_lower_number)
            end_sum += int(right_lower_number)

    print(end_sum)

def print_part(specific_part):
    print(
        str(specific_part.number_part + 1) + " : " + "Dla symbolu: " + specific_part.symbol + "   Pozycja y wynosi: " + str(
            specific_part.y + 1) + "   Pozycja x wynosi: " + str(specific_part.x + 1))


with open("input.txt", 'r') as file:
    x = 0  # index of symbol in line
    y = 0  # index of line in file

    number_part = 0
    part_array = []
    lines = file.readlines()  # lines == ['..233.258.\n', '..636+5832.\n', '...58432.']

    for line in lines:
        line = line.strip()  # line='..233.258.'

        # znajduje pozycje czesci w tablicy i tworze ja jako obiekt, przypisuje wartosci poczatkowe w konstruktorze
        for character in line:
            if character != "." and not character.isdigit():
                part = Part(number_part, character, x, y, [], 0)
                part_array.append(part)  # tworze array wszystkich numerow
                number_part += 1
            x += 1
        x = 0
        y += 1

    # ustawiam wszystkie cyfry w liczby
    for specific_part in part_array:
        set_numbers(specific_part, lines)