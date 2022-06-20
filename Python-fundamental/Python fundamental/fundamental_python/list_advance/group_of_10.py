groups = list(map(lambda x: int(x), input().split(", ")))
test = []
for i in groups:
    group = 0
    left = 0
    while i > 10:
        group += 10
        i -= 10
    left = i
    test.append([group + 10, left + group])
for i in range(len(test)):
    # print(f"Group of {test[i][0]}'s: {[p for p in test if test[i][0] == 10]}")
print()
