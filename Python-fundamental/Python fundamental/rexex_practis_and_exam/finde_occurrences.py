import re

data = input()
word = input()
word = word.lower()
data = data.lower()
a = re.findall(r"\b" + word + r"\b(?=\.!\?)?", data)

print(len(a))