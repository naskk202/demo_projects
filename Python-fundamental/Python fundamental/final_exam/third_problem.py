command = input()
zoo_areas = {}
zoo_animals = {}

while not command == "EndDay":
    order = command.split(": ")
    animal_info = order[1].split("-")
    animal = animal_info[0]
    if "Add" in order:
        needed_food = int(animal_info[1])
        area = animal_info[2]
        if area not in zoo_areas:
            zoo_areas[area] = []
        if animal not in zoo_animals:
            zoo_animals[animal] = 0
            zoo_areas[area].append(animal)
        zoo_animals[animal] += needed_food
    elif "Feed" in order:
        food = int(animal_info[1])
        if animal in zoo_animals:
            zoo_animals[animal] -= food
            if zoo_animals[animal] <= 0:
                print(f"{animal} was successfully fed")
                for i in zoo_areas.values():
                    if animal in i:
                        i.remove(animal)
                zoo_animals.pop(animal)
    command = input()

print("Animals:")

zoo_animals = sorted(zoo_animals.items(), key=lambda x: (-x[1], x[0]))
for k, v in zoo_animals:
    print(f" {k} -> {v}g")
print("Areas with hungry animals:")

sorted_areas = sorted(zoo_areas.items(), key=lambda x: (-len(x[1]), x[0]))
for k, v in sorted_areas:
    if not len(v) == 0:
        print(f" {k}: {len(v)}")



