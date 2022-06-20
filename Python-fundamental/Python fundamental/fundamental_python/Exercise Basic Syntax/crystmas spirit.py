quantity = int(input())
days = int(input())
budget = 0
spirit = 0
for i in range(2, days + 1):
    if i % 11 == 0:
        quantity += 2
    if i % 2 == 0:
        budget += 2 * quantity
        spirit += 5
    if i % 3 == 0:
        budget += 8 * quantity
        spirit += 13
    if i % 5 == 0:
        budget += 15 * quantity
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        spirit -= 20
        budget += 23
if days % 10 ==0:
    spirit -= 30
print(f"Total cost: {budget}\n"
      f"Total spirit: {spirit} ")