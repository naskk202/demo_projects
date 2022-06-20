# a = [
#     [1, 2, 3, 2, 4],
#     [2, 3, 4, 5, 5],
#     [3, 4, 5, 6, 7],
#     [4, 5, 6, 7, 8],
#     [5, 6, 7, 8, 9]
# ]
#
#
# #
# # n = 5
# # print([a[i][i] for i in range(n)])
# # print([a[i][n - i - 1] for i in range(n)])
#
#
# # for i in range(-2, 2):
# #         print(i)
#
#
# def in_range(matrix, counter):
#     new_positions = []
#     for pair in counter:
#         row, col = pair
#         if row - 1 >= 0:
#             new_positions.append([row - 1, col])
#         if row + 1 < len(matrix):
#             new_positions.append([row + 1, col])
#         if col - 1 >= 0:
#             new_positions.append([row, col - 1])
#         if col + 1 < len(matrix[0]):
#             new_positions.append([row, col + 1])
#     return new_positions
#
#
# counter = []
# for r in range(len(a)):
#     for c in range(len(a[r])):
#         if a[r][c] == 2:
#             counter.append([r, c])
# print(counter)
#
# counter.extend(in_range(a, counter))
# print(sorted(counter))
# print("-----------------------")
# for r, c in counter:
#     a[r][c] = "2"
#
# for i in range(len(a)):
#     print(a[i])


# def if_won(move, cur_row, cur_col, matrix):
#     won = False
#     matrix[cur_row][cur_col] = "_"
#     if move == "U":
#         if 0 > cur_row - 1:
#             won = True
#         else:
#             cur_row -= 1
#             matrix[cur_row][cur_col] = "P"
#     elif move == "D":
#         if len(matrix) == cur_row + 1:
#             won = True
#         else:
#             cur_row += 1
#             matrix[cur_row][cur_col] = "P"
#     elif move == "L":
#         if 0 > cur_col - 1:
#             won = True
#         else:
#             cur_col -= 1
#             matrix[cur_row][cur_col] = "P"
#     elif move == "R":
#         if len(matrix[0]) == cur_col + 1:
#             won = True
#         else:
#             cur_col += 1
#             matrix[cur_row][cur_col] = "P"
#     return won, cur_row, cur_col
#
#
# def cur_player_position(matrix):
#     for r in range(len(matrix)):
#         if "P" in matrix[r]:
#             return r, matrix[r].index("P")
#
#
# def bunny_position(matrix):
#     bunny_pos = []
#     for r in range(len(matrix)):
#         for c in range(len(matrix[r])):
#             if matrix[r][c] == "B":
#                 bunny_pos.append([r, c])
#     return bunny_pos
#
#
# def bunny_spread(bunny_indexes, matrix):
#     new_positions = []
#     for pair in bunny_indexes:
#         row, col = pair
#         if row - 1 >= 0:
#             new_positions.append([row - 1, col])
#         if row + 1 < len(matrix):
#             new_positions.append([row + 1, col])
#         if col - 1 >= 0:
#             new_positions.append([row, col - 1])
#         if col + 1 < len(matrix[0]):
#             new_positions.append([row, col + 1])
#     return new_positions
#
#
# # rows, cols = [int(i) for i in input().split()]
# matrix = [
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "P", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "B", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ],
#     ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", ]
# ]
#
# # for i in range(rows):
# #     matrix.append([i for i in input()])
# rows = len(matrix)
# # moves = [i for i in input()]
#
# cur_row, cur_col = cur_player_position(matrix)
# bunny_indexes = bunny_position(matrix)
# won = False
# step_on_bunny = False
#
# for i in range(rows):
#     print("".join(matrix[i]))
#
# while not won:
#
#     move = input()
#     won, cur_row, cur_col = if_won(move, cur_row, cur_col, matrix)
#     bunny_indexes = bunny_spread(bunny_indexes, matrix)
#     for r, c in bunny_indexes:
#         matrix[r][c] = "B"
#     if matrix[cur_row][cur_col] == "B" or won:
#         break
#     for i in range(rows):
#         print("".join(matrix[i]))
#     print()
#     print("------------------------")
#     print()
#
#
#
# if won:
#     print(f"won: {cur_row} {cur_col}")
# else:
#     print(f"dead: {cur_row} {cur_col}")


# a = [0, 4, 3, 6]
# b = ["a", "b", "c", "d"]
#
# print(max(a))
# print(b[a.index(max(a))])


# a, b, c = 0, 0, 5
# ways = {
#     "up": lambda r, c, n: (r - n, c),
#     "down": lambda r, c, n: (r + n, c),
#     "left": lambda r, c, n: (r, c - n),
#     "right": lambda r, c, n: (r, c + n),
# }
#
# a, b = ways["up"](a, b, c)
# print(a)
# print(b)

# from math import floor
# a = 27
# b = 3
#
# print(a // b)
# print(floor(a / b))
#
# the_tuple = {"are", "be", "malak"}
# items = ["edno", "dve", "tri"]
# are = [1, 2, 3]
# for el in are:
#     items.append(el)
#
# print(items)


# from collections import deque
#
#
# def special_case(num):
#     return num % 25 == 0
#
#
#
# male = [int(i) for i in input().split() if int(i) > 0]
# female = deque(int(i) for i in input().split() if int(i) > 0)
# matches = 0
# spec_case = False
#
# while male and female:
#     cur_male = male.pop()
#     cur_female = female.popleft()
#     while cur_male <= 0:
#         if male:
#             cur_male = male.pop()
#         else:
#             break
#     while cur_female <= 0:
#         if female:
#             cur_female = female.popleft()
#         else:
#             break
#
#     while special_case(cur_male):
#         if len(male) > 1:
#             male.pop()
#             cur_male = male.pop()
#         else:
#             male = []
#             spec_case = True
#             cur_male = 1
#     while special_case(cur_female):
#         if len(female) > 1:
#             female.popleft()
#             cur_female = female.popleft()
#         else:
#             female = []
#             spec_case = True
#             cur_female = 1
#     if spec_case:
#         break
#     if cur_male == cur_female:
#         matches += 1
#     else:
#         male.append(cur_male - 2)
#
# print(f"Matches: {matches}")
# print(f"Males left: {', '.join(reversed([str(i) for i in male])) if male else 'none'}")
# print(f"Females left: {', '.join(str(i) for i in female) if female else 'none'}")


# a = "Diamond Jewellery"
# b = "Gold"
#
# b = ["Gemstone", "Porcelain Sculpture"]
# c = ["Gold", "Diamond Jewellery"]
#
# combinations = {
#     "first_combo": ["Gemsone", "Porcelain Sculpture"],
#     "second_combo": ["Gold", "Diamond Jewellery"]
# }
# print(combinations)
# for el in combinations.values():
#     if a in el:
#         el.remove(a)
#         print(el)
# print(combinations)
# for el in combinations.values():
#     if b in el:
#         el.remove(b)
#         print(el)


a = 1

while a < 5:
    print(a)
    a += 1