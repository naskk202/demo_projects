word = input()
my_dict = {}

for char in word:
    if char not in my_dict:
        my_dict[char] = 0
    my_dict[char] += 1
my_dict.pop(" ")

for k, v in my_dict.items():
    print(f"{k} -> {v}")