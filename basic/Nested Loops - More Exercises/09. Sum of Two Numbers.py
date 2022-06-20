first = int(input())
second = int(input())
magick = int(input())
combination = 0
counter = True
for a in range(first, second + 1):
    for b in range(first, second + 1):
        combination += 1
        if a + b == magick:
            print(f"Combination N:{combination} ({a} + {b} = {magick})")
            counter = False
            exit()
if counter:
    print(f"{combination} combinations - neither equals {magick}")