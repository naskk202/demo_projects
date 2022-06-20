def in_rage(targets, index):
    if index < len(targets):
        if not targets[index] == -1:
            return True
    return False


targets = [int(i) for i in input().split()]
command = input()
shot_targets = 0
while not command == "End":
    command = int(command)
    if in_rage(targets, command):
        shot_targets += 1
        power = targets[command]
        targets[command] = -1
        for i in range(len(targets)):
            if not targets[i] == -1:
                if targets[i] <= power:
                    targets[i] += power
                else:
                    targets[i] -= power

    command = input()
print(f"Shot targets: {shot_targets} ->", end=" ")
print(*targets, sep = " ")
