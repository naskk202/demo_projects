a = input()
b = input()
for i in range(len(a)):
    a = [x for x in a]
    b = [x for x in b]
    if a[i] != b[i]:
        a[i] = b[i]
        print("".join(a))
