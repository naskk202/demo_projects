try:
    file = open("first table", "a")
    file2 = open("new_one.txt", "r")
    name = file2.readline().split(", ")
    print(name)
    new_names = {name[i]: name[i + 1] for i in range(0, len(name), 2)}
    file.write("".join(f"name: {k}\n"
              f"quantity: {v}\n"
              f"-----------------\n"for k, v in new_names.items()))
except:
    print("ne stana")

try:
    file = open("first table.txt", "r")
    a = file.readline().split(", ")
    print(a)
    print(a[2])

except:
    print("ZzZzZz")
