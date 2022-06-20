asd = input()
sum = 0
while asd != "NoMoreMoney":
    deposit = float(asd)
    if deposit <= 0:
        print("Invalid operation!")
        break
    else:
        sum += deposit
        print(f"Increase: {deposit:.2f}")
    asd = input()

print(f"Total: {sum:.2f}")