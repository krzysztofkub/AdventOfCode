import queue

from Day10.second import process_pipeline_tile, Tile, get_pipeline_tiles
from input_reader import read_file

lines = read_file("test.txt")
lines = [line.strip() for line in lines]


def assert_tile(pipeline_tile, traversed_from_tile, expected_queue):
    q = queue.Queue()
    pipeline_tiles = get_pipeline_tiles(lines)
    process_pipeline_tile(pipeline_tile, traversed_from_tile, q, [], lines, pipeline_tiles)
    test_result = list(q.queue) == expected_queue
    print(f'Test pass: {test_result}')


assert_tile(Tile("-", 3, 1), Tile(".", 3, 0), [Tile("-", 2, 1), Tile("-", 4, 1)])  # 1. z kropki do lini prostej
assert_tile(Tile("-", 4, 1), Tile("-", 3, 1, (0, -1)), [Tile(".", 4, 0)])  # 2. z lini prostej do lini prostej
