energy = int(input())
distance = input()
won_battle = 0
win = True

while not distance == "End of battle":
    distance = int(distance)
    energy -= distance
    if energy >= 0:
        won_battle += 1
        if won_battle % 3 == 0:
            energy += won_battle
    else:
        print(f"Not enough energy! Game ends with {won_battle} won battles and {energy + distance} energy")
        win = False
        break
    distance = input()

if win:
    print(f"Won battles: {won_battle}. Energy left: {energy}")