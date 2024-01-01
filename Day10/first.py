from dataclasses import dataclass

from input_reader import read_file


@dataclass
class TraverseVector:
    x_vector: int
    y_vector: int


@dataclass
class Tile:
    value: str
    x: int
    y: int

    def __eq__(self, other):
        if isinstance(other, Tile):
            return self.x == other.x and self.y == other.y
        return False


lines = read_file("input.txt")
traverse_vectors = {
    "|": [(0, 1), (0, -1)],
    "-": [(-1, 0), (1, 0)],
    "L": [(0, -1), (1, 0)],
    "J": [(0, -1), (-1, 0)],
    "7": [(0, 1), (-1, 0)],
    "F": [(0, 1), (1, 0)],
    "S": []
}
max_char_index = 0
max_line_index = 0


def find_start(lines):
    for row_index, line in enumerate(lines):
        for char_index, char in enumerate(line):
            if char == 'S':
                return Tile(char, char_index, row_index)


def get_tile(x, y, lines):
    return Tile(lines[y][x], x, y)


def get_adjacent_pipe_tiles(tile, lines):
    adjacent_tiles = []
    if tile.x > 0:
        adjacent_tiles.append(get_tile(tile.x - 1, tile.y, lines))
    if tile.x < max_char_index:
        adjacent_tiles.append(get_tile(tile.x + 1, tile.y, lines))
    if tile.y > 0:
        adjacent_tiles.append(get_tile(tile.x, tile.y - 1, lines))
    if tile.y < max_line_index:
        adjacent_tiles.append(get_tile(tile.x, tile.y + 1, lines))
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


def process(lines):
    lines = [line.strip() for line in lines]
    tile = find_start(lines)
    tile_history = []
    set_max_lengths(lines)

    while tile is not None:
        tile = traverse(tile, lines, tile_history)
        tile_history.append(tile)
        print(tile)

    number_of_pipes = len(tile_history)
    return number_of_pipes / 2


print(process(lines))
