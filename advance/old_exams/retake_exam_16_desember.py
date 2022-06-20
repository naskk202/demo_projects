# 1.

# input1 = """4 5 7 3 6 9 12
# 12 9 6 1
# """
#
# input2 = """3 0 3 6 9 0 12
# 12 9 6 1 2 3 15 13 4
# """
#
# input3 = """3 0 -12 4 7 9 6 18 90 4
# 7 14 2 3 9 5 0 -13 -26 4 0 27
# """
#
# input4 = """3 25
# 25 3
# """
#
# sys.stdin = StringIO(input1)
#
# from collections import deque
#
#
# male = [int(i) for i in input().split() if int(i) > 0]
# female = deque([int(i) for i in input().split() if int(i) > 0])
# matches = 0
# spec_case = False
#
# while male and female:
#     cur_male = male[-1]
#     cur_female = female[0]
#
#     while cur_male <= 0:
#         male.pop()
#         if male:
#             cur_male = male[-1]
#         else:
#             break
#     while cur_female <= 0:
#         female.popleft()
#         if female:
#             cur_female = female[0]
#         else:
#             break
#
#     while cur_male % 25 == 0:
#         if len(male) > 2:
#             male = male[:-2]
#             cur_male = male[-1]
#         else:
#             male = []
#             spec_case = True
#             cur_male = 1
#
#     while cur_female % 25 == 0:
#         if len(female) > 2:
#             female = female[2:]
#             cur_female = male[0]
#         else:
#             female = []
#             spec_case = True
#             cur_female = 1
#     if spec_case:
#         break
#     if cur_male == cur_female:
#         male.pop()
#         female.popleft()
#         matches += 1
#     else:
#         male[-1] -= 2
#         female.popleft()
#
# print(f"Matches: {matches}")
# print(f"Males left: {', '.join(reversed([str(i) for i in male])) if male else 'none'}")
# print(f"Females left: {', '.join(str(i) for i in female) if female else 'none'}")


# 3.


def is_in_range(size, r, c):
    return 0 <= r < size and 0 <= c < size - 1


def index_checker(matrix, row, col):
    cur_sum = 0
    if is_in_range(len(matrix), row, col - 1):
        cur_sum += matrix[row][col - 1]
    if is_in_range(len(matrix), row, col):
        cur_sum += matrix[row][col]
    return cur_sum


def get_magic_triangle(num):
    triangle = [[1], [1, 1]]

    while len(triangle) < num:
        triangle.append([])
        for i in range(len(triangle)):
            cur_row = len(triangle) - 1
            cur_col = i
            triangle[cur_row].append(index_checker(triangle, cur_row - 1, cur_col))
    for el in range(len(triangle)):
        print(f'{" " * (len(triangle[-el]) if el != 0 else len(triangle) + 1)}{triangle[el]}')

get_magic_triangle(20)
