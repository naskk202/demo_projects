floor = int(input())
rooms = int(input())
for floors in range(floor, 0, -1):
    for room in range(rooms):
        if floors == floor:
            print(f"L{floors}{room}", end = " ")
        elif floors % 2 == 0:
            print(f"O{floors}{room}", end = " ")
        else:
            print(f"A{floors}{room}", end = " ")
    print()