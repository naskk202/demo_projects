a = input().split()
team_a = []
team_b = []
stop = False
for i in a:
    if len(set(team_a)) > 4 or len(set(team_b)) > 4:
        stop = True
        break
    if i[0] == "A":
        team_a.append(i)
    else:
        team_b.append(i)
print(f"Team A - {11 - len(set(team_a))}; Team B - {11 - len(set(team_b))}")
if stop:
    print("Game was terminated")