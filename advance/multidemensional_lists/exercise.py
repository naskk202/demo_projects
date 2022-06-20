# input1 = """3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# """
#
# sys.stdin = StringIO(input1)
#
# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     matrix.append([i for i in input().split(", ")])
#
# primary_diagonal = [matrix[i][i] for i in range(rows)]
# secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]
#
# print(f"Primary diagonal: {', '.join(primary_diagonal)}. Sum: {sum(int(i) for i in primary_diagonal)}")
# print(f"Secondary diagonal: {', '.join(secondary_diagonal)}. Sum: {sum(int(i) for i in secondary_diagonal)}")
#

# 2. Diagonal_diff

# input1 = """3
# 11 2 4
# 4 5 6
# 10 8 -12
# """
#
# sys.stdin = StringIO(input1)
#
# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(i) for i in input().split()])
#
# primary_diagonal = [matrix[i][i] for i in range(rows)]
# secondary_diagonal = [matrix[i][rows - i - 1] for i in range(rows)]
#
# print(abs(sum(primary_diagonal) - sum(secondary_diagonal)))


# 3. 2x2
# import sys
# from io import StringIO
#
# input1 = """5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# """
#
# sys.stdin = StringIO(input1)
#
# rows, cols = [int(i) for i in input().split()]
# matrix = []
# secondary_matrix_count = 0
#
# for _ in range(rows):
#     matrix.append([i for i in input().split()])
#
# for r in range(rows - 1):
#     for c in range(cols - 1):
#         if matrix[r][c] == matrix[r][c + 1] == matrix[r + 1][c] == matrix[r + 1][c + 1]:
#             secondary_matrix_count += 1
# print(secondary_matrix_count)


# 4. maximal_sum
# import sys
# from io import StringIO
#
# input1 = """4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# """
#
# sys.stdin = StringIO(input1)
#
# rows, cols = [int(i) for i in input().split()]
# matrix = []
# max_sum = 0
# cur_r = 0
# cur_c = 0
#
# for i in range(rows):
#     matrix.append([int(i) for i in input().split()])
#
# for r in range(rows - 2):
#     for c in range(cols - 2):
#         current_sum = matrix[r][c] + matrix[r][c + 1] + matrix[r][c + 2] + matrix[r + 1][c] + matrix[r + 1][c + 1] + \
#                       matrix[r + 1][c + 2] + matrix[r + 2][c] + matrix[r + 2][c + 1] + matrix[r + 2][c + 2]
#         if current_sum > max_sum:
#             max_sum, cur_r, cur_c = current_sum, r, c
#
# print(f"Sum = {max_sum}")
# print(matrix[cur_r][cur_c], matrix[cur_r][cur_c + 1], matrix[cur_r][cur_c + 2])
# print(matrix[cur_r + 1][cur_c], matrix[cur_r + 1][cur_c + 1], matrix[cur_r + 1][cur_c + 2])
# print(matrix[cur_r + 2][cur_c], matrix[cur_r + 2][cur_c + 1], matrix[cur_r + 2][cur_c + 2])


# 5. Matrix_of_palindrome

# rows, cols = [int(i) for i in input().split()]
#
# for r in range(rows):
#     for c in range(cols):
#         print(f"{chr(97 + r)}{chr(97 + c + r)}{chr(97 + r)}", end = " ")
#     print()


# 6. matrix_shuff

# import sys
# from io import StringIO
#
# input1 = """4 3
# 1 2 3
# 4 5 6
# 2 3 6
# 8 7 3
# swap 0 0 1 4
# swap 10 9 8 7
# swap 0 1 1 0
# swra 0 2 3 2
# swap 1 0 7 9
# end
# END
# """
#
# sys.stdin = StringIO(input1)
#
#
# def is_valid_index(r, c, rows, cols):
#     if 0 <= r < rows and 0 <= c < cols:
#         return True
#     return False
#
#
# rows, cols = [int(i) for i in input().split()]
# matrix = []
#
# for _ in range(rows):
#     matrix.append([i for i in input().split()])
# while True:
#     command = input()
#     if command == "END":
#         break
#
#     command = command.split()
#
#     if not command[0] == "swap" and not len(command) == 5:
#         print("Invalid input!")
#         continue
#
#     row1, col1, row2, col2 = [int(i) for i in command[1:]]
#
#     if is_valid_index(row1, col1, rows, cols) and is_valid_index(row2, col2, rows, cols):
#         matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
#         for r in range(rows):
#             print(f"{' '.join(matrix[r])}")
#     else:
#         print("Invalid input!")


