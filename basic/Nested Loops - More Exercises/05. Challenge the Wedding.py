man = int(input())
woman = int(input())
tables = int(input())
count = 0
for b in range(1, man + 1):
    for c in range(1, woman +1):
        count += 1
        if count <= tables:
            print(f"({b} <-> {c})", end = " ")
        else:
            break