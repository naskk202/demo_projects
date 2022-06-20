# 1. sum_matrix_elements

# row, col = [int(i) for i in input().split(", ")]
# matrix = []
# total = 0
#
# for i in range(row):
#     matrix.append([int(i) for i in input().split(", ")])
#     total += sum(matrix[i])
#
# print(total)
# print(matrix)

# ------------------------------------------

# rows, cols = [int(i) for i in input().split(", ")]
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(i) for i in input().split()])
#
# for col in range(cols):
#     col_sum = 0
#     for row in range(rows):
#         col_sum += matrix[row][col]
#     print(col_sum)

# ------------------------------------------

# 2. even_matrix_

# rows = int(input())
# matrix = []
#
# for i in range(rows):
#     matrix.append([int(num) for num in input().split(", ") if int(num) % 2 == 0])
#
# print(matrix)

# 5. primary_diagonal

# num = int(input())
# matrix = []
# total = 0
#
# for i in range(num):
#     matrix.append([int(i) for i in input().split()])
#     total += matrix[i][i]
# print(total)

# 6. symbol_in_matrix

# num = int(input())
# matrix = []
#
# for i in range(num):
#     matrix.append([el for el in input()])
#
# special_el = input()
# found = False
#
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if matrix[i][j] == special_el:
#             found = True
#             print(f"({i}, {j})")
#             exit()
#
# if not found:
#     print(f"{special_el} does not occur in the matrix")

# 7. square_with_maximum_sum

rows, cols = [int(i) for i in input().split(", ")]
matrix = []
small_matrix = []
sum_el = 0
matrix_for_printing = []

for i in range(rows):
    matrix.append([int(i) for i in input().split(", ")])

out_of_index = False
row_index = 0
column_index = 0
while not out_of_index:

    for i in range(row_index, row_index + 2):
        for j in range(column_index, column_index + 2):
            small_matrix.append(matrix[i][j])
    if sum(small_matrix) > sum_el:
        sum_el = sum(small_matrix)
        matrix_for_printing.append([i for i in small_matrix])
    small_matrix.clear()
    column_index += 1
    if column_index > cols - 2:
        row_index += 1
        column_index = 0
        if row_index == rows - 1:
            out_of_index = True
for i in range(0, 3, 2):
    print(f"{matrix_for_printing[-1][i]}", end=" ")
    print(matrix_for_printing[-1][i + 1])
print(sum_el)
