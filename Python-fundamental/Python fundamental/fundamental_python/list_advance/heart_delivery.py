neighborhood = [int(i) for i in input().split("@")]
command = input()
position = 0

while not command == "Love!":
    jump = int(command.split()[1])
    position += jump
    if position >= len(neighborhood):
        position = 0
    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {position}.")
failed_houses = 0
for i in neighborhood:
    if not i == 0:
        failed_houses += 1
if failed_houses == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {failed_houses} places.")




neighborhood = [int(i) for i in input().split("@")]
command = input()
position = 0

while not command == "Love!":
    length_jump = int(command.split()[1])
    position += length_jump
    if position >= len(neighborhood):
        position = 0
    if neighborhood[position] == 0:
        print(f"Place {position} already had Valentine's day.")
    else:
        neighborhood[position] -= 2
        if neighborhood[position] == 0:
            print(f"Place {position} has Valentine's day.")
    command = input()

print(f"Cupid's last position was {position}.")
counter = 0
for num in neighborhood:
    if not num == 0:
        counter += 1
if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
