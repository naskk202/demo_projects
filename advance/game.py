def player_turn():
    pass


def player_move():
    pass


def win_check():
    pass


def create_board(rows, cols):
    matrix = []

    for _ in range(rows):
        matrix.append([0] * cols)

    return matrix


def valid_input(inp, line):
    while not inp.isdigit():
        inp = input(f"Matrix {line}:")
    if not 4 < int(inp) < 16:
        valid_input(inp, line)
    return inp


def input_size():
    rows = input("Matrix rolls:")
    cols = input("Matrix columns:")
    valid_input(rows, "rolls")
    valid_input(cols, "columns")

    return int(rows), int(cols)


rows, cols = input_size()

bord = create_board(rows, cols)

for el in bord:
    print(el)
