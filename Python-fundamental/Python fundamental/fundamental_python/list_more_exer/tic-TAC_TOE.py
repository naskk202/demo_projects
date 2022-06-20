def game_winner(game):
    diagonal_left = []
    diagonal_right = []
    left_side = []
    right_side = []
    mid_side = []
    for i in range(len(game)):
        if len(set(game[i])) == 1:
            return game[i]
        left_side.append(game[i][0])
        right_side.append(game[i][2])
        diagonal_left.append(game[i][i])
        diagonal_right.append(game[-i - 1][i])
        mid_side.append(game[i][1])
    if len(set(diagonal_left)) == 1:
        return diagonal_left
    if len(set(diagonal_right)) == 1:
        return diagonal_right
    if len(set(left_side)) == 1:
        return left_side
    if len(set(right_side)) == 1:
        return right_side
    if len(set(mid_side)) == 1:
        return mid_side
    return "Draw!"


game = 3
results = []
while game > 0:
    one = input().split()
    results.append(one)
    game -= 1
winner = game_winner(results)
if "1" in winner:
    print("First player won")
elif "2" in winner:
    print("Second player won")
else:
    print("Draw!")
