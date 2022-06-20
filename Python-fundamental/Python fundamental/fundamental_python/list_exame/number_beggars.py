amount = [int(x) for x in input().split(", ")]
beggars = int(input())
lis = [0] * beggars
counter = 0
bigger = False
for beggar in range(len(amount)):
    counter = beggar
    while beggar >= beggars:
        beggar = beggar - beggars
        bigger = True
    if bigger:
        lis[beggar] += amount[counter]
    else:
        lis[beggar] += amount[beggar]
print(lis)


# coins = [int(num) for num in input().split(", ")]
# beggars = int(input())
# count = 0
# beggars_list = [0] * beggars
# for coin in coins:
#     beggars_list[count] += coin
#     count += 1
#     if count >= beggars:
#         count = 0
# print(beggars_list)
# !!!daibaa!!!