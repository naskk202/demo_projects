fire_cell = [input()].split("#")
water = int(input())
valid = False
total_fire = 0
print("Cells:")
for fire in fire_cell:
    fire = fire.split()
    if fire[0] == "Low" and 0 < int(fire[2]) <= 50:
        valid = True
    elif fire[0] == "Medium" and 50 < int(fire[2]) <= 80:
        valid = True
    elif fire[0] == "High" and 80 < int(fire[2]) <= 125:
        valid = True
    if valid:
        if int(fire[2]) <= water:
            water -= int(fire[2])
            print(f" - {int(fire[2])}")
            total_fire += int(fire[2])
    valid = False
print(f"Effort: {total_fire * 0.25:.2f}\n"
      f"Total Fire: {total_fire}")