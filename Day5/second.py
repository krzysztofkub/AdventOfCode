from Day5.classes import Mappers, Mapper, Number_Range
from input_reader import read_file

lines = read_file("test.txt")


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


def get_seeds(line):
    seeds = []
    numbers = line.split("seeds: ")[1].split(" ")
    for index, number in enumerate(numbers):
        number = int(number.strip())
        if index % 2 == 0:
            seeds.append(Number_Range(number, int(numbers[index + 1].strip())))

    return seeds


def get_range(type_mappers, input_range):
    for mapper in type_mappers:
        destination = mapper.get_destination_range(input_range)
        if destination is not None:
            return destination
    return input_range


def calculate_min_location(seed_range, mappers):
    soil_range = get_range(mappers.seed_to_soil, seed_range)
    fertilizer_range = get_range(mappers.soil_to_fertilizer, soil_range)
    water_range = get_range(mappers.fertilizer_to_water, fertilizer_range)
    light_range = get_range(mappers.water_to_light, water_range)
    temperature_range = get_range(mappers.light_to_temperature, light_range)
    humidity_range = get_range(mappers.temperature_to_humidity, temperature_range)
    location_range = get_range(mappers.humidity_to_location, humidity_range)
    return location_range.start


def process(lines):
    seeds_ranges = get_seeds(lines[0])
    mappers = to_mapper(lines)
    all_seeds_min_locations = []
    for seeds_range in seeds_ranges:
        min_location = calculate_min_location(seeds_range, mappers)
        all_seeds_min_locations.append(min_location)
    return min(all_seeds_min_locations)


print(process(lines))
