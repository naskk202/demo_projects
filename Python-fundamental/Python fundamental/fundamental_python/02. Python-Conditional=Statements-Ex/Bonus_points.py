points = int(input())
bonus = 0
if points < 101:
    bonus += 5
elif points >1000:
    bonus += points * 0.1
else:
    bonus += points * 0.2
if points % 2 == 0:
    bonus += 1
else:
    bonus += 0
if points % 10 == 5:
    bonus += 2
else:
    bonus += 0
print(bonus)
print(points + bonus)