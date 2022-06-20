# centers = int(input())
# visitors = 0
# chairs = 0
# room_chair = 0
# room_visitors = 0
# less_rooms = []
# for room in range(1, centers + 1):
#     info = input()
#     for i in info:
#         if i == "X":
#             room_chair += 1
#         if i == info[-1]:
#             room_visitors += int(info[-1])
#     if room_visitors > room_chair:
#         less_rooms.extend([(room_visitors - room_chair), room])
#     visitors += room_visitors
#     chairs += room_chair
#     room_visitors = 0
#     room_chair = 0
# if less_rooms:
#     for i in range(0, len(less_rooms), 2):
#         print(f"{less_rooms[i]} more chairs needed in room {less_rooms[i + 1]}")
# else:
#     print(f"Game On, {chairs - visitors} free chairs left")


centers = int(input())
less_rooms = []
all_visitors = 0
all_chairs = 0
for room in range(centers):
    info = input().split()
    chairs = info[0].count("X")
    people = int(info[1])
    if people > chairs:
        less_rooms.extend([(people - chairs), room + 1])
    all_visitors += people
    all_chairs += chairs
if less_rooms:
    for i in range(0, len(less_rooms), 2):
        print(f"{less_rooms[i]} more chairs needed in room {less_rooms[i + 1]}")
else:
    print(f"Game On, {all_chairs - all_visitors} free chairs left")
