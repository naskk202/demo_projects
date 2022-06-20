type = input()
count = int(input())
budget = float(input())
price = 0
if type == "Roses":
    if count > 80:
        price = 5 * 0.9
    else:
        price = 5
elif type == 'Dahlias':
    if count > 90:
        price = 3.8 * 0.85
    else:
        price = 3.8
elif type == "Tulips":
    if count > 80:
        price = 2.8 * 0.85
    else:
        price = 2.8
elif type == "Narcissus":
    if count < 120:
        price = 3 * 1.15
    else:
        price = 3
elif type == "Gladiolus":
    if count < 80:
        price = 2.5 * 1.2
    else:
        price = 2.5
sum = price * count
if budget >= sum:
    print(f"Hey, you have a great garden with {count} {type} and {budget - sum:.2f} leva left.")
else:
    print(f"Not enough money, you need {sum - budget:.2f} leva more.")