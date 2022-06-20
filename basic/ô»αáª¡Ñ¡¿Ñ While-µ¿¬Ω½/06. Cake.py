h = int(input())
w = int(input())
cake_size = h * w
eaten_cake = 0
pieces = input()
cake_was_enough = True
while pieces != "STOP":
    pieces = int(pieces)
    eaten_cake += pieces
    if eaten_cake >= cake_size:
        cake_was_enough = False
        print(f"No more cake left! You need {eaten_cake - cake_size} pieces more.")
        break
    else:
        pieces = input()
if cake_was_enough:
    print(f"{cake_size - eaten_cake} pieces are left.")