vacation = input()
sum = 0
vacations = ''
while vacation != "End":
    budget = float(input())
    while sum < budget:
        save = float(input())
        sum += save
        if sum >= budget:
            vacations += f"Going to {vacation}!\n"
    vacation = input()
    sum = 0
print(vacations)
