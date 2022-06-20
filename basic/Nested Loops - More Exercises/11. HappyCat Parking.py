days = int(input())
hours = int(input())
sum_per_day = 0
sum = 0
for a in range(1, days + 1):
    for b in range(1, hours + 1):
        if a % 2 ==0 and b % 2 !=0:
            sum_per_day += 2.5
        elif a % 2 != 0 and b % 2 == 0:
            sum_per_day += 1.25
        else:
            sum_per_day += 1
    print(f"Day: {a} - {sum_per_day:.2f} leva")
    sum += sum_per_day
    sum_per_day = 0
print(f"Total: {sum:.2f} leva")