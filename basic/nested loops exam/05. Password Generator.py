n = int(input())
l = int(input())

for a in range(1, n + 1):
    for b in range(1, n + 1):
        for c in range(l):
            for d in range(l):
                for e in range(1, n + 1):
                    if a < e > b:
                        print(f"{a}{b}{chr(97 + c)}{chr(97 + d)}{e}", end = " ")
