import sys

sys.path.append('C:/Users/Admin/PycharmProjects/AdventOfCode')
from classes import Mappers, Mapper, Number_Range
from input_reader import read_file

lines = read_file("input.txt")


def to_mapper(lines):
    lines.pop(0)
    mappers = Mappers()
    current_mapper = ''
    single_type_mappers = []
    for line_index, line in enumerate(lines):
        first_char = line[0]
        if first_char.isalpha():
            current_mapper = line.split(" ")[0].replace("-", "_")
        if first_char.isdigit():
            splitted_line = line.split(" ")
            destination_range_start = int(splitted_line[0])
            source_range_start = int(splitted_line[1])
            mapping_range = int(splitted_line[2].strip())

            single_type_mappers.append(Mapper(source_range_start, destination_range_start, mapping_range))

        if line == '\n' and current_mapper != '' or line_index == len(lines) - 1:
            mappers.set_value(current_mapper, single_type_mappers)
            single_type_mappers = []
    return mappers


def get_seeds_ranges(line):
    seeds = []
    numbers = line.split("seeds: ")[1].split(" ")
    for index, number in enumerate(numbers):
        number = int(number.strip())
        if index % 2 == 0:
            seeds.append(Number_Range(number, number + int(numbers[index + 1].strip()) - 1))
    return seeds


def get_destination_ranges(type_mappers, input: [Number_Range]):
    ranges = []
    for input_range in input:
        for mapper in type_mappers:
            destination_range = mapper.get_destination_range(input_range)
            if destination_range is not None:
                ranges.append(destination_range)

        ranges_without_mappers = input_range.get_ranges_without_mappers()
        if ranges_without_mappers:
            ranges.extend(ranges_without_mappers)
        input_range.checked_against = []
    return ranges


def calculate_location_range(seed, mappers):
    soil_number = get_destination_ranges(mappers.seed_to_soil, [seed])
    fertilizer_number = get_destination_ranges(mappers.soil_to_fertilizer, soil_number)
    water_number = get_destination_ranges(mappers.fertilizer_to_water, fertilizer_number)
    light_number = get_destination_ranges(mappers.water_to_light, water_number)
    temperature_number = get_destination_ranges(mappers.light_to_temperature, light_number)
    humidity_number = get_destination_ranges(mappers.temperature_to_humidity, temperature_number)
    location_number = get_destination_ranges(mappers.humidity_to_location, humidity_number)
    return location_number


def process(lines):
    seeds_ranges = get_seeds_ranges(lines[0])
    mappers = to_mapper(lines)
    min_location = None
    for seed_range in seeds_ranges:
        location_ranges = calculate_location_range(seed_range, mappers)
        temp_min_location = min(location_ranges, key=lambda x: x.start).start

        if min_location is None or temp_min_location < min_location:
            min_location = temp_min_location
    return min_location

print(process(lines))