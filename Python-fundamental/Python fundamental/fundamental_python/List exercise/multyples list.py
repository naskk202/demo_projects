counter = int(input())
length = int(input())
lis = []
i = 1
while len(lis) < length:
    if i % counter == 0:
        lis.append(i)
    i += 1
print(lis)