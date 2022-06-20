start = int(input())
final = int(input())
for a in range(start, final + 1):
    for b in range(start, final + 1):
        for c in range(start, final + 1):
            for d in range(start, final + 1):
                if (b + c) % 2 == 0 and a > d:
                    if a % 2 == 0 and d % 2 != 0 or a % 2 != 0 and d % 2 == 0:
                        print(f"{a}{b}{c}{d}", end=" ")
                    else:
                        continue