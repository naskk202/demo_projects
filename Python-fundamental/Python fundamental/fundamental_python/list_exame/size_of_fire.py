fire = input().split("#")
water = int(input())
effor = 0
no_fire = 0
print("Cells:")
for cell in fire:
    cell = cell.split(" = ")
    if cell[0] == "Low" and 0 < int(cell[1]) <= 50 or cell[0] == "Medium" and 50 < int(cell[1]) <= 80 or cell[0] == "High" and 80 < int(cell[1]) <= 125:
        if water >= int(cell[1]):
           water -= int(cell[1])
           effor += int(cell[1]) * 0.25
           no_fire += int(cell[1])
           print(f" - {cell[1]}")
        else:
            continue
    else:
        continue
print(f"Effort: {effor:.2f}")
print(f"Total Fire: {no_fire}")