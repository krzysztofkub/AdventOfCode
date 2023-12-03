from functools import reduce
from operator import mul
import re


def map_to_multiplied(line):
    possible_game_to_check = {}

    cubes_str = line.split(': ')[1]
    cube_arr = re.split('; |, ', cubes_str)
    for cube in cube_arr:
        cube_parts = cube.split(" ")
        cube_count = int(cube_parts[0])
        cube_color = cube_parts[1].rstrip()

        if cube_color not in possible_game_to_check:
            possible_game_to_check[cube_color] = cube_count

        if possible_game_to_check[cube_color] < cube_count:
            possible_game_to_check[cube_color] = cube_count

    values = possible_game_to_check.values()
    return reduce(mul, values, 1)


def resolve():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
        added = 0
        for line in lines:
            number = map_to_multiplied(line)
            added += number

    return added


print(resolve())