# 7. snake_moves
# import sys
# from io import StringIO
#
# input1 = """"5 6
# SoftUni
# """
#
# sys.stdin = StringIO(input1)

# rows, cols = [int(i) for i in input().split()]
# string = input()
# matrix = []
# index = 0
# while len(string) < rows*cols:
#     string += string
# for r in range(rows):
#     matrix.append([])
#     for c in range(cols):
#         matrix[r].append(string[c + index])
#     index += cols
#
# for i in range(1, rows + 1):
#     if i % 2 == 0:
#         print("".join(reversed(matrix[i - 1])))
#     else:
#         print("".join(matrix[i - 1]))
#


# rows, cols = [int(i) for i in input().split()]
# string = input()
# matrix = []
# index = 0
#
# for r in range(rows):
#     matrix.append([None] * cols)
#     for c in range(cols):
#         if r % 2 == 0:
#             matrix[r][c] = string[index]
#         else:
#             matrix[r][cols - c - 1] = string[index]
#         index = (index + 1) % len(string)
#
# for i in range(rows):
#     print("".join(matrix[i]))


# 8. bombs

# import sys
# from io import StringIO
#
# input1 = """4
# 8 3 2 5
# 6 4 7 9
# 9 9 3 6
# 6 8 1 2
# 1,2 2,1 2,0
# """
#
# sys.stdin = StringIO(input1)
#
#
# def bombard(power, row, col, matrix):
#     for r in range(-1, 2):
#         if 0 <= row + r < len(matrix):
#             for c in range(-1, 2):
#                 if 0 <= c + col < len(matrix[0]):
#                     if matrix[row + r][col + c] > 0:
#                         matrix[row + r][col + c] -= power
#     matrix[row][col] = 0
#     return matrix
#
#
# rows = int(input())
# matrix = []
# alive_cells = 0
# sum_cells = 0
# for _ in range(rows):
#     matrix.append([int(i) for i in input().split()])
# coordinates = input().split()
#
# for i in range(len(coordinates)):
#     row, col = [int(i) for i in coordinates[i].split(",")]
#     power = matrix[row][col]
#     if power > 0:
#         matrix = bombard(power, row, col, matrix)
#
# for i in range(rows):
#     for el in matrix[i]:
#         if el > 0:
#             alive_cells += 1
#             sum_cells += el
# print(f"Alive cells: {alive_cells}")
# print(f"Sum: {sum_cells}")
# for q in range(rows):
#     print(" ".join([str(i) for i in matrix[q]]))


# 9. miner

