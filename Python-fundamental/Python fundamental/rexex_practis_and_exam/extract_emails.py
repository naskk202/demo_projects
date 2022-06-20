import re

data = input()

pattern = r"(?<=\s)\b[A-Za-z\d]+[\-\.\_]?[a-zA-Z\d]*@[a-z]+[a-z\.\-]*\.[a-z]+\b"

email = re.finditer(pattern, data)

for i in email:
    print(i.group())