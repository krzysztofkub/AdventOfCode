import queue

from Day10.second import process_pipeline_tile, Tile, get_pipeline_tiles, set_normal_vector_based_on_bend_pipe_and_return_two_possible_ground_tiles
from input_reader import read_file

lines = read_file("test.txt")
lines = [line.strip() for line in lines]

class bcolors:
    OKGREEN = '\033[92m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'


def assert_process_pipline_tile(pipeline_tile, traversed_from_tile, expected_queue):
    q = queue.Queue()
    pipeline_tiles = get_pipeline_tiles(lines)
    process_pipeline_tile(pipeline_tile, traversed_from_tile, q, [], lines, pipeline_tiles)
    test_result = list(q.queue) == expected_queue
    color = bcolors.OKGREEN if test_result else bcolors.FAIL
    print(f'Test pass: {color}{test_result}{bcolors.ENDC}')


print("Pipeline tile process:")
assert_process_pipline_tile(Tile("-", 3, 1), Tile(".", 3, 0), [Tile("-", 3, 1, (0, -1))])  # 1. z kropki do lini prostej
assert_process_pipline_tile(Tile("-", 4, 1), Tile("-", 3, 1, (0, -1)),
                            [Tile(".", 4, 0)])  # 2. z lini prostej do lini prostej


def assert_set_normal_vector_based_on_bend_pipe(pipline_tile, traversed_from_tile, expected_normal_vector):
    set_normal_vector_based_on_bend_pipe_and_return_two_possible_ground_tiles(pipline_tile, traversed_from_tile)
    test_result = expected_normal_vector == pipline_tile.normal_vector
    color = bcolors.OKGREEN if test_result else bcolors.FAIL
    print(f'Test pass: {color}{test_result}{bcolors.ENDC}')


print()
print("Normal vector calculations:")
assert_set_normal_vector_based_on_bend_pipe(Tile("F", 2, 2), Tile("-", 3, 2, (0, -1)), (-1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("F", 2, 2), Tile("-", 3, 2, (0, 1)), (1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("F", 2, 2), Tile("|", 2, 3, (-1, 0)), (0, -1))
assert_set_normal_vector_based_on_bend_pipe(Tile("F", 2, 2), Tile("|", 2, 3, (1, 0)), (0, 1))
assert_set_normal_vector_based_on_bend_pipe(Tile("7", 2, 2), Tile("|", 2, 3, (1, 0)), (0, -1))
assert_set_normal_vector_based_on_bend_pipe(Tile("7", 2, 2), Tile("|", 2, 3, (-1, 0)), (0, 1))
assert_set_normal_vector_based_on_bend_pipe(Tile("7", 2, 2), Tile("-", 3, 2, (0, -1)), (1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("7", 2, 2), Tile("-", 3, 2, (0, 1)), (-1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("J", 2, 2), Tile("-", 3, 2, (0, -1)), (-1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("J", 2, 2), Tile("-", 3, 2, (0, 1)), (1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("J", 2, 2), Tile("|", 2, 3, (1, 0)), (0, 1))
assert_set_normal_vector_based_on_bend_pipe(Tile("J", 2, 2), Tile("|", 2, 3, (-1, 0)), (0, -1))
assert_set_normal_vector_based_on_bend_pipe(Tile("L", 2, 2), Tile("-", 3, 2, (0, -1)), (1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("L", 2, 2), Tile("-", 3, 2, (0, 1)), (-1, 0))
assert_set_normal_vector_based_on_bend_pipe(Tile("L", 2, 2), Tile("|", 2, 3, (1, 0)), (0, -1))
assert_set_normal_vector_based_on_bend_pipe(Tile("L", 2, 2), Tile("|", 2, 3, (-1, 0)), (0, 1))



def override_file():
    result_file = "result.txt"

    with open(result_file, 'r', encoding='utf-8') as file:
        result_lines = file.readlines()

    result = []
    for line in result_lines:
        line = line.replace("7", "\u2510").replace("L", "\u2514").replace("J", "\u2518").replace("F", "\u250C")
        result.append(line)

    with open(result_file, 'w', encoding='utf-8') as file:
        file.writelines("".join(result))

override_file()