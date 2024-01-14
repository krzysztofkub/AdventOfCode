def read_file_lines(filename):
    with open(filename, 'r') as file:
        return file.readlines()


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()
