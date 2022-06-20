def in_inventory(inventory: list, item):
    if item in inventory:
        return True
    return False

inventory = input().split(", ")
command = input()
while not command == "Craft!":
    job = command.split(" - ")
    if job[0] == "Collect":
        if not in_inventory(inventory, job[1]):
            inventory.append(job[1])
    elif job[0] == "Drop":
        if in_inventory(inventory, job[1]):
            inventory.remove(job[1])
    elif job[0] == "Combine Items":
        old_item = job[1].split(":")[0]
        new_items = job[1].split(":")[1]
        if in_inventory(inventory, old_item):
            inventory.insert(inventory.index(old_item) + 1, new_items)
    elif job[0] == "Renew":
        if in_inventory(inventory, job[1]):
            popped_item = inventory.pop(inventory.index(job[1]))
            inventory.append(popped_item)
    command = input()
print(", ".join(inventory))