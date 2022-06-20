my_dict = {}
for i in range(int(input())):
    student = input()
    grade = float(input())
    if student not in my_dict.keys():
        my_dict[student] = grade
    else:
        my_dict[student] = (my_dict[student] + grade) / 2

sorted_students = sorted(my_dict.items(), key=lambda x: -x[1])

for k, v in sorted_students:
    if v >= 4.5:
        print(f"{k} -> {v:.2f}")