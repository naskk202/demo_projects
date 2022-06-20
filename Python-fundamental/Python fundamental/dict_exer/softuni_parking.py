num_cars = int(input())
parking = {}
for i in range(num_cars):
    car = input().split()
    command = car[0]
    key = car[1]
    if command == "register":
        value = car[2]
        if key not in parking:
            parking[key] = value
            print(f"{key} registered {value} successfully")
        else:
            print(f"ERROR: already registered with plate number {value}")
    if command == "unregister":
        if key not in parking:
            print(f"ERROR: user {key} not found")
        else:
            print(f"{key} unregistered successfully")
            parking.pop(key)

for k, v in parking.items():
    print(f"{k} => {v}")