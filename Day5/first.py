from Day5.classes import Mappers, Mapper
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
    return [int(seed.strip()) for seed in line.split("seeds: ")[1].split(" ")]


def get_number(type_mappers, input):
    for mapper in type_mappers:
        destination = mapper.get_destination(input)
        if destination is not None:
            return destination
    return input



def calculate_min_location(seed, mappers):
    print(f'seed {seed} ========')
    soil_number = get_number(mappers.seed_to_soil, seed)
    print(f'soil_number : {soil_number}')
    fertilizer_number = get_number(mappers.soil_to_fertilizer, soil_number)
    print(f'fertilizer_number : {fertilizer_number}')
    water_number = get_number(mappers.fertilizer_to_water, fertilizer_number)
    print(f'water_number : {water_number}')
    light_number = get_number(mappers.water_to_light, water_number)
    print(f'light_number : {light_number}')
    temperature_number = get_number(mappers.light_to_temperature, light_number)
    print(f'temperature_number : {temperature_number}')
    humidity_number = get_number(mappers.temperature_to_humidity, temperature_number)
    print(f'humidity_number : {humidity_number}')
    location_number = get_number(mappers.humidity_to_location, humidity_number)
    print(f'location_number : {location_number}')
    print()
    return location_number


def process(lines):
    seeds = get_seeds(lines[0])
    mappers = to_mapper(lines)
    all_seeds_min_locations = []
    for seed in seeds:
        min_location = calculate_min_location(seed, mappers)
        all_seeds_min_locations.append(min_location)
    return min(all_seeds_min_locations)



print(process(lines))
