floor = int(input())
rooms = int(input())
for floors in range(floor, 0, -1):
    for room in range(rooms):
        if floors == floor:
            print(f"L{floors * 10 + room}", end = " ")
        elif floors % 2 == 0:
            print(f"O{floors * 10 + room}", end = " ")
        else:
            print(f"A{floors * 10 + room}", end = " ")
    print()