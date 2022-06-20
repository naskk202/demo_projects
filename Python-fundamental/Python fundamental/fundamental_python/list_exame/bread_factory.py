events = input().split("|")
energy = 100
coins = 100
day_complete = True
for event in events:
    event = event.split("-")
    mani = event[0]
    value = int(event[1])
    if "rest" in event:
        if (energy + value) > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += value
            print(f"You gained {value} energy.")
        print(f"Current energy: {energy}.")
    elif "order" in event:
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if coins > value:
            print(f"You bought {mani}.")
            coins -= value
        else:
            print(f"Closed! Cannot afford {mani}.")
            day_complete = False
            break
if day_complete:
    print(f"Day completed!\n"
          f"Coins: {coins}\n"
          f"Energy: {energy}")