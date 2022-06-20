cards = input().split(" ")
team_a = []
team_b = []
game_was_stop = False
if cards == ['']:
    print("Team A -11; Team B - 11")
    exit()
else:
    pass
for card in cards:
    if card[0] == "A":
        team_a.append(card)
    elif card[0] == "B":
        team_b.append(card)
    if len(set(team_a)) > 4 or len(set(team_b)) > 4:
        game_was_stop = True
        break
print(f"Team A - {11 - len(set(team_a))}; Team B - {11 - len(set(team_b))}")
if game_was_stop:
    print('Game was terminated')
# cards = input().split(" ")
# team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
# team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
# game_was_stop = False
# for card in cards:
#     if card in team_a:
#         team_a.remove(card)
#     elif card in team_b:
#         team_b.remove(card)
#     if len(team_a) < 7 or len(team_b) < 7:
#         game_was_stop = True
#         break
# print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
# if game_was_stop:
#     print("Game was terminated")