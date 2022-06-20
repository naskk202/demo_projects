num = int(input())
count = 0
password = ""
no_password = True
for a in range(1, 10):
    for b in range(1, 10):
        for c in range(1, 10):
            for d in range(1, 10):
                if (a * b) + (c * d) == num:
                    if a < b and c > d:
                        count += 1
                        if count == 4:
                            no_password = False
                            password = str(f'{a}{b}{c}{d}')
                        print(f"{a}{b}{c}{d}", end=" ")
print()
if no_password:
    print("No!")
else:
    print(f"Password: {password}")