first = int(input())
second = int(input())
third = int(input())
students = int(input())
students_per_hour = first + second + third
hours = 0

while students > 0:
    students -= students_per_hour
    hours += 1
    if hours % 4 == 0:
        hours += 1

print(f"Time needed: {hours}h.")