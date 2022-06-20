emp_one = int(input())
emp_two = int(input())
emp_three = int(input())
people = int(input())

hour = 0
people_per_h = emp_one + emp_two + emp_three

while people > 0:
    people -= people_per_h
    hour += 1
    if hour % 4 == 0:
        hour += 1
print(f"Time needed: {hour}h.")