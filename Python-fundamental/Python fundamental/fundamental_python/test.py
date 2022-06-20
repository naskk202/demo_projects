# def game(step):
#     first = step.count("1")
#     second = step.count("2")
#     if first > second:
#         return "one"
#     elif second > first:
#         return "two"
#     else:
#         return
#
#
# first_player = 0
# second_player = 0
# games = 3
# while not games == 0:
#     steps = input().split()
#     turn = game(steps)
#     if turn == "one":
#         first_player += 1
#     elif turn == "two":
#         second_player += 1
#     games -= 1
# if first_player > second_player:
#     print("First player won")
# elif second_player > first_player:
#     print("Second player won")
# else:
#     print("Draw!")



# games = 3
# first_player = 0
# second_player = 0
# while games > 0:
#     turns = input().split()
#     for turn in turns:
#         if turn == "1":
#             first_player += 1
#         elif turn == "2":
#             second_player += 1
#     games -= 1
# if first_player > second_player:
#     print("First player won")
# elif second_player > first_player:
#     print("Second player won")
# else:
#     print("Draw!")
# def game_winner(game):
#     if game.count(1) > game.count(2):
#         return "one"
#     elif game.count(1) < game.count(2):
#         return "two"


game = 3
results = []
while game > 0:
    one = input().split()
    results.extend(one)
    game -= 1
first_game = [int(results[i]) for i in range(0, len(results), 3)]
second_game = [int(results[i]) for i in range(1, len(results), 3)]
third_game = [int(results[i]) for i in range(2, len(results), 3)]
# winners = game_winner(first_game)
a = 5
b = 6



if  > second:
    print("First player won")
elif first < second:
    print("Second player won")
else:
    print("Draw!")