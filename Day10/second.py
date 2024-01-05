from dataclasses import dataclass
from input_reader import read_file
import queue
import threading


@dataclass
class TraverseVector:
    x_vector: int
    y_vector: int


@dataclass
class Tile:
    value: str
    x: int
    y: int
    normal_vector: (int, int) = None

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        return False


lines = read_file("test.txt")
traverse_vectors = {
    "|": [(0, 1), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": []
}
straight_pipes = ["|", "-"]
max_char_index = 0
max_line_index = 0


def find_start(lines):
    for row_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == 'S':
                return Tile(char, char_index, row_index)


def get_tile(x, y, lines):
    return Tile(lines[y][x], x, y)


def get_adjacent_tiles(tile, lines):
    adjacent_tiles = []
    if tile.x > 0:
        adjacent_tiles.append(get_tile(tile.x - 1, tile.y, lines))
    if tile.x < max_char_index:
        adjacent_tiles.append(get_tile(tile.x + 1, tile.y, lines))
    if tile.y > 0:
        adjacent_tiles.append(get_tile(tile.x, tile.y - 1, lines))
    if tile.y < max_line_index:
        adjacent_tiles.append(get_tile(tile.x, tile.y + 1, lines))
    return adjacent_tiles


def get_adjacent_pipe_tiles(tile, lines):
    adjacent_tiles = get_adjacent_tiles(tile, lines)
    return [tile for tile in adjacent_tiles if tile.value in traverse_vectors.keys()]


def is_legal_flow(destination_pipe, from_tile):
    to_vector = (destination_pipe.x - from_tile.x, destination_pipe.y - from_tile.y)
    from_vector = (from_tile.x - destination_pipe.x, from_tile.y - destination_pipe.y)
    return ((from_tile.value == 'S' or to_vector in traverse_vectors[from_tile.value])
            and from_vector in traverse_vectors[destination_pipe.value])


def traverse(from_tile, lines, tile_history):
    pipe_tiles = get_adjacent_pipe_tiles(from_tile, lines)
    legal_pipes = [destination_pipe for destination_pipe in pipe_tiles if
                   destination_pipe not in tile_history and is_legal_flow(destination_pipe, from_tile)]
    return legal_pipes[0] if legal_pipes else None


def set_max_lengths(lines):
    global max_char_index, max_line_index
    max_line_index = len(lines) - 1
    max_char_index = len(lines[0].strip()) - 1


def get_rim_tiles(lines):
    rim_tiles = []
    for line_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if (line_index == 0 or
                    line_index == len(lines) - 1 or
                    char_index == 0 or
                    char_index == len(line) - 1):
                rim_tiles.append(Tile(char, char_index, line_index))
    return rim_tiles


def find_first_outside_tile(tiles, lines):
    rim_tiles = get_rim_tiles(lines)
    return [rim_tile for rim_tile in rim_tiles if rim_tiles not in tiles][0]


def add_to_queue(tile, processed_nodes, q):
    if tile not in processed_nodes or tile not in list(q.queue):
        q.put(tile)


def worker(q, pipeline_tiles, lines):
    counter = 0
    processed_nodes = []
    while True:
        node = q.get()
        if node is None:
            closed_tiles = len(lines[0]) * len(lines) - len(pipeline_tiles) - counter
            print(f'Closed tiles number: {closed_tiles}')
            break
        counter = process_node(node, q, pipeline_tiles, lines, processed_nodes, counter)
        processed_nodes.append(node)
        q.task_done()


def process_pipeline_tile(pipeline_tile, traversed_from_tile, q, processed_nodes, lines, pipeline_tiles):
    if pipeline_tile.value in straight_pipes:
        if traversed_from_tile not in pipeline_tiles:
            pipeline_tile.normal_vector = (
                traversed_from_tile.x - pipeline_tile.x, traversed_from_tile.y - pipeline_tile.y)
            for vector in traverse_vectors[pipeline_tile.value]:
                new_pipeline_tile = get_tile(pipeline_tile.x + vector[0], pipeline_tile.y + vector[1], lines)
                new_pipeline_tile.normal_vector = pipeline_tile.normal_vector
                add_to_queue(new_pipeline_tile, processed_nodes, q)

        elif traversed_from_tile.value in straight_pipes:
            pipeline_tile.normal_vector = traversed_from_tile.normal_vector
            tile_from_normal_vector = get_tile(pipeline_tile.x + pipeline_tile.normal_vector[0],
                                               pipeline_tile.y + pipeline_tile.normal_vector[1], lines)
            add_to_queue(tile_from_normal_vector, processed_nodes, q)


        # else:
        # 1. calculate normal vector from 90 degree turn
        # tile_from_normal_vector = get_tile(pipeline_tile.x + pipeline_tile.normal_vector[0],
        #                                    pipeline_tile.y + pipeline_tile.normal_vector[1], lines)
        # add_to_queue(tile_from_normal_vector, processed_nodes, q)


def set_normal_vector_for_pipeline_tile(new_pipeline_tile, pipeline_tile):
    if new_pipeline_tile.value in straight_pipes:
    else:
        pass
        # pass vector from straight pipeline to 90degrees one


def process_node(node, q, pipeline_tiles, lines, processed_nodes, counter):
    counter += 1

    adjacent_tiles = get_adjacent_tiles(node, lines)
    for adjacent_tile in adjacent_tiles:
        if adjacent_tile not in pipeline_tiles:
            add_to_queue(adjacent_tile, processed_nodes, q)
        else:
            process_pipeline_tile(adjacent_tile, node, q, processed_nodes, lines, pipeline_tiles)

    if q.qsize() == 0:
        q.put(None)
    return counter


def count_points_inside_polygon(pipeline_tiles, lines):
    first_outside_node = find_first_outside_tile(pipeline_tiles, lines)
    q = queue.Queue()
    q.put(first_outside_node)

    thread = threading.Thread(target=worker, args=(q, pipeline_tiles, lines))
    thread.start()
    thread.join()

    return 0


def process(lines):
    lines = [line.strip() for line in lines]
    pipeline_tiles = get_pipeline_tiles(lines)
    return count_points_inside_polygon(pipeline_tiles, lines)


def get_pipeline_tiles(lines):
    tile = find_start(lines)
    tile_history = [tile]
    set_max_lengths(lines)
    while tile is not None:
        tile = traverse(tile, lines, tile_history)
        if tile is not None:
            tile_history.append(tile)
    return tile_history

# print(process(lines))
