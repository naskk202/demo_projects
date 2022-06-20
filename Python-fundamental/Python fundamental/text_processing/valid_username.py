names = input().split(", ")
for name in names:
    if 2 < len(name) < 17:
        valid = "1234567890qwertyuiopasdfghjklzxcvbnm-_QWERTYUIOPASDFGHJKLZXCVBNM"
        set_name = set(name)
        if set_name.issubset(valid):
            print(name)
