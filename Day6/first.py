import math
from dataclasses import dataclass
from input_reader import read_file
from functools import reduce
import operator

lines = read_file("input.txt")


@dataclass
class Race:
    race_time: int
    distance_to_beat: int


# distance = swimming_time * (race_time - swimming_time)
# distance = - swimming_time^2 + race_time * swimming_time
#
#
# distance_to_beat < swimming_time * (race_time - swimming_time)
# swimming_time^2 - race_time*swimming_time + distance_to_beat < 0
def solve_quadratic_inequality(race: Race):
    a = 1
    b = -1 * race.race_time
    c = race.distance_to_beat
    delta = b ** 2 - 4 * a * c
    root1 = (-b - math.sqrt(delta)) / (2 * a)
    root2 = (-b + math.sqrt(delta)) / (2 * a)
    root1, root2 = min(root1, root2), max(root1, root2)

    root1_up_rounded = math.ceil(root1)
    if root1 == root1_up_rounded:
        root1_up_rounded += 1

    root2_down_rounded = math.floor(root2)
    if root2 == root2_down_rounded:
        root2_down_rounded -= 1

    number_of_solutions = root2_down_rounded - root1_up_rounded + 1
    return number_of_solutions


def process(lines):
    races = get_races(lines)
    return reduce(operator.mul, map(solve_quadratic_inequality, races))


def get_races(lines):
    times = get_digits(lines[0].split(" "))
    distances = get_digits(lines[1].split(" "))
    races = []
    for time, distance in zip(times, distances):
        races.append(Race(time, distance))
    return races


def get_digits(string_arr):
    return [int(x.strip()) for x in string_arr if x.strip().isdigit()]


print(process(lines))
