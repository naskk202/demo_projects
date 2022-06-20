dungeon = input().split("|")
health = 100
coins = 0
complete = True
for floor in dungeon:
    room = floor.split()
    command = room[0]
    points = int(room[1])
    if command == "potion":
        if health + points <= 100:
            health += points
            print(f"You healed for {points} hp.\n"
                  f"Current health: {health} hp.")
        else:
            print(f"You healed for {100 - health} hp.\n"
                  f"Current health: 100 hp.")
            health = 100
    elif command == "chest":
        coins += points
        print(f"You found {points} bitcoins.")
    else:
        health -= points
        if health <= 0:
            print(f"You died! Killed by {command}.\n"
                  f"Best room: {dungeon.index(floor) + 1}")
            complete = False
            break
        else:
            print(f"You slayed {command}.")

if complete:
    print(f"You've made it!\n"
          f"Bitcoins: {coins}\n"
          f"Health: {health}")