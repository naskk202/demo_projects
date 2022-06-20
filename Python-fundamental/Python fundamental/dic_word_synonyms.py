my_dict = {}

for i in range(int(input())):
    command = input()
    synonym = input()
    if command not in my_dict:
        my_dict[command] = []
    my_dict[command].append(synonym)
for k, v in my_dict.items():
    print(f"{k} - {', '.join(v)}")