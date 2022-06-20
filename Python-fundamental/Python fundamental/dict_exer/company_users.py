command = input()
my_dict = {}
while not command == "End":
    academy, student = command.split(" -> ")
    if academy not in my_dict:
        my_dict[academy] = []
    if student not in my_dict[academy]:
        my_dict[academy].append(student)
    command = input()
sorted_company = sorted(my_dict.items(), key=lambda x: x[0])
for k, v in sorted_company:
    print(k)
    for i in v:
        print(f"-- {i}")