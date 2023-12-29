from dataclasses import dataclass, field
from typing import List


@dataclass
class Number_Range:
    start: int
    end: int
    checked_against: List['Number_Range'] = field(default_factory=list)

    def __str__(self):
        return f"({self.start}, {self.end})"

    def get_ranges_without_mappers(self):
        sorted_ranges = sorted(self.checked_against, key=lambda r: r.start)

        missing_ranges = []
        current_start = self.start

        for range in sorted_ranges:
            # Check if there is a gap before the start of the current range
            if range.start > current_start:
                missing_ranges.append(Number_Range(current_start, range.start - 1))

            # Update the current start to the end of the current range, if it's within the main range
            current_start = max(current_start, range.end + 1)

        # Check for any remaining range after the last checked range
        if current_start <= self.end:
            missing_ranges.append(Number_Range(current_start, self.end))

        return missing_ranges


class Mapper:

    def __init__(self, source_start, destination_start, mapping_range):
        self.source_range = Number_Range(source_start, source_start + mapping_range - 1)
        self.vector = source_start - destination_start

    def get_destination(self, input):
        if self.source_range.start <= input <= self.source_range.end:
            return input - self.vector
        return None

    def get_common_range(self, range: Number_Range):
        if range.start > self.source_range.end or range.end < self.source_range.start:
            return None

        if range.start > self.source_range.start:
            tmp_common_start = range.start
        else:
            tmp_common_start = self.source_range.start

        if range.end > self.source_range.end:
            tmp_common_end = self.source_range.end
        else:
            tmp_common_end = range.end
        return Number_Range(tmp_common_start, tmp_common_end)

    def get_destination_range(self, range: Number_Range):
        range.checked_against.append(self.source_range)
        common_range = self.get_common_range(range)

        if common_range is None:
            return None

        destination_range = Number_Range(common_range.start - self.vector, common_range.end - self.vector)
        return destination_range


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
