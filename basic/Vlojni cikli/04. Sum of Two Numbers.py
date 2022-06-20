start = int(input())
end = int(input())
magick = int(input())
combos = 0
cant = True
for a in range(start, end + 1):
    for b in range(start, end + 1):
        combos += 1
        if a + b == magick:
            cant = False
            print(f"Combination N:{combos} ({a} + {b} = {magick})")
            break
    if not cant:
        break
if cant:
    print(f"{combos} combinations - neither equals {magick}")