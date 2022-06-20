budget = float(input())
kg_flour = float(input())
cozonac = kg_flour + kg_flour * 0.75 + (kg_flour * 1.25) / 4
cozonacs = budget // cozonac
money_left = budget - (cozonac * cozonacs)
eggs = 0
for egg in range(1, int(cozonacs) + 1):
    eggs += 3
    if egg % 3 == 0:
        eggs -= egg -2
print(f"You made {int(cozonacs)} cozonacs! Now you have {eggs} eggs and {money_left:.2f}BGN left.")
