from functools import reduce
from operator import add

possible_game_to_check = {
    "red": 12,
    "green": 13,
    "blue": 14
}


def prepare_color_dict_set(game):
    game_parts = game.split(':')[1].split(';')
    game_sets = []

    for part in game_parts:
        elements = [element.strip() for element in part.split(',')]
        dict = {}
        for element in elements:
            count, color = element.split()
            dict[color] = int(count)
        game_sets.append(dict)
    return game_sets


def get_game_id_if_possible(game):
    cube_check_set = prepare_color_dict_set(game)
    for possible_color in possible_game_to_check:
        for check_dict in cube_check_set:
            if possible_color not in check_dict:
                continue

            checked_color_value = int(check_dict[possible_color])
            if checked_color_value > int(possible_game_to_check[possible_color]):
                return False
    return True


def map_to_game_id(game):
    return int(game[5:game.find(':')].strip())


def resolve():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        filtered_lines = list(filter(get_game_id_if_possible, lines))
        total_sum = reduce(add, map(map_to_game_id, filtered_lines), 0)
    return total_sum


print(resolve())
