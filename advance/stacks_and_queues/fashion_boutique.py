clothes = input().split()
capacity = int(input())
racks = 0
times_fill = 0

while clothes:
    cloth = int(clothes.pop())
    racks += cloth
    if racks > capacity:
        racks = cloth
        times_fill += 1
if racks == 0:
    print(times_fill)
else:
    print(times_fill + 1)
