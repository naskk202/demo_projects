from math import ceil
students = int(input())
lectures = int(input())
bonus = int(input())
attendances = []
for i in range(students):
    attendances.append(int(input()))
if attendances:
    chosen_one = max(attendances)
else:
    chosen_one = 0
bonuses = []
for st in attendances:
     bonuses.append(int((ceil(chosen_one / lectures * (5 + bonus)))))
if bonuses:
    bbb = max(bonuses)
else:
    bbb = 0
print(f"Max Bonus: {bbb}.")
print(f"The student has attended {chosen_one} lectures.")