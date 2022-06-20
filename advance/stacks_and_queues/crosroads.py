from collections import deque


green_duration = int(input())
free_window = int(input())
time = green_duration + free_window
cars = deque()
cars_enter = input()
all_cars_pass = True
cars_pass = 0
while not cars_enter == "END":
    while not cars_enter == "green":
        cars.append(cars_enter)
        cars_enter = input()
    while cars:
        car = cars[0]
        if time < len(car):
            print("A crash happened!")
            print(f"{car} was hit at {car[time]}.")
            all_cars_pass = False
            exit()
        else:
            time -= len(car)
            cars_pass += 1
            cars.popleft()
            if not cars:
                break
        if time <= free_window:
            break
    time = free_window + green_duration
    cars_enter = input()

if all_cars_pass:
    print("Everyone is safe.")
    print(f"{cars_pass} total cars passed the crossroads.")