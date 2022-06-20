units = int(input())
dozens = int(input())
hundreds = int(input())
for a in range(2, units + 1):
    if a % 2 != 0:
        continue
    for b in range(2, dozens + 1):
        if b == 4 or b == 6 or b > 7:
            continue
        for c in range(2, hundreds + 1):
            if c % 2 !=0:
                continue
            print(f"{a} {b} {c}")