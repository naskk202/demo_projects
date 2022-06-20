from collections import deque

petrol_station = deque()
gas = 0
index = 0
start_index = 0
circles = 0

circle = int(input())
for i in range(circle):
    petrol_station.append(input().split())


while True:
    gas_fill = int(petrol_station[index][0])
    distance = int(petrol_station[index][1])
    gas += gas_fill
    if gas < distance:
        a = petrol_station.popleft()
        petrol_station.append(a)
        start_index += 1
        gas = 0
        circles = 0
        index = 0
    else:
        index += 1
        circles += 1
        gas -= distance
    if circles == circle:
        break
print(start_index)