material = input()
my_dict = {}
while not material == "stop":
    quantity = int(input())
    if material not in my_dict:
        my_dict[material] = 0
    my_dict[material] += quantity
    material = input()
for k, v in my_dict.items():
    print(f"{k} -> {v}")
