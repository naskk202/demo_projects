number = input()
simp = 0
comp = 0
while number != "stop":
    number = int(number)
    if number < 0:
        number = 0
        print("\nNumber is negative.")
    elif number < 4:
        simp += number
    elif number % 2 == 0 or number % 3 == 0:
        comp += number
    else:
        simp += number
    number = input()
print(f"Sum of all prime numbers is: {simp}\n"
      f"Sum of all non prime numbers is: {comp}")