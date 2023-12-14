from dataclasses import dataclass


@dataclass
class Number_Range:
    start: int
    input_range: int


@dataclass
class Mapper:
    source_start: int
    destination_start: int
    mapping_range: int

    def get_destination(self, input):
        if input in range(self.source_start, self.mapping_range + self.source_start):
            return self.destination_start + input - self.source_start
        return None

    def get_common_range(self, range: Number_Range):
        source_end = self.source_start + self.mapping_range - 1
        range_end = range.start + range.input_range - 1

        if range.start > source_end or range_end < self.source_start:
            return None

        if range.start > self.source_start:
            tmp_common_start = range.start
        else:
            tmp_common_start = self.source_start

        if range_end > source_end:
            tmp_common_end = source_end
        else:
            tmp_common_end = range_end
        return Number_Range(tmp_common_start, tmp_common_end - tmp_common_start + 1)

    def get_destination_range(self, range: Number_Range):
        common_range = self.get_common_range(range)
        if common_range is None:
            return None
        vector = self.get_vector()
        return Number_Range(common_range.start - vector, common_range.input_range)

    def get_vector(self):
        return self.source_start - self.destination_start


@dataclass
class Mappers:
    seed_to_soil: [Mapper]
    soil_to_fertilizer: [Mapper]
    fertilizer_to_water: [Mapper]
    water_to_light: [Mapper]
    light_to_temperature: [Mapper]
    temperature_to_humidity: [Mapper]
    humidity_to_location: [Mapper]

    def __init__(self):
        pass

    @classmethod
    def set_value(cls, field_name: str, mappers: [Mapper]):
        setattr(cls, field_name, mappers)


def pretty_print(mapper, range_to_check):
    mapper_arr = [x for x in range(mapper.source_start, mapper.mapping_range + mapper.source_start)]
    print(f'{mapper_arr} -> destination_start: {mapper.destination_start}')

    range_to_check_arr = [x for x in range(range_to_check.start, range_to_check.input_range + range_to_check.start)]
    print(range_to_check_arr)
    print(mapper.get_destination_range(range_to_check))
    print()
    print("============================")


def test():
    pretty_print(Mapper(5, 3, 3), Number_Range(4, 2))
    pretty_print(Mapper(5, 3, 7), Number_Range(4, 4))
    pretty_print(Mapper(5, 8, 5), Number_Range(5, 5))
    pretty_print(Mapper(5, 8, 5), Number_Range(2, 2))


test()
