command = input()
my_dict = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in my_dict.keys():
        my_dict[course] = []
    my_dict[course].append(student)
    command = input()
for k, v in my_dict.items():
    my_dict[k] = sorted(v)
ordered_dict = sorted(my_dict.items(), key=lambda x: -len(x[1]))

for k, v in ordered_dict:
    print(f"{k}: {len(v)}")
    for i in range(len(v)):
        print(f"-- {v[i]}")