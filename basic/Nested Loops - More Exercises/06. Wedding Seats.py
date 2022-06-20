sector = input()
row = int(input())
seat = int(input())
all = 0
for sectors in range(65, ord(sector) +1):
    for rows in range(1, row + (sectors - 64)):
        if rows % 2 == 0:
            for seats in range(97, (97 + seat + 2)):
                all += 1
                print(f"{chr(sectors)}{rows}{chr(seats)}")
        elif rows % 2 != 0:
            for seats in range(97, (97 + seat)):
                all += 1
                print(f"{chr(sectors)}{rows}{chr(seats)}")
print(all)