import sys
from io import StringIO

# 1. flat_lines
# import sys
# from io import StringIO
#
# input1 = """1 2 3 ||  |  |||  | | ||  7  88"""
#
# sys.stdin = StringIO(input1)
#
# flat_list = [el for el in input().split("|")]
# for i in flat_list[::-1]:
#     if not i.split():
#         continue
#     print(" ".join(i.split()), end=" ")


# 2. matrix_modification
# import sys
# from io import StringIO
#
# input1 = """3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# """
#
# input2 = """4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# """
#
# sys.stdin = StringIO(input2)
#
#
# def is_in_range(row, col, matrix):
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         return True
#     return False
#
#
# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(i) for i in input().split()])
#
# while True:
#     command = input()
#     if command == "END":
#         break
#     sign = command.split()[0]
#     row, col, count = [int(i) for i in command.split()[1:]]
#     if sign == "Add" and is_in_range(row, col, matrix):
#         matrix[row][col] += count
#     elif sign == "Subtract" and is_in_range(row, col, matrix):
#         matrix[row][col] -= count
#     else:
#         print("Invalid coordinates")
#
# for el in range(rows):
#     print(" ".join(str(i) for i in matrix[el]))


# 3. knight_game
# import sys
# from io import StringIO
#
# input1 = """5
# 0K0K0
# K000K
# 00K00
# K000K
# 0K0K0
# """
#
# input2 = """8
# 0K0KKK00
# 0K00KKKK
# 00K0000K
# KKKKKK0K
# K0K0000K
# KK00000K
# 00K0K000
# 000K00KK
# """
#
# sys.stdin = StringIO(input2)
#
#
# def is_in_range(matrix, row, col):
#     if 0 <= row < len(matrix) and 0 <= col < len(matrix):
#         return matrix[row][col] == "K"
#
#
# def time_hit_horses(matrix, cur_row, cur_col):
#     times_hit = 0
#     if is_in_range(matrix, cur_row - 2, cur_col - 1):
#         times_hit += 1
#     if is_in_range(matrix, cur_row - 2, cur_col + 1):
#         times_hit += 1
#     if is_in_range(matrix, cur_row - 1, cur_col + 2):
#         times_hit += 1
#     if is_in_range(matrix, cur_row + 1, cur_col + 2):
#         times_hit += 1
#     if is_in_range(matrix, cur_row + 2, cur_col + 1):
#         times_hit += 1
#     if is_in_range(matrix, cur_row + 2, cur_col - 1):
#         times_hit += 1
#     if is_in_range(matrix, cur_row - 1, cur_col - 2):
#         times_hit += 1
#     if is_in_range(matrix, cur_row + 1, cur_col - 2):
#         times_hit += 1
#     return times_hit
#
#
# rows = int(input())
# matrix = []
# removed_horse = 0
# for _ in range(rows):
#     matrix.append(list(input()))
#
# while True:
#     knights_hit, cur_row, cur_col = 0, 0, 0
#     for r in range(rows):
#         for c in range(rows):
#             if matrix[r][c] == "0":
#                 continue
#             else:
#                 times_hit= time_hit_horses(matrix, r, c)
#                 if times_hit > knights_hit:
#                     knights_hit = times_hit
#                     cur_row = r
#                     cur_col = c
#     if knights_hit == 0:
#         break
#     matrix[cur_row][cur_col] = "0"
#     removed_horse += 1
#
# print(removed_horse)


# 4. easter_bunny

#
# input1 = """5
# 1 3 7 9 11
# X 5 4 X 63
# 7 3 21 95 1
# B 1 73 4 9
# 9 2 33 2 0
# """
#
# input2 = """8
# 4 18 9 7 24 41 52 11
# 54 21 19 X 6 34 75 57
# 76 67 7 44 76 27 56 37
# 92 35 25 37 52 34 56 72
# 35 X 1 45 4 X 37 63
# 105 X B 2 12 43 5 19
# 48 19 35 20 32 27 42 4
# 73 88 78 32 37 52 X 22
# """
#
# sys.stdin = StringIO(input1)

# the problem is that total sum doesn't stop summing when reach "X"
# def bunny_direction_sum(matrix, row, col):
#     total_sum = [0] * 4
#     direction = [[], [], [], []]
#     ways = ["up", "down", "left", "right"]
#     for i in range(1, len(matrix)):
#         if is_in_range(matrix, row - i, col):
#             total_sum[0] += int(matrix[row - i][col])
#             direction[0].append([row - 1, col])
#         if is_in_range(matrix, row + i, col):
#             total_sum[1] += int(matrix[row + i][col])
#             direction[1].append([row + i, col])
#         if is_in_range(matrix, row, col - i):
#             total_sum[2] += int(matrix[row][col - i])
#             direction[2].append([row, col - i])
#         if is_in_range(matrix, row, col + i):
#             total_sum[3] += int(matrix[row][col + i])
#             direction[3].append([row, col + i])
#     the_index = total_sum.index(max(total_sum))
#     return max(total_sum), direction[the_index], ways[the_index]
#
#
# rows = int(input())
# matrix = []
# bunny_row, bunny_col = 0, 0
#
# for i in range(rows):
#     matrix.append(input().split())
#     if "B" in matrix[i]:
#         bunny_row, bunny_col = i, matrix[i].index("B")
#
# total_sum, direction, way = bunny_direction_sum(matrix, bunny_row, bunny_col)
#
# print(way)
# for i in range(len(direction)):
#     print(direction[i])
# print(total_sum)


