from io import StringIO
import sys
import time
import numpy as np
from scipy.signal import convolve2d
import copy

# input1 = """2
# Player 1
# Player 2
# 15
# 25
# 1
# A
# """
#
# sys.stdin = StringIO(input1)


class Counter:
    counter = -1

    def __init__(self, players):
        self.players = players
        self.cnt = self.get_cur_index()

    def get_cur_index(self):
        Counter.counter += 1
        if Counter.counter == self.players:
            Counter.counter = 0
        return


def names_and_board_input():
    players_count = players_count_validator()
    players = []
    for pl in range(players_count):
        player = input(f"Player {pl + 1} choose name: ")
        player_name_validator(player, players, pl + 1)
        players.append(player)

    row, col = set_board_size()
    board = set_board(row, col)

    start_game(board, players, row, col)


def players_count_validator():
    while True:
        players_count = input("Select players count from 2 to 4: ")
        if players_count.isdigit() and 1 < int(players_count) < 5:
            return int(players_count)


def player_name_validator(player, players, players_count):
    while player in players or player == "":
        player = input(f"Player {players_count} choose different name: ")
    return


def set_board_size():
    row = board_validator('row')
    col = board_validator('column')
    return row, col


def set_board(row, col):
    board = []
    for i in range(row):
        board.append([])
        for j in range(col):
            board[i].append("[ ]")
    return board


def board_validator(side_name):
    while True:
        size = input(f"Set board {side_name}'s count: ")
        if size.isdigit() and 8 < int(size) < 31:
            return int(size)


def print_board(board):
    row_chars = "     "
    for row_char in range(len(board[0])):
        row_chars += chr(65 + row_char) + "  "

    print(row_chars)

    for i in range(len(board)):
        if i < 9:
            print(f'{i + 1}   {"".join(board[i])}')
        else:
            print(f'{i + 1}  {"".join(board[i])}')

    print()


def which_player_turn(players):
    cls_ind = Counter(len(players))
    ind = cls_ind.counter
    signs = ["[X]", "[O]", "[▲]", "[⚫]"]
    cur_pl = players[ind]
    cur_sign = signs[ind]
    if ind == len(players) - 1:
        ind = 0
    ind += 1
    return cur_pl, cur_sign


def row_validator(limit):
    while True:
        loc = input(f"Choose row coordinates(number from 1 to {limit}): ")
        if loc.isdigit() and 0 <= int(loc) - 1 < limit:
            return int(loc) - 1


def col_validator(limit):
    while True:
        loc = input(f"Choose column coordinates(capital letter from A to {chr(limit + 64)}): ")
        loc_num = ord(loc) - 65
        if len(loc) == 1 and loc.isalpha() and 0 <= loc_num < limit:
            return loc_num


def player_move(r, c):
    row = row_validator(r)
    col = col_validator(c)
    return row, col


def check_if_win(board, sign):
    original_board = copy.deepcopy(board)
    new_board = convert_players_moves(board, sign)
    board_2d = np.transpose(new_board)

    vertical = np.array([[1, 1, 1, 1]])
    horizontal = np.transpose(vertical)
    diagonal_1 = np.eye(4, dtype=np.uint)
    diagonal_2 = np.fliplr(diagonal_1)

    all_directions = [vertical, horizontal, diagonal_1, diagonal_2]
    result = winning_move(board_2d, all_directions)

    return result, original_board


def winning_move(board_2d, detection):
    for kernel in detection:
        if (convolve2d(board_2d, kernel, mode="valid") == 4).any():
            return True
    return False


def convert_players_moves(board, sign):
    board_to_return = board
    for row in range(len(board)):
        for el in range(len(board[row])):
            if board[row][el] == sign:
                board_to_return[row][el] = 1
            else:
                board_to_return[row][el] = 0
    return board_to_return


def print_game_winner(cur_player):
    print("""                                                                     
            88                                                       
            ""              ,d                                       
                            88                                       
8b       d8 88  ,adPPYba, MM88MMM ,adPPYba,  8b,dPPYba, 8b       d8  
`8b     d8' 88 a8"     ""   88   a8"     "8a 88P'   "Y8 `8b     d8'  
 `8b   d8'  88 8b           88   8b       d8 88          `8b   d8'   
  `8b,d8'   88 "8a,   ,aa   88,  "8a,   ,a8" 88           `8b,d8'    
    "8"     88  `"Ybbd8"'   "Y888 `"YbbdP"'  88             Y88'     
                                                            d8'      
                                                           d8'""")
    print(f'YOU WON!!!\n'
          f'{cur_player}')


def start_game(board, players, row_limit, col_limit):
    cur_player, cur_sign = which_player_turn(players)
    print(f"\n{'-' * 7}{cur_player} it's your turn!!!{'-' * 7}\n")
    print_board(board)

    selected_row, selected_col = player_move(row_limit, col_limit)
    while True:
        if board[selected_row][selected_col] == "[ ]":
            break
        print("This spot is already taken!!!")
        selected_row, selected_col = player_move(row_limit, col_limit)
    board[selected_row][selected_col] = cur_sign
    result, original_board = check_if_win(board, cur_sign)
    if result:
        print(print_game_winner(cur_player))
        time.sleep(15)
        exit()

    board = original_board
    start_game(board, players, row_limit, col_limit)


names_and_board_input()
