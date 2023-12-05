from dataclasses import dataclass


@dataclass
class SeedRange:
    start: int
    seed_range: int

@dataclass
class Mapper:
    source_start: int
    destination_start: int
    mapping_range: int

    def get_destination(self, input):
        if input in range(self.source_start, self.mapping_range + self.source_start):
            return self.destination_start + input - self.source_start
        return None


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
