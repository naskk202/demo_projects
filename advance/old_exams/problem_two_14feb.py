import sys
from io import StringIO

input1 = """5
1 X 7 9 11
X 14 46 62 0
15 33 21 95 X
P 14 3 4 18
9 20 33 X 0
right
right
up
up
left
down
"""

input2 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
up
left
"""

input3 = """8
13 18 9 7 24 41 52 11
54 21 19 X 6 4 75 6
76 5 7 1 76 27 2 37
92 3 25 37 52 X 56 72
15 X 1 45 45 X 7 63
1 63 P 2 X 43 5 1
48 19 35 20 100 27 42 80
73 88 78 33 37 52 X 22
asfddsf
left
left
up
left
left
left
left
"""

sys.stdin = StringIO(input3)


def is_in_range(size, row, col):
    return 0 <= row < size and 0 <= col < size


def position_check(matrix, row, col):
    result = -1
    if is_in_range(len(matrix), row, col):
        if not matrix[row][col] == "X":
            result = int(matrix[row][col])
    return result, row, col


size = int(input())
matrix = []
player_row, player_col = 0, 0

for i in range(size):
    matrix.append([i for i in input().split()])
    if "P" in matrix[i]:
        player_row, player_col = i, matrix[i].index("P")

coins = 0
collected_index = []

while coins < 100:
    result = 0
    command = input()
    if command == "up":
        result, player_row, player_col = position_check(matrix, player_row - 1, player_col)
    elif command == "down":
        result, player_row, player_col = position_check(matrix, player_row + 1, player_col)
    elif command == "left":
        result, player_row, player_col = position_check(matrix, player_row, player_col - 1)
    elif command == "right":
        result, player_row, player_col = position_check(matrix, player_row, player_col + 1)
    else:
        continue
    if result == -1:
        if not coins == 0:
            coins //= 2
        break
    else:
        coins += result
        collected_index.append([player_row, player_col])

if coins < 100:
    print(f"Game over! You've collected {coins} coins.")
else:
    print(f"You won! You've collected {coins} coins.")

print("Your path:")
for el in collected_index:
    print(el)
