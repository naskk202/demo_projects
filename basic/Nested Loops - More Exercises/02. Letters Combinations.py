start = input()
final = input()
parasite = input()
count = 0
for a in range(ord(start), ord(final) + 1):
    if a == ord(parasite):
        continue
    for b in range(ord(start), ord(final) + 1):
        if b == ord(parasite):
            continue
        for c in range(ord(start), ord(final) + 1):
            if c == ord(parasite):
                continue
            else:
                count += 1
                print(f"{chr(a)}{chr(b)}{chr(c)}", end = " ")
print(count)