sum = input().split(", ")
beggar = int(input())
lis = [0] * beggar
sepp = 0
for money in range(len(sum)):
    for i in range(len(lis)):
        if money == i + sepp:
            lis[i] += int(sum[money])
            if money == beggar + sepp - 1:
                sepp += beggar
                break
print(lis)