# def is_in_range(size, r, c):
#     return 0 <= r < size and 0 <= c < size
#
#
# rows = int(input())
# matrix = []
# bunny_row, bunny_col = 0, 0
#
# for i in range(rows):
#     matrix.append(input().split())
#     if "B" in matrix[i]:
#         bunny_row, bunny_col = i, matrix[i].index("B")
#
# ways = {
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
#     "left": lambda r, c: (r, c - 1),
#     "right": lambda r, c: (r, c + 1),
# }
#
# total_sum = float("-inf")
# coordinates = []
# direction = ""
#
#
# for direct, step in ways.items():
#     cur_sum = 0
#     cur_row, cur_col = bunny_row, bunny_col
#     cur_coordinates = []
#
#     while True:
#         cur_row, cur_col = step(cur_row, cur_col)
#         if not is_in_range(rows, cur_row, cur_col):
#             break
#         if matrix[cur_row][cur_col] == "X":
#             break
#         cur_sum += int(matrix[cur_row][cur_col])
#         cur_coordinates.append([cur_row, cur_col])
#     if total_sum < cur_sum:
#         total_sum = cur_sum
#         coordinates = cur_coordinates
#         direction = direct
# print(direction)
# for el in coordinates:
#     print(el)
# print(total_sum)


# 5. alice_in_wonderland

# input1 = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# right
# left
# down
# up
# left
# """
#
# input32 = """5
# . A . . 1
# R . 2 . .
# 4 7 . 1 .
# . . . 2 .
# . 3 . . .
# down
# up
# up
# right
# left
# down
# up
# left
# """
#
# input2 = """7
# . A . 1 1 . .
# 9 . . . 6 . 5
# . 6 . R . . .
# . 3 . . 1 . .
# . . . 2 . . 2
# . 3 . . 1 . .
# . 8 3 . . . 2
# left
# down
# down
# right
# """
#
# sys.stdin = StringIO(input32)
#
#
# def is_in_range(size, r, c):
#     return 0 <= r < size and 0 <= c < size
#
#
# size = int(input())
# matrix = []
# alice_row, alice_col = 0, 0
# for i in range(size):
#     matrix.append(input().split())
#     if "A" in matrix[i]:
#         alice_row, alice_col = i, matrix[i].index("A")
#
# tea_bags = 0
# row, col = alice_row, alice_col
# ways = {
#     "up": lambda r, c: (r - 1, c),
#     "down": lambda r, c: (r + 1, c),
#     "left": lambda r, c: (r, c - 1),
#     "right": lambda r, c: (r, c + 1),
# }
# in_game = True
# matrix[row][col] = "*"
# while in_game:
#     command = input()
#     row, col = ways[command](row, col)
#     if not is_in_range(size, row, col):
#         in_game = False
#         break
#     if matrix[row][col] == "R":
#         in_game = False
#     elif matrix[row][col].isdigit():
#         tea_bags += int(matrix[row][col])
#     matrix[row][col] = "*"
#     if tea_bags >= 10:
#         break
#
# if in_game:
#     print("She did it! She went to the party.")
# else:
#     print("Alice didn't make it to the tea party.")
# for el in matrix:
#     print(" ".join(el))


# 6. range_day7


input1 = """. . . . . 
x . . . . 
. A . . . 
. . . x . 
. x . . x 
3
shoot down
move right 4
move left 1
"""

input2 = """. . . . . 
. . . . . 
. A x . . 
. . . . . 
. x . . . 
2
shoot down
shoot right
"""

input3 = """. . . . . 
. . . . . 
. . x . . 
. . . . . 
. x . . A 
3
shoot down
move right 2
shoot left
"""

sys.stdin = StringIO(input2)


def is_in_range(r, c):
    return 0 <= r < 5 and 0 <= c < 5


matrix = []
start_row, start_col = 0, 0
targets_count = 0
shot_targets_coordinates = []

for i in range(5):
    matrix.append(input().split())
    targets_count += matrix[i].count("x")
    if "A" in matrix[i]:
        start_row, start_col = i, matrix[i].index("A")
all_targets = targets_count
ways = {
    "up": lambda r, c, n: (r - n, c),
    "down": lambda r, c, n: (r + n, c),
    "left": lambda r, c, n: (r, c - n),
    "right": lambda r, c, n: (r, c + n),
}
for i in range(int(input())):
    command = input().split()
    action = command[0]
    cur_row, cur_col = start_row, start_col
    if action == "shoot":
        for _ in range(5):
            cur_row, cur_col = ways[command[1]](cur_row, cur_col, 1)
            if is_in_range(cur_row, cur_col):
                if matrix[cur_row][cur_col] == "x":
                    shot_targets_coordinates.append([cur_row, cur_col])
                    targets_count -= 1
                    matrix[cur_row][cur_col] = "."
                    break
    if action == "move":
        steps = int(command[2])
        cur_row, cur_col = ways[command[1]](start_row, start_col, steps)
        if is_in_range(cur_row, cur_col):
            start_row, start_col = cur_row, cur_col
    if targets_count == 0:
        break

if targets_count:
    print(f"Training not completed! {targets_count} targets left.")
else:
    print(f"Training completed! All {all_targets} targets hit.")
for el in shot_targets_coordinates:
    print(el)