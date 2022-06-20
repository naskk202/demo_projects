events = input().split("|")
day =[]
energy = 100
coins = 0
force_closed = False
for i in events:
    day = i.split("-")
    if "rest" in day:
        if energy + int(day[1]) > 100:
            gained = (100 + int(day[1])) - (energy + int(day[1]))
            print(f"You gained {gained} energy.")
            energy = 100
        else:
            energy = energy + int(day[1])
            print(f"You gained {int(day[1])} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in day:
        energy -= 30
        if energy < 0:
            energy += 80
            print("You had to rest!")
            continue
        else:
            coins += int(day[1])
            print(f"You earned {int(day[1])} coins.")
    else:
        if coins >= 0:
            coins -= int(day[1])
            print(f"You bought {day[0]}.")
        else:
            print(f"Closed! Cannot afford {day[0]}.")
            force_closed = True
            break
if not force_closed:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")