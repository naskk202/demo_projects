import re
a = []
data = input()
while data:
    a.extend(re.findall(r"\d+", data))
    data = input()

print(*a)