# import sys
# from io import StringIO
#
# input1 = """5
# up right right up right
# * * * c *
# * * * e *
# * * c * *
# s * * c *
# * * c * *
# """
#
# input2 = """4
# left left up right right right down
# * * * e
# * * c *
# * s * c
# * * * *
# """
#
# input3 = """6
# down right up left left down down down
# * * * * * *
# e * * * c *
# * * c s * *
# * * * * * *
# c * * * c *
# * * c * * *
# """
#
# input4 = """4
# left left upp right right right down
# * * * e
# * * c *
# * s * c
# * * * *
# """
#
# sys.stdin = StringIO(input2)
#
#
# def find_starter_index(rows, matrix):
#     start_row, start_col = 0, 0
#     coal = 0
#     for i in range(rows):
#         if "s" in matrix[i]:
#             start_row, start_col = i, matrix[i].index("s")
#         coal += matrix[i].count("c")
#     return start_row, start_col, coal
#
#
# def collector(start_row, start_col, matrix):
#     if matrix[start_row][start_col] == "*":
#         return 0
#     if matrix[start_row][start_col] == "e":
#         print(f"Game over! ({start_row}, {start_col})")
#         exit()
#     if matrix[start_row][start_col] == "c":
#         matrix[start_row][start_col] = "*"
#         return 1
#     if matrix[start_row][start_col] == "s":
#         return 0
#
#
# rows = int(input())
# commands = input().split()
# matrix = []
# collected = 0
# all_coal = 0
# all_collected = False
#
# for _ in range(rows):
#     matrix.append(input().split())
#
# start_row, start_col, all_coal = find_starter_index(rows, matrix)
#
# for command in commands:
#     if command == "up":
#         if 0 <= start_row - 1:
#             start_row -= 1
#             collected += (collector(start_row, start_col, matrix))
#     elif command == "down":
#         if rows - 1 >= start_row + 1:
#             start_row += 1
#             collected += (collector(start_row, start_col, matrix))
#     elif command == "left":
#         if 0 <= start_col - 1:
#             start_col -= 1
#             collected += (collector(start_row, start_col, matrix))
#     elif command == "right":
#         if rows - 1 >= start_col + 1:
#             start_col += 1
#             collected += (collector(start_row, start_col, matrix))
#     if collected == all_coal:
#         all_collected = True
#         print(f"You collected all coal! ({start_row}, {start_col})")
#         exit()
#
#
# if not all_collected:
#     print(f"{all_coal - collected} pieces of coal left. ({start_row}, {start_col})")


# 10. radioactive_mutate_vampire

import sys
from io import StringIO

input1 = """5 6
.....P
......
...B..
......
......
ULDDDR
"""

input2 = """4 5
.....
.....
.B...
...P.
LLLLLLLL
"""

input3 = """5 8
.......B
...B....
....B..B
........
..P.....
ULLL
"""

sys.stdin = StringIO(input3)


def if_won(move, cur_row, cur_col, matrix):
    won = False
    matrix[cur_row][cur_col] = "."
    if move == "U":
        if 0 > cur_row - 1:
            won = True
        else:
            cur_row -= 1
    elif move == "D":
        if len(matrix) == cur_row + 1:
            won = True
        else:
            cur_row += 1
    elif move == "L":
        if 0 > cur_col - 1:
            won = True
        else:
            cur_col -= 1
    elif move == "R":
        if len(matrix[0]) == cur_col + 1:
            won = True
        else:
            cur_col += 1
    return won, cur_row, cur_col


def cur_player_position(matrix):
    for r in range(len(matrix)):
        if "P" in matrix[r]:
            return r, matrix[r].index("P")


def bunny_position(matrix):
    bunny_pos = []
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == "B":
                bunny_pos.append([r, c])
    return bunny_pos


def bunny_spread(bunny_indexes, matrix):
    new_positions = []
    for pair in bunny_indexes:
        row, col = pair
        if row - 1 >= 0:
            new_positions.append([row - 1, col])
        if row + 1 < len(matrix):
            new_positions.append([row + 1, col])
        if col - 1 >= 0:
            new_positions.append([row, col - 1])
        if col + 1 < len(matrix[0]):
            new_positions.append([row, col + 1])
    return new_positions


rows, cols = [int(i) for i in input().split()]
matrix = []

for i in range(rows):
    matrix.append([i for i in input()])

moves = [i for i in input()]

cur_row, cur_col = cur_player_position(matrix)
bunny_indexes = bunny_position(matrix)
won = False
step_on_bunny = False

for move in moves:
    won, cur_row, cur_col = if_won(move, cur_row, cur_col, matrix)
    bunny_indexes = bunny_spread(bunny_indexes, matrix)
    for r, c in bunny_indexes:
        matrix[r][c] = "B"
    if matrix[cur_row][cur_col] == "B" or won:
        break

for i in range(rows):
    print("".join(matrix[i]))

if won:
    print(f"won: {cur_row} {cur_col}")
else:
    print(f"dead: {cur_row} {cur_col}")


