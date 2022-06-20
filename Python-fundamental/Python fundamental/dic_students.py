# command = input()
#
# my_dict = {}
#
# while command[0].isupper():
#     command = command.split(":")
#     if command[2] in my_dict:
#         my_dict[command[2]] += [command[0], command[1]]
#     else:
#         my_dict[command[2]] = [command[0], command[1]]
#     command = input()
# for i in range(0, len(my_dict[command]), 2):
#     print(f"{my_dict[command][i]} - {my_dict[command][i + 1]}")


command = input()
my_dict = {}

while command[0].isupper():
    name, student_id, course = command.split(":")
    if course not in my_dict:
        my_dict[course] = {}
    my_dict[course][name] = student_id
    command = input()
command = command.split("_")
command = " ".join(command)

searched_class = {k: v for k, v in my_dict[command].items()}

for k, v in searched_class.items():
    print(f"{k} - {v}")