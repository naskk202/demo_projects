def valid_index_range(range, index):
    if 0 <= index < len(range):
        return True
    return False


def shoot(range, index, power):
    if valid_index_range(range, index):
        range[index] -= power
        if range[index] <= 0:
            range.pop(index)
            return range
    return range


def add(range, index, add):
    if valid_index_range(range, index):
        range.insert(index, add)
        return range
    print("Invalid placement!")
    return range


def strike(the_range, index, radius):
    if valid_index_range(the_range, index + radius):
        if valid_index_range(the_range, index - radius):
            for i in range(radius + radius + 1):
                the_range.pop(index - radius)
            return the_range
    print("Strike missed!")
    return the_range


targets = [int(i) for i in input().split()]
command = input()
while not command == "End":
    command = command.split()
    if command[0] == "Shoot":
        targets = shoot(targets, int(command[1]), int(command[2]))
    elif command[0] == "Add":
        targets = add(targets, int(command[1]), int(command[2]))
    elif command[0] == "Strike":
        targets = strike(targets, int(command[1]), int(command[2]))
    command = input()
targets = [str(i) for i in targets]
print("|".join(targets))
